from PyQt5.QtWidgets import QWidget, QSlider, QPushButton, QSpinBox, QLabel, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QComboBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from Serial_com import SerialComm
from BrainAPI_Handlers import Handlers

class Gui(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.serial_comm = SerialComm()
        self.handlers = Handlers(self.serial_comm)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Healthbot | DEMO DASH v1.1")
        self.resize(1600, 800)

        self.cheekLEDButton = QPushButton("Cheek LED")
        self.cheekLEDButton.setCheckable(True)
        self.cheekLEDButton.setChecked(False)
        self.cheekLEDButton.clicked.connect(self.handlers.cheekLEDButtonClicked)

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
        self.set_color_button.clicked.connect(lambda: self.handlers.setLEDColorClicked(self.hue_slider, self.sat_slider, self.val_slider, self.pick_LED_strip_spinbox, self.anim_combo))
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
        self.set_eye_button.clicked.connect(lambda: self.handlers.setEyeClicked(self.pick_eye_spinbox, self.eye_x_spinbox, self.eye_y_spinbox, self.eye_anim_combo))

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
        self.set_head_button.clicked.connect(lambda: self.handlers.setHeadClicked(self.head_speed_spinbox, self.head_azimuth_spinbox, self.head_elevation_spinbox))

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

    def updateColorPreview(self):
        h = self.hue_slider.value()
        s = self.sat_slider.value() / 255.0
        v = self.val_slider.value() / 255.0
        color = QColor.fromHsvF(h / 359.0, s, v)
        self.color_preview.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;")
