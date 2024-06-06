from PyQt5.QtGui import QColor
import time

class Handlers:
    def __init__(self, serial_comm):
        self.serial_comm = serial_comm

    def cheekLEDButtonClicked(self):
        self.serial_comm.send("Cheek LED")
        print("Cheek LED clicked")

    def setLEDColorClicked(self, hue_slider, sat_slider, val_slider, pick_LED_strip_spinbox, anim_combo):
        h = hue_slider.value()
        s = sat_slider.value()
        v = val_slider.value()
        strip_nr = pick_LED_strip_spinbox.value()
        anim = anim_combo.currentText()
        color = QColor.fromHsv(h, s, v)
        r, g, b = color.red(), color.green(), color.blue()

        # Set RGB command
        command = f"LS101 {strip_nr} {r} {g} {b}\r\n"
        self.serial_comm.send(command)

        if anim == "Blink":
            duration = 1000 
            command = f"LS102 {strip_nr} {r} {g} {b} {duration}\r\n"
            self.serial_comm.send(command)
        elif anim == "Fade In":
            duration = 1000 
            command = f"LS104 {strip_nr} {duration}\r\n"
            self.serial_comm.send(command)
        elif anim == "Fade Out":
            duration = 1000  
            command = f"LS103 {strip_nr} {duration}\r\n"
            self.serial_comm.send(command)
        elif anim == "Solid Color":
            # No additional command needed for solid color
            pass
        else:
            print(f"Animation {anim} is not implemented")

        print(f"Set LED strip {strip_nr} color to HSV({h}, {s}, {v}), RGB({r}, {g}, {b}) with {anim} animation")

    def setEyeClicked(self, pick_eye_spinbox, eye_x_spinbox, eye_y_spinbox, eye_anim_combo):
        eye_nr = pick_eye_spinbox.value()
        x = eye_x_spinbox.value()
        y = eye_y_spinbox.value()
        anim = eye_anim_combo.currentText()

        # Move display command
        command = f"DS101 {eye_nr} {x} {y} 1000\r\n"  
        self.serial_comm.send(command)

        # Animation commands
        if anim == "Blink":
            command = f"DS102 {eye_nr} 1\r\n"  # Blink
        elif anim == "Confusion":
            command = f"DS103 {eye_nr} 1\r\n"  # Confusion
        elif anim == "Think":
            command = f"DS104 {eye_nr} 1\r\n"  # Think
        else:
            print(f"Animation {anim} is not implemented")
            return

        self.serial_comm.send(command)
        print(f"Set eye {eye_nr} to position ({x}, {y}) with {anim} animation")

    def setHeadClicked(self, head_speed_spinbox, head_azimuth_spinbox, head_elevation_spinbox):
        speed = head_speed_spinbox.value()
        azimuth = head_azimuth_spinbox.value()
        elevation = head_elevation_spinbox.value()
        
        command = f"M101 1 {speed}\r\n"  # First motor
        self.serial_comm.send(command)
        command = f"M102 1 {azimuth}\r\n" 
        self.serial_comm.send(command)
        command = f"M101 2 {speed}\r\n"  # Second motor
        self.serial_comm.send(command)
        command = f"M102 2 {elevation}\r\n"
        self.serial_comm.send(command)
        
        print(f"Set head to azimuth {azimuth}, elevation {elevation} with speed {speed}")
