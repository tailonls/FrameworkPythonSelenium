import os
import json

settings = None


def load_settings():
    global settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        settings = json.load(f)
        print('Settings carregado com sucesso!')


load_settings()
