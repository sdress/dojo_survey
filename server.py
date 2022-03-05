from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'shhh'

@app.route('/')
def make_form():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def save_info():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)