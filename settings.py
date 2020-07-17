from pathlib import Path

VSCODE_CONFIG_FILE = "{0}/.config/Code/User/settings.json".format(
    str(Path.home()))

THEMES = {
    "LIGHT": {
        "DESKTOP": "Plata-Lumine-Compact",
        "VSCODE": "Solus OS Light"
    },
    "DARK": {
        "DESKTOP": "Plata-Noir-Compact",
        "VSCODE": "Solus OS Dark"
    }
}

TIME_HOUR_LIGHT_THEME = {
    "START": 6,
    "END": 17
}
