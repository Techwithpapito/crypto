from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('diensten.html')

@app.route('/about')
def about():
    return render_template('over_ons.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/why_crypto')
def why_crypto():
    return render_template('waarom_crypto.html')


if __name__ == '__main__':
    app.run(debug=True)
    