from PyQt5 import QtWidgets
from tablet_config import configure_tablet, load_config, save_config

class TabletConfigApp:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Tablet Configuration")

        self.layout = QtWidgets.QVBoxLayout()

        self.monitor_label = QtWidgets.QLabel('Select Monitor:')
        self.monitor_input = QtWidgets.QComboBox()
        self.monitor_input.addItems(['Monitor 1', 'Monitor 2'])
        self.layout.addWidget(self.monitor_label)
        self.layout.addWidget(self.monitor_input)

        self.area_label = QtWidgets.QLabel('Tablet Area Size:')
        self.area_input = QtWidgets.QLineEdit('Default Area Size')
        self.layout.addWidget(self.area_label)
        self.layout.addWidget(self.area_input)

        self.apply_button = QtWidgets.QPushButton('Apply')
        self.apply_button.clicked.connect(self.apply_settings)
        self.layout.addWidget(self.apply_button)

        self.window.setLayout(self.layout)

        self.load_settings()

    def load_settings(self):
        config = load_config()
        monitor = config.get('Settings', 'monitor', fallback='Monitor 1')
        area_size = config.get('Settings', 'area_size', fallback='Default Area Size')

        self.monitor_input.setCurrentText(monitor)
        self.area_input.setText(area_size)

    def apply_settings(self):
        monitor = self.monitor_input.currentText()
        area_size = self.area_input.text()
        configure_tablet(monitor, area_size)
        save_config(monitor,area_size)
        QtWidgets.QMessageBox.information(self.window, "Tablet Configuration", "Settings applied successfully!")

    def run(self):
        self.window.show()
        self.app.exec_()



    