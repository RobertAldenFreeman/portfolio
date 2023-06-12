from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key
socketio = SocketIO(app)

# SQLite database setup
db_path = 'messages.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS messages (name TEXT, email TEXT, message TEXT)')

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        save_message(name, email, message)
        return redirect('/contact?success=true')
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/messages')
def messages():
    messages = fetch_messages()
    return render_template('messages.html', messages=messages)

def save_message(name, email, message):
    c.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    emit_message(name, email, message)  # Emit the new message to all connected clients

def fetch_messages():
    c.execute('SELECT * FROM messages')
    return c.fetchall()

@socketio.on('connect')
def handle_connect():
    messages = fetch_messages()
    emit('initial_messages', messages)  # Send the existing messages to the newly connected client

@socketio.on('new_message')
def handle_new_message(data):
    name = data['name']
    email = data['email']
    message = data['message']
    save_message(name, email, message)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)