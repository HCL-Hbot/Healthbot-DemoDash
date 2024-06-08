# Healthbot Demo Dashboard 
This repository contains the Healthbot Demonstration GUI Dashboard. This dashboard is designed to provide a convenient interface for functional debugging, external events manual demonstration, and robot manual control.

## Features 
- COM Port Selection: Dynamically select and set the COM port for serial communication.
- HSV Color Picker: Adjust the hue, saturation, and value to set the color of the LED strip.
- LED Animations: Choose from various animations such as Solid Color, Fade In, Fade Out, Blink, Rainbow, and Strobe.
- Eye Animations: Control the eye animations with options like None, Blink, Think, and Confusion.
- Head Movement: Set the speed, azimuth, and elevation for the robot's head movement.
- Cheek LED Control: Toggle the cheek LED on and off.

![Example of the Dashboard](Docs/Dashboard%20Example.png)

## Installation
1) Clone the repository:
```bash
git clone https://github.com/your-username/Healthbot-DemoDash.git
cd Healthbot-DemoDash
```

2) Install the required dependencies: 
```bash
pip install pyqt5
```

3) Run the application:
```bash
python main.py
```

4) Navigate the interface:
*Main Tab*: Control the LED colors, animations, eye animations, and head movement.
*Settings Tab*: Select and set the COM port for serial communication.

## File Structure
- main.py: Entry point to run the application.
- gui.py: Contains the Gui class, which sets up the user interface and manages the main and settings tabs.
- serial_comm.py: Handles the serial communication with the robot.
- handlers.py: Contains handler functions for various actions triggered by the GUI elements.
