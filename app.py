from flask import Flask, render_template
app = Flask(__name__)

@app.route("/polina")
def polina():
    return render_template('polina/index.html')


@app.route("/dasha")
def dasha():
    return render_template('dasha/index.html')


@app.route("/dasha/success")
def success():
    return render_template('dasha/index1.html')


@app.route("/dasha/valentine")
def valentine():
    return render_template('dasha/val.html')


@app.route("/nikita/birthday")
def birthday():
    return render_template('nikita/birthday.html')

# app.run(host='0.0.0.0', port=80)
app.run(debug=True)

