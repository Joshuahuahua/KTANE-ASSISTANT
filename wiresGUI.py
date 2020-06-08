import tkinter
import tkinter.messagebox as msgbox
import tkinter.font as tkFont

from modules.wires import wires
from modules.button import button

class ProgramGUI:

    
    def __init__(self):
        
        ############################# INIT #############################
        
        self.bomb_data = {
            'bat_AA': 0,
            'bat_B': 0,
            'bat_total': 0,
            'ind_LIT': [],
            'ind_UNLIT': [],
            'serial': '',
            'serial_odd': False,
            'serial_vowel': False,
            'port_DVI': False,
            'port_parallel': False,
            'port_ps2': False,
            'port_rj45': False,
            'port_rca': False,
        } 

        #myFont = tkFont.Font(family = 'Helvetica', size = 16, slant = 'roman', weight = 'normal')
        
        self.main = tkinter.Tk()

        self.main.title('KTANE Assistant')
        self.main.configure(bg='#FFFFFF')

        self.options = tkinter.Frame(self.main)
        self.options.pack()

        self.wires = tkinter.Frame(self.options)
        self.wires.pack(side='left')

        self.buttons = tkinter.Frame(self.options)
        self.buttons.pack(side='right')

        # Wires

        self.wire_one = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_one.pack()

        self.wire_two = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_two.pack()

        self.wire_three = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_three.pack()

        self.wire_four = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_four.pack()

        self.wire_five = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_five.pack()

        self.wire_six = tkinter.Label(self.wires, text="                ", bg='#dedede')
        self.wire_six.pack()

        # Buttons

        self.button_one = tkinter.Frame(self.buttons)
        self.button_one.pack()

        self.button_two = tkinter.Frame(self.buttons)
        self.button_two.pack()

        self.button_three = tkinter.Frame(self.buttons)
        self.button_three.pack()

        self.button_four = tkinter.Frame(self.buttons)
        self.button_four.pack()

        self.button_five = tkinter.Frame(self.buttons)
        self.button_five.pack()

        self.button_six = tkinter.Frame(self.buttons)
        self.button_six.pack()

        self.color_changer(self.button_one, self.wire_one)
        self.color_changer(self.button_two, self.wire_two)
        self.color_changer(self.button_three, self.wire_three)
        self.color_changer(self.button_four, self.wire_four)
        self.color_changer(self.button_five, self.wire_five)
        self.color_changer(self.button_six, self.wire_six)
        
        self.confirm_frame = tkinter.Frame(self.main)
        self.confirm_frame.pack()
        self.confirm = tkinter.Button(self.confirm_frame, text='Confirm', command=lambda: tkinter.messagebox.showinfo('Cut the following wire', wires(self.bomb_data, self.save_list())))
        self.confirm.pack()


        tkinter.mainloop()


    def color_changer(self, frame, wire):

        self.red_one = tkinter.Button(frame, text='   ', bg='#ff3030', command=lambda: wire.configure(bg='#ff3030'))
        self.white_one = tkinter.Button(frame, text='   ', bg='#ffffff', command=lambda: wire.configure(bg='#ffffff'))
        self.black_one = tkinter.Button(frame, text='   ', bg='#303030', command=lambda: wire.configure(bg='#303030'))
        self.blue_one = tkinter.Button(frame, text='   ', bg='#1482ff', command=lambda: wire.configure(bg='#1482ff'))
        self.yellow_one = tkinter.Button(frame, text='   ', bg='#fffb80', command=lambda: wire.configure(bg='#fffb80'))

        self.clear_one = tkinter.Button(frame, text=' X ', bg='#dedede', command=lambda: wire.configure(bg='#dedede'))
        
        self.red_one.pack(side='left')
        self.blue_one.pack(side='left')
        self.yellow_one.pack(side='left')
        self.white_one.pack(side='left')
        self.black_one.pack(side='left')

        self.clear_one.pack(side='left')
    
    def save_list(self):
        self.wire_list = [self.wire_one['bg'], self.wire_two['bg'], self.wire_three['bg'], self.wire_four['bg'], self.wire_five['bg'], self.wire_six['bg']]
        
        self.colour_chart = [
        {'hex': '#ff3030', 'word': 'red'},
        {'hex': '#ffffff', 'word': 'white'},
        {'hex': '#303030', 'word': 'black'},
        {'hex': '#1482ff', 'word': 'blue'},
        {'hex': '#fffb80', 'word': 'yellow'}
        ]

        converted_wire_list = []
        
        for i, wire in enumerate(self.wire_list):
            for colour in self.colour_chart:
                if wire != '#dedede':
                    if wire == colour['hex']:
                        converted_wire_list.append(colour['word'])
        return converted_wire_list

gui = ProgramGUI()