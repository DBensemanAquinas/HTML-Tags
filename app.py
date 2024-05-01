from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template("index.html")


@app.route('/html')
def render_html():
    return render_template("html.html")


@app.route('/css')
def render_css():
    print("css")
    definitions = [["color", "The color of the text"],
                   ["border", "The thickness, type and colour of a border"],
                   ["padding", "The distance between the object and the border"]]
    return render_template("css.html", definitions=definitions)

if __name__ == '__main__':
    app.run()
