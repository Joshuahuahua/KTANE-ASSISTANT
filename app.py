from flask import Flask, render_template, request
from modules.vanilla.simple_wires import simple_wires

app = Flask(__name__)

# INDEX / HOMEPAGE

@app.route('/')
def index():
    return render_template('index.html')

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
        print(wire_list)
        for i, x in enumerate(wire_list):
            if x == '':
                del wire_list[i]
        wires(bomb_data, wire_list)
        print(wire_list)


        return render_template('wires.html', wire=simple_wires(bomb_data, wire_list))
    return render_template('wires.html')

if __name__ == '__main__':
    app.run(debug=True)