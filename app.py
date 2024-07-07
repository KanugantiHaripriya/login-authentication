from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'Haripriya_kanuganti' and password == 'haripriya09':
        return render_template('dashboard.html')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
