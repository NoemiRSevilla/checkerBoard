from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard8x8():
    return render_template('checkerboard.html', row=int(8), column=int(8))

@app.route('/<row>')
def checkerboardcolumn(row):
    return render_template('checkerboard.html', row=int(row), column=int(8))

@app.route('/<row>/<column>/')
def checkerboardRowColumn(row, column):
    return render_template('checkerboard.html', row=int(row), column=int(column))

if __name__ == "__main__":
    app.run(debug=True)