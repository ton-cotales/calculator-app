from tkinter import Tk, Frame, Label, Entry
from calculator import logic
from calculator import utils


class CalculatorUI:
    def __init__(self, root: Tk):
        
        self.root = root
        self.calc = logic.Calculator()
        self.font = utils.get_custom_font()
        self.images = {
            k: utils.load_image(v) for k, v in
            utils.get_image_data().items()
        }
        
        self.create_widgets()
        
    def create_widgets(self):

        background = '#303030'
        display_background = '#97B172'
        
        # Display border image
        border_image = Label(
            master=self.root,
            image=self.images['image.png'],
            background=background
        )
        border_image.place(relwidth=1, relheight=0.38)
        
        # Container for widgets inside the display
        display_container = Frame(
            master=self.root,
            name='display_container',
            bg=display_background
        )
        display_container.place(
            relx=0.07, rely=0.105,
            relwidth=0.86, relheight=0.165
        )
        # Memory indicator on display
        memory_label = Label(
            master=display_container,
            name='memory_label',
            anchor='s',
            bg=display_background,
            text='M',
            font=('Default', 8, 'bold')
        )
        memory_label.place(relwidth=0.08, relheight=0.5)
        # Operator indicator on display
        operator_label = Label(
            master=display_container,
            name='operator_label',
            anchor='n',
            bg=display_background,
            text=chr(247),
            font=('Default', 12, 'bold')
        )
        operator_label.place(rely=0.5, relwidth=0.08, relheight=0.5)
        # Display entry
        display_entry = Entry(
            master=display_container,
            name='display_entry',
            justify='right',
            relief='flat',
            foreground='#1E1E1E',
            borderwidth=4,
            font=self.font,
            bg=display_background,
            readonlybackground=display_background,
        )
        display_entry.place(relx=0.08, relwidth=0.92, relheight=1)
        display_entry.insert(index=0, string=self.calc.start_zero)
        display_entry.config(state='readonly')
        
        # Container for the buttons
        button_container = Frame(
            master=self.root,
            name='btn_container',
            background=background
        )
        button_container.place(
            relx=0.07, rely=0.38,
            relwidth=0.86, relheight=0.53
        )
        # Configure a 5x5 grid for the buttons
        for i in range(5):
            button_container.rowconfigure(
                index=i, weight=1, minsize=40, uniform='a'
            )
            button_container.columnconfigure(
                index=i, weight=1, minsize=40, uniform='a'
            )
            
        

        