
#include "Wire.h"
#include <SoftwareSerial.h>
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

long timer = 0;
float SAMPLING_RATE = 0.05;
void setup() {
  Serial.begin(115200);
  Wire.begin();
  byte status = mpu.begin();
  Serial.print("MPU6050 status: ");
  Serial.println(status);
  while(status!=0){ } 
  
  Serial.println("Calculating offsets, do not move MPU6050");
  delay(1000);
  mpu.calcOffsets(true,true); 
//  Serial.println("Done!");
  Serial.println("=======================================================");
  Serial.println("Author: Soheil Dolatabadi\nMicroprocessor: Arduino Pro Micro\nAcc sensor: MPU6050\nSampling rate: " + String(SAMPLING_RATE) + " PerSec");
  Serial.println("=======================================================");
}



void loop() {
  mpu.update();

  if(millis() - timer > int(SAMPLING_RATE * 1000)){ // print data every second
    
    Serial.print("$START$TEMP:");Serial.print(mpu.getTemp());
    
    Serial.print("$ACC:");Serial.print(mpu.getAccX());
    Serial.print("$");Serial.print(mpu.getAccY());
    Serial.print("$");Serial.print(mpu.getAccZ());
  
    Serial.print("$GYR:");Serial.print(mpu.getGyroX());
    Serial.print("$");Serial.print(mpu.getGyroY());
    Serial.print("$");Serial.print(mpu.getGyroZ());
  
    Serial.print("$END$\n");
    timer = millis();
  }

}
