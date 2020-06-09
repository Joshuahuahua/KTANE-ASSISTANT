import tkinter
import tkinter.messagebox as msgbox
import tkinter.font as tkFont
from PIL import Image, ImageTk

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
        self.main['bg']='#FFFFFF'

        self.options = tkinter.Frame(self.main, bg='#FFFFFF')
        self.options.pack()

        # Images
        black_temp = Image.open('images/wires/black.png')
        black_temp = black_temp.resize((130,32), Image.ANTIALIAS)
        self.black = ImageTk.PhotoImage(black_temp)

        white_temp = Image.open('images/wires/white.png')
        white_temp = white_temp.resize((130,32), Image.ANTIALIAS)
        self.white = ImageTk.PhotoImage(white_temp)

        blue_temp = Image.open('images/wires/blue.png')
        blue_temp = blue_temp.resize((130,32), Image.ANTIALIAS)
        self.blue = ImageTk.PhotoImage(blue_temp)

        red_temp = Image.open('images/wires/red.png')
        red_temp = red_temp.resize((130,32), Image.ANTIALIAS)
        self.red = ImageTk.PhotoImage(red_temp)

        yellow_temp = Image.open('images/wires/yellow.png')
        yellow_temp = yellow_temp.resize((130,32), Image.ANTIALIAS)
        self.yellow = ImageTk.PhotoImage(yellow_temp)

        clear_temp = Image.open('images/wires/clear.png')
        clear_temp = clear_temp.resize((130,32), Image.ANTIALIAS)
        self.clear = ImageTk.PhotoImage(clear_temp)

        # Six rows, one for each wire

        self.one = tkinter.Frame(self.options, bg='#FFFFFF')
        self.one.pack()

        self.two = tkinter.Frame(self.options, bg='#FFFFFF')
        self.two.pack()

        self.three = tkinter.Frame(self.options, bg='#FFFFFF')
        self.three.pack()

        self.four = tkinter.Frame(self.options, bg='#FFFFFF')
        self.four.pack()

        self.five = tkinter.Frame(self.options, bg='#FFFFFF')
        self.five.pack()

        self.six = tkinter.Frame(self.options, bg='#FFFFFF')
        self.six.pack()

        # Wires
        self.wire_one = tkinter.Label(self.one, bg='#ffffff', image=self.clear)
        self.wire_one.pack(side='left')

        self.wire_two = tkinter.Label(self.two, bg='#ffffff', image=self.clear)
        self.wire_two.pack(side='left')

        self.wire_three = tkinter.Label(self.three, bg='#ffffff', image=self.clear)
        self.wire_three.pack(side='left')

        self.wire_four = tkinter.Label(self.four, bg='#ffffff', image=self.clear)
        self.wire_four.pack(side='left')

        self.wire_five = tkinter.Label(self.five, bg='#ffffff', image=self.clear)
        self.wire_five.pack(side='left')

        self.wire_six = tkinter.Label(self.six, bg='#ffffff', image=self.clear)
        self.wire_six.pack(side='left')

        # Buttons

        self.button_one = tkinter.Frame(self.one)
        self.button_one.pack(side='right')

        self.button_two = tkinter.Frame(self.two)
        self.button_two.pack(side='right')

        self.button_three = tkinter.Frame(self.three)
        self.button_three.pack(side='right')

        self.button_four = tkinter.Frame(self.four)
        self.button_four.pack(side='right')

        self.button_five = tkinter.Frame(self.five)
        self.button_five.pack(side='right')

        self.button_six = tkinter.Frame(self.six)
        self.button_six.pack(side='right')


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

        self.red_one = tkinter.Button(frame, text='   ', bg='#ff3030', command=lambda: wire.configure(image=self.red))
        self.white_one = tkinter.Button(frame, text='   ', bg='#ffffff', command=lambda: wire.configure(image=self.white))
        self.black_one = tkinter.Button(frame, text='   ', bg='#303030', command=lambda: wire.configure(image=self.black))
        self.blue_one = tkinter.Button(frame, text='   ', bg='#1482ff', command=lambda: wire.configure(image=self.blue))
        self.yellow_one = tkinter.Button(frame, text='   ', bg='#fffb80', command=lambda: wire.configure(image=self.yellow))

        self.clear_one = tkinter.Button(frame, text=' X ', bg='#dedede', command=lambda: wire.configure(image=self.clear))
        
        self.red_one.pack(side='left')
        self.blue_one.pack(side='left')
        self.yellow_one.pack(side='left')
        self.white_one.pack(side='left')
        self.black_one.pack(side='left')

        self.clear_one.pack(side='left')
    
    def save_list(self):
        self.wire_list = [self.wire_one['image'], self.wire_two['image'], self.wire_three['image'], self.wire_four['image'], self.wire_five['image'], self.wire_six['image']]
        self.colour_chart = [
        {'code': 'pyimage4', 'word': 'red'},
        {'code': 'pyimage2', 'word': 'white'},
        {'code': 'pyimage1', 'word': 'black'},
        {'code': 'pyimage3', 'word': 'blue'},
        {'code': 'pyimage5', 'word': 'yellow'}
        ]

        converted_wire_list = []
        
        for wire in self.wire_list:
            for colour in self.colour_chart:
                if wire != '#dedede':
                    if wire == colour['code']:
                        converted_wire_list.append(colour['word'])
        print(self.wire_list)
        print(converted_wire_list)
        return converted_wire_list

gui = ProgramGUI()