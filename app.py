from flask import Flask, render_template, request
from modules.vanilla.simple_wires import simple_wires
from modules.vanilla.button import button, button2

app = Flask(__name__)

bomb_data = {
    'bat_AA': 0,
    'bat_B': 0,
    'bat_total': 0,
    'ind_LIT': ['FRK'],
    'ind_UNLIT': [],
    'serial': 'serial',
    'serial_odd': 'serial_odd',
    'serial_vowel': 'serial_vowel',
    'port_parallel': 'port_parallel',
}

# INDEX / HOMEPAGE

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vanilla')
def vanilla():
    return render_template('vanilla.html')

# SIMPLE WIRES

@app.route('/wires', methods=['GET', 'POST'])
def wires():
    if request.method == 'POST':
        
        bomb_data = {'serial_odd': True}
        
        wire_list = []
        wire_list.append(request.form['wire1'])
        wire_list.append(request.form['wire2'])
        wire_list.append(request.form['wire3'])
        wire_list.append(request.form['wire4'])
        wire_list.append(request.form['wire5'])
        wire_list.append(request.form['wire6'])


        return render_template('wires.html', wire=simple_wires(bomb_data, wire_list))
    return render_template('wires.html')

if __name__ == '__main__':
    app.run(debug=True)