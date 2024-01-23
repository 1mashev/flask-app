from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

database = [
    {'id': 1, 'name': 'John Doe', 'message': 'Привет, мир!', 'timestamp': datetime.now()},
    {'id': 2, 'name': 'Jane Smith', 'message': 'Привет от Jane!', 'timestamp': datetime.now()}
]

@app.route('/')
def home():
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', current_time=current_time, messages=database)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add_message', methods=['POST'])
def add_message():
    if request.method == 'POST':
        name = request.form['name']
        message_text = request.form['message']
        timestamp = datetime.now()

        new_message = {'id': len(database) + 1, 'name': name, 'message': message_text, 'timestamp': timestamp}
        database.append(new_message)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
