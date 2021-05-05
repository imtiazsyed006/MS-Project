
#include "BNO055.h"
#include <MS5803_05.h> 
#include <Wire.h>

#define A 0X28  //I2C address selection pin LOW
#define B 0x29  //                          HIGH

BNO055 mySensor(A);



MS_5803 sensor = MS_5803(512);
float value = 0;
void setup() 
{

  Wire.begin();
  Serial.begin(9600); // other values include 9600, 14400, 57600 etc.
  mySensor.init();
  if (sensor.initializeMS_5803()) 
  {
  } 
}

void loop() {
  // Use readSensor() function to get pressure and temperature reading. 
  sensor.readSensor();
  mySensor.readEul();
  value = sensor.pressure()*100;
  //Serial.print(value);
  int32_t tempValue = value;
  //Serial.println(tempValue);
  uint8_t one  = tempValue  & 0xff;
  uint8_t two = (tempValue >> 8) & 0xff;
  uint8_t three =  (tempValue >> 16) & 0xff;
  uint8_t four =  (tempValue >> 24) & 0xff;
  value = mySensor.euler.x;
  tempValue = value*100;
  uint8_t five  = tempValue  & 0xff;
  uint8_t six = (tempValue >> 8) & 0xff;
  uint8_t seven =  (tempValue >> 16) & 0xff;
  uint8_t eight =  (tempValue >> 24) & 0xff;
  Serial.write(83);
  Serial.write(one);
  Serial.write(two);
  Serial.write(three);
  Serial.write(four);
  Serial.write(five);
  Serial.write(six);
  Serial.write(seven);
  Serial.write(eight);
  Serial.write(69);
  
}
