from pywinauto.application import Application
import configparser

CONFIG_FILE = 'config.ini'

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

def save_config(monitor, area_size):
    config = configparser.ConfigParser()
    config['Settings'] = {
        'monitor': monitor,
        'area_size': area_size
    }
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def configure_tablet(monitor, area_size):
    app = Application().start(r'C:\Users\arugg\AppData\Roaming\Pentablet V3')  # Path to your Pentablet V3 utility file
    window = app.window(title="XP-Pen configuration")

    window['MonitorDropdown'].select(monitor)
    window['AreaSizeInput'].set_text(area_size)
    window['ApplyButton'].click()