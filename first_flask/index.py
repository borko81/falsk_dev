from flask import Flask, render_template
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('base.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
