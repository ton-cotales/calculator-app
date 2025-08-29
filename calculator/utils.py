from pathlib import Path
from tkinter import PhotoImage


CALCULATOR_DIR = Path(__file__).resolve().parent
ASSETS_DIR = CALCULATOR_DIR.parent / 'assets'

def has_application_icons() -> bool:
    icons_dir = ASSETS_DIR / 'icons'
    if icons_dir.is_dir():
        file_count = [i for i in icons_dir.iterdir()]
        if len(file_count) == 26:
            return True
    return False

def get_image_data() -> dict:
    data = {}
    if has_application_icons():
        icons_dir = ASSETS_DIR / 'icons'
        for file in icons_dir.iterdir():
            if file.suffix == '.png':
                name = file.name.strip().replace(' ', '_')
                data[name.lower()] = str(file)
    return data

def load_image(image_path: str) -> PhotoImage:
    return PhotoImage(file=image_path)