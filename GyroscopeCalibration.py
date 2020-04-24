import time
import smbus
import math

CTRL_REG1 = 0x20
CTRL_REG2 = 0x21
CTRL_REG3 = 0x22
CTRL_REG4 = 0x23
CTRL_REG5 = 0x24
CTRL_REG6 = 0x25

gyroI2CAddr = 105
gyroRaw = []
gyroDPS = []
heading = []
gyroZeroRate = []
gyroThreshold = []

NUM_GYRO_SMAPLES = 50
GYRO_SIGMA_MULTIPLE = 3

dpsPerDigit = 0.00875

setupGyro()
calibrateGyro()
printHeadings()

def printDPS():
	print(gyroDPS[0],gyroDPS[1],gyroDPS[2])

def printHeadings():
	print(heading[0],heading[1],heading[2])

def updateHeadings():
	deltaT = getDeltaTMicros()
	for i in range(3):
		heading[i] = heading[i] - gyroDPS[i]*deltaT/1000000

def getDeltaTMicros():
	lastTime = 0
	currentTime = time.time()
	deltaT = currentTime - lastTime
	if deltaT < 0.0:
		deltaT = currentTime+(4294967295-lastTime)
	lastTime = currentTime
	return deltaT

def testCalibration():
	calibrateGyro()
	for i in range(3):
		print(gyroZeroRate[i],gyroThreshold[i])


def setupGyro():
	gyroWriteI2C(CTRL_REG1,0x1F)
	gyroWriteI2C(CTRL_REG3,0x08)
	setGyroSensitivity500()
	time.sleep(0.1)

def calibrateGyro():
	gyroSums = []
	gyroSigma = []

	for i in range(NUM_GYRO_SMAPLES):
		updateGyroValues()
		for i in range(3):
			gyroSums[i] += gyroRaw[i]
			gyroSigma[i] += gyroRaw[i]*gyroRaw[i]

	for i in range(3):
		averageRate = gyroSums[i]/NUM_GYRO_SMAPLES
		gyroZeroRate[i] = averageRate
		gyroThreshold[i] = math.sqrt((double(gyroSigma[j]) / NUM_GYRO_SAMPLES) - (averageRate * averageRate)) * GYRO_SIGMA_MULTIPLE

def updateGyroValues():
	while (!(gyroReadI2C(0x27) and b00001000)):
		print(0,0,0)

	reg = 0x28
	for i in range(3):
		gyroRaw[i] = gyroReadI2C(reg) | gyroReadI2C(reg+1) << 8
		reg += 2

	deltaGyro = []
	for i in range(3):
		deltaGyro.append((gyroRaw[i]-gyroZeroRate[i])) 
		if (math.abs(deltaGyro[i] < gyroThreshold[i])):
			deltaGyro[i] = 0
		gyroDPS[i] = dpsPerDigit*deltaGyro[i]

def setGyroSensitivity250():
	dpsPerDigit = 0.00875
	gyroWriteI2C(CTRL_REG4,0x80)

def setGyroSensitivity500():
	dpsPerDigit = .0175
	gyroWriteI2C(CTRL_REG4,0x90)

def setGyroSensitivity2000():
	dpsPerDigit = .0.07
	gyroWriteI2C(CTRL_REG4,0xA0)


def gyroReadI2C (regAddr):
	bus.write_byte_data(gyroI2CAddr,regAddr)
	val = bus.read_byte_data(gyroI2CAddr,1)
	return val

def gyroWriteI2C(regAddr, val):
	bus.write_byte_data(gyroI2CAddr,regAddr,val)


