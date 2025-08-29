from tkinter import Tk, Frame
from calculator import utils


class CalculatorUI:
    def __init__(self, root: Tk):
        
        self.root = root
        self.images = utils.get_image_data()
        
        self.create_widgets()
        
    def create_widgets(self):
        top_frame = Frame(
            master=self.root,
            name='top_frame'
        )
        top_frame.place(relwidth=1, relheight=0.35)
        