-- IoT Fall Detection Device: Arduino-style reference firmware
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;
const int BUZZER = 8;
const float IMPACT_THRESHOLD = 2.5;
const float LOW_MOTION_THRESHOLD = 0.35;

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER, OUTPUT);
  if (!mpu.begin()) {
    Serial.println("MPU6050 not detected");
    while (true) delay(100);
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  float magnitude = sqrt(a.acceleration.x*a.acceleration.x + a.acceleration.y*a.acceleration.y + a.acceleration.z*a.acceleration.z) / 9.80665;
  bool impact = magnitude > IMPACT_THRESHOLD;
  bool lowMotion = magnitude < LOW_MOTION_THRESHOLD;

  if (impact) {
    delay(500);
    mpu.getEvent(&a, &g, &temp);
    float after = sqrt(a.acceleration.x*a.acceleration.x + a.acceleration.y*a.acceleration.y + a.acceleration.z*a.acceleration.z) / 9.80665;
    if (after < LOW_MOTION_THRESHOLD) {
      digitalWrite(BUZZER, HIGH);
      Serial.println("Potential fall detected");
      delay(3000);
      digitalWrite(BUZZER, LOW);
    }
  }
  delay(100);
}
