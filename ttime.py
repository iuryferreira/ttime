from datetime import datetime
from settings import THEMES, VSCODE_CONFIG_FILE
from json import dump, load
from os import system


def get_theme():

    hour = datetime.now().hour

    if hour >= 6 and hour < 18:
        return THEMES['LIGHT']

    return THEMES['DARK']


def set_vscode_theme():

    data = None

    with open(VSCODE_CONFIG_FILE) as config_file:

        data = load(config_file)
        current = data['workbench.colorTheme']
        data['workbench.colorTheme'] = get_theme()['VSCODE']

    with open(VSCODE_CONFIG_FILE, "w") as config_file:
        dump(data, config_file)


def set_desktop_theme():

    system(
        'gsettings set org.gnome.desktop.interface gtk-theme "{0}"'.format(get_theme()['DESKTOP']))


if __name__ == "__main__":

    set_desktop_theme()
    set_vscode_theme()
