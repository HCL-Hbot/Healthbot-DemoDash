from PyQt5.QtWidgets import QWidget, QSlider, QPushButton, QSpinBox, QLabel, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QComboBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from Serial_com import SerialComm

class Gui(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.serial_comm = SerialComm()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Healthbot | DEMO DASH v1.1")
        self.resize(1600, 800)

        self.cheekLEDButton = QPushButton("Cheek LED")
        self.cheekLEDButton.setCheckable(True)
        self.cheekLEDButton.setChecked(False)
        self.cheekLEDButton.clicked.connect(self.cheekLEDButtonClicked)

        self.hsv_group = QGroupBox("HSV Color Picker")
        self.hsv_layout = QVBoxLayout()
        self.hsv_group.setLayout(self.hsv_layout)

        self.hue_layout = QHBoxLayout()
        self.hue_label = QLabel("Hue (0-359):")
        self.hue_slider = QSlider(Qt.Horizontal)
        self.hue_slider.setRange(0, 359)
        self.hue_layout.addWidget(self.hue_label)
        self.hue_layout.addWidget(self.hue_slider)
        self.hsv_layout.addLayout(self.hue_layout)

        self.sat_layout = QHBoxLayout()
        self.sat_label = QLabel("Saturation (0-255):")
        self.sat_slider = QSlider(Qt.Horizontal)
        self.sat_slider.setRange(0, 255)
        self.sat_slider.setValue(255)  # Start with full saturation
        self.sat_layout.addWidget(self.sat_label)
        self.sat_layout.addWidget(self.sat_slider)
        self.hsv_layout.addLayout(self.sat_layout)

        self.val_layout = QHBoxLayout()
        self.val_label = QLabel("Value (0-255):")
        self.val_slider = QSlider(Qt.Horizontal)
        self.val_slider.setRange(0, 255)
        self.val_slider.setValue(255)  # Start with full brightness
        self.val_layout.addWidget(self.val_label)
        self.val_layout.addWidget(self.val_slider)
        self.hsv_layout.addLayout(self.val_layout)       

        self.color_preview = QLabel()
        self.color_preview.setFixedSize(100, 100)
        self.color_preview.setStyleSheet("background-color: #000000; border: 1px solid black;")
        self.hsv_layout.addWidget(self.color_preview, alignment=Qt.AlignCenter)

        self.set_color_button = QPushButton("Set LED Color")
        self.set_color_button.clicked.connect(self.setLEDColorClicked)
        self.hue_slider.valueChanged.connect(self.updateColorPreview)
        self.sat_slider.valueChanged.connect(self.updateColorPreview)
        self.val_slider.valueChanged.connect(self.updateColorPreview)

        self.led_anim_widget = QWidget()
        self.anim_layout = QVBoxLayout()
        self.led_anim_widget.setLayout(self.anim_layout)

        self.anim_group = QGroupBox("LED Animations")
        self.anim_inner_layout = QVBoxLayout()
        self.anim_group.setLayout(self.anim_inner_layout)
        self.anim_layout.addWidget(self.anim_group)

        self.anim_label = QLabel("Select Animation:")
        self.anim_combo = QComboBox()
        self.anim_combo.addItems(["Solid Color", "Fade In", "Fade Out", "Blink", "Rainbow", "Strobe"])
        self.anim_inner_layout.addWidget(self.anim_combo)

        self.pick_LED_strip = QGroupBox("Pick LED Strip")
        self.pick_LED_strip_layout = QVBoxLayout()
        self.pick_LED_strip.setLayout(self.pick_LED_strip_layout)

        self.pick_LED_strip_spinbox = QSpinBox()
        self.pick_LED_strip_spinbox.setRange(0, 1)
        self.pick_LED_strip_spinbox.setValue(0)
        self.pick_LED_strip_layout.addWidget(self.pick_LED_strip_spinbox)

        self.set_eye_button = QPushButton("Set eye")
        self.set_eye_button.clicked.connect(self.setEyeClicked)

        self.eye_anim_widget = QWidget()
        self.eye_anim_layout = QVBoxLayout()
        self.eye_anim_widget.setLayout(self.eye_anim_layout)
        
        self.eye_anim_group = QGroupBox("Eye Animations")
        self.eye_anim_inner_layout = QVBoxLayout()
        self.eye_anim_group.setLayout(self.eye_anim_inner_layout)
        self.eye_anim_layout.addWidget(self.eye_anim_group)
        self.eye_anim_combo = QComboBox()
        self.eye_anim_combo.addItems(["None", "Blink", "Think", "Confusion"])
        self.eye_anim_combo.setCurrentIndex(0)
        self.eye_anim_inner_layout.addWidget(self.eye_anim_combo)

        self.pick_eye = QGroupBox("Pick eye")
        self.pick_eye_layout = QVBoxLayout()
        self.pick_eye.setLayout(self.pick_eye_layout)

        self.pick_eye_spinbox = QSpinBox()
        self.pick_eye_spinbox.setRange(0, 1)
        self.pick_eye_spinbox.setValue(0)
        self.pick_eye_layout.addWidget(self.pick_eye_spinbox)

        self.eye_x_spinbox = QSpinBox()
        self.eye_x_spinbox.setRange(0, 240)
        self.eye_x_spinbox.setValue(120)
        self.eye_x_spinbox.setSuffix(" px")

        self.eye_y_spinbox = QSpinBox()
        self.eye_y_spinbox.setRange(0, 240)
        self.eye_y_spinbox.setValue(120)
        self.eye_y_spinbox.setSuffix(" px")

        self.head_azimuth_spinbox = QSpinBox()
        self.head_azimuth_spinbox.setRange(0, 180)
        self.head_azimuth_spinbox.setValue(90)
        self.head_azimuth_spinbox.setSuffix(" °")

        self.head_elevation_spinbox = QSpinBox()
        self.head_elevation_spinbox.setRange(0, 180)
        self.head_elevation_spinbox.setValue(90)        
        self.head_elevation_spinbox.setSuffix(" °")
        self.head_speed_spinbox = QSpinBox()
        self.head_speed_spinbox.setSuffix(" rpm")
        self.set_head_button = QPushButton("Set head")
        self.set_head_button.clicked.connect(self.setHeadClicked)

        self.layout.addWidget(self.head_speed_spinbox, 2, 2)
        self.layout.addWidget(self.head_elevation_spinbox, 2, 3)
        self.layout.addWidget(self.head_azimuth_spinbox, 2, 4)
        self.layout.addWidget(self.set_head_button, 2, 6)

        self.layout.addWidget(self.pick_eye, 3, 1)        
        self.layout.addWidget(self.eye_anim_widget, 3, 2)
        self.layout.addWidget(self.eye_x_spinbox, 3, 3)
        self.layout.addWidget(self.eye_y_spinbox, 3, 4)
        self.layout.addWidget(self.set_eye_button, 3, 6)
        
        self.layout.addWidget(self.pick_LED_strip, 4, 1)        
        self.layout.addWidget(self.led_anim_widget, 4, 2)
        self.layout.addWidget(self.hsv_group, 4, 5)
        self.layout.addWidget(self.set_color_button, 4, 6)
        self.layout.addWidget(self.cheekLEDButton, 5, 6)

    def cheekLEDButtonClicked(self):
        self.serial_comm.send("Cheek LED")
        print("Cheek LED clicked")

    def setLEDColorClicked(self):
        h = self.hue_slider.value()
        s = self.sat_slider.value()
        v = self.val_slider.value()
        strip_nr = self.pick_LED_strip_spinbox.value()
        anim = self.anim_combo.currentText()
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

    def setEyeClicked(self):
        eye_nr = self.pick_eye_spinbox.value()
        x = self.eye_x_spinbox.value()
        y = self.eye_y_spinbox.value()
        anim = self.eye_anim_combo.currentText()

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

    def setHeadClicked(self):
        speed = self.head_speed_spinbox.value()
        azimuth = self.head_azimuth_spinbox.value()
        elevation = self.head_elevation_spinbox.value()
        
        command = f"\nM101 1 {speed}\r\n" # First motor
        self.serial_comm.send(command)
        command = f"M101 2 {speed}\r\n" # Second motor
        self.serial_comm.send(command)
        command = f"M102 1 {azimuth}\r\n" # First motor
        self.serial_comm.send(command)
        command = f"M102 2 {elevation}\r\n"
        self.serial_comm.send(command)
        
        print(f"Set head to azimuth {azimuth}, elevation {elevation} with speed {speed}")

    def updateColorPreview(self):
        h = self.hue_slider.value()
        s = self.sat_slider.value() / 255.0
        v = self.val_slider.value() / 255.0
        color = QColor.fromHsvF(h / 359.0, s, v)
        self.color_preview.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;")
