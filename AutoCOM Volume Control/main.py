import serial
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pynput.keyboard import Key, Controller
import time

# Replace 'COM__' with your Arduino's serial port
try:
    ser = serial.Serial('COM6', 9600)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Get default audio endpoint (speakers/headphones)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

keyboard = Controller()

last_volume_level = -1

def adjust_volume(volume_level):
    global last_volume_level
    if abs(volume_level - last_volume_level) > 0.01:  # Update only if there's a significant change
        last_volume_level = volume_level
        # Set the volume level
        volume.SetMasterVolumeLevelScalar(volume_level, None)
        # Trigger volume OSD by simulating volume up key press
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        # Small delay to ensure the OSD is shown
        time.sleep(0.01)
        # Return volume to desired level without changing it
        volume.SetMasterVolumeLevelScalar(volume_level, None)

while True:
    try:
        if ser.in_waiting:
            raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
            if raw_data.isdigit():
                pot_value = int(raw_data)
                # Convert the potentiometer value (0-1023) to volume level (0.0-1.0)
                volume_level = pot_value / 1023.0
                # Adjust the volume and trigger OSD
                adjust_volume(volume_level)
                print(f"Potentiometer value: {pot_value}, Volume level: {int(volume_level * 100)}%")
    except Exception as e:
        print(f"Error: {e}")
        break
