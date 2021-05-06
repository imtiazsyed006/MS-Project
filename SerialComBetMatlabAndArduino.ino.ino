uint8_t received[4];
void setup() 
{

  Serial.begin(9600); // other values include 9600, 14400, 57600 etc.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Use readSensor() function to get pressure and temperature reading. 
  
  int32_t tempValue = 97800;
  int one  = tempValue  & 0xff;
  int two = (tempValue >> 8) & 0xff;
  int three =  (tempValue >> 16) & 0xff;
  int four =  (tempValue >> 24) & 0xff;

//  int32_t tempValue = 97800;
//  int one  = (tempValue >> 24) & 0xff;
//  int two = (tempValue >> 16) & 0xff;
//  int three =  (tempValue >> 8) & 0xff;
//  int four =  (tempValue) & 0xff;
for (int i = 0; i<4; i++)
{
  received[i] = Serial.read();
}

//  int one  = tempValue  & 0xff;
//  int two = (tempValue >> 8) & 0xff;
//  int three =  (tempValue >> 16) & 0xff;
//  int four =  (tempValue >> 24) & 0xff;
  Serial.write(83);
  Serial.write(received[0]);
  Serial.write(received[1]);
  Serial.write(received[2]);
  Serial.write(received[3]);
  Serial.write(69);

//  Serial.write(83);
//  Serial.write(one);
//  Serial.write(two);
//  Serial.write(three);
//  Serial.write(four);
//  Serial.write(69);


  delay(50);  
}
