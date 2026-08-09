# IoT Fall Detection Device

Reference firmware for an MPU6050-based fall detection prototype. The logic looks for a high-impact acceleration event followed by a low-motion state and triggers a local alert.

## Hardware
- Arduino-compatible microcontroller
- MPU6050 accelerometer/gyroscope
- Buzzer or alert actuator

## Important
Thresholds are prototype values and must be calibrated against real sensor data before any safety-critical use.
