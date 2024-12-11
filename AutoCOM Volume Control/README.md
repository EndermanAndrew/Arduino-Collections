# AutoCOM Volume Control

This project allows automatic detection of the correct COM port for an Arduino and uses a potentiometer to control the volume of your computer. The volume level is displayed on the screen using the volume OSD (On-Screen Display).

## Features
- Automatically detects the correct COM port for the Arduino.
- Reads potentiometer values from the Arduino.
- Adjusts the computer's volume based on potentiometer input.
- Displays the volume level on the screen using the OSD.

## Requirements
- Python 3.x
- Arduino with a potentiometer connected
- Required Python packages (listed in `requirements.txt`):
  - pyserial
  - pycaw
  - comtypes
  - pynput

## Installation
1. **Download the files**

2. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Replace 'COM__'** with your Arduino's serial port, by editing the **main.py**

## Usage
1. **Connect your Arduino** with a potentiometer to your computer.

2. **Run the script**:
    ```sh
    python main.py
    ```

3. **Adjust the potentiometer** to control the volume level.

## Code Explanation
The script performs the following tasks:
1. **Find Arduino**: Attempts to connect to available COM ports to find the Arduino.
2. **Audio Utilities**: Uses the Pycaw library to get the default audio endpoint and control the volume.
3. **Volume Adjustment**: Converts potentiometer values (0-1023) to volume levels (0.0-1.0) and adjusts the computer's volume accordingly.
4. **OSD Trigger**: Simulates volume up key press to trigger the OSD for visual feedback.

## Troubleshooting
- **Error opening serial port**: Ensure that your Arduino is connected and the correct COM port is used.
- **Volume adjustment not working**: Ensure that the Pycaw library is installed and configured correctly.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgements
- Pycaw library for audio control
- Pynput library for keyboard control
- Arduino community for providing inspiration and resources
