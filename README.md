# Cursor Control Using Gyro Sensor (MPU6050 + Arduino + Python)

This project allows you to control your computer mouse cursor using an **MPU6050 accelerometer and gyroscope sensor** connected to an **Arduino Uno**. The sensor captures motion and tilt data, which is sent via serial communication to a Python script that moves the cursor accordingly.  
By tilting the sensor about 90 degrees in different directions, you can move the cursor **up, down, left, or right**.

---

##  Features
- Cursor control using **MPU6050 sensor**.
- Tilt detection mapped to specific cursor movements.
- Real-time motion processing with Arduino and Python.
- Expandable for **gesture-based clicking, scrolling, or gaming controls**.

---

##  Components Required
- Arduino Uno (R3 DIP/SMD)
- MPU6050 Accelerometer + Gyroscope sensor
- Jumper Wires (Male-to-Female recommended)
- USB Cable (for Arduino-PC connection)
- (Optional) Push Buttons / Flex Sensors for clicks

---

##  Connections
| MPU6050 Pin | Arduino Uno Pin |
|-------------|-----------------|
| VCC         | 5V              |
| GND         | GND             |
| SCL         | A5 (SCL)        |
| SDA         | A4 (SDA)        |

---

##  Project Structure
