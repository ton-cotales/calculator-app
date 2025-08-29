from tkinter import Tk
from calculator.ui import CalculatorUI


class CalculatorApp:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('Calculator')
        self.root.geometry(self.new_geometry(280, 340))
        
        self.ui = CalculatorUI(self.root)
        
    def new_geometry(self, width: int, height: int) -> str:
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        x, y = (0, 0)
        
        if width < scrn_width and height < scrn_height:
            x = (scrn_width - width) // 2
            y = (scrn_height - height) // 3
            
        return f"{width}x{height}+{x}+{y}"
    
    def run(self):
        self.root.mainloop()