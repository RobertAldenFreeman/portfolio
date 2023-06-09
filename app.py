
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)