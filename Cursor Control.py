import serial
import pyautogui
import time

arduino_port = 'COM3'  # Replace with your port
baud_rate = 115200
arduino = serial.Serial(arduino_port, baud_rate, timeout=0.1)

movement_map = {
    "LEFT": (-30, 0),
    "RIGHT": (30, 0),
    "UP": (0, -30),
    "DOWN": (0, 30)
}

print("Starting fast 90° tilt control...")

last_direction = None
last_move_time = 0
move_interval = 0.1  # Move every 100ms when held

while True:
    try:
        line = arduino.readline().decode('utf-8').strip()
        if not line:
            continue

        print(f"Received: {line}")

        current_time = time.time()
        if line in movement_map:
            if line != last_direction or (current_time - last_move_time) > move_interval:
                dx, dy = movement_map[line]
                pyautogui.moveRel(dx, dy)
                last_direction = line
                last_move_time = current_time
        else:
            last_direction = None  # Reset on NEUTRAL or unknown

    except Exception as e:
        print("Error:", e)
