import os
from ez_settings import EZSettings
SETTINGS_PATH = os.path.join(os.path.expanduser("~"), "dcs_kneeboard_creator_settings.json")
EZSettings(SETTINGS_PATH)