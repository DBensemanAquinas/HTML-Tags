from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

DATABASE = "html_tags.db"


def create_connection(db_file):
    """ Create a connection to the sql database
    Parameters: 
    db_file - The name of the file
    Returns: A connection to the database
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)
    return None


def get_tag_types():
    query = "SELECT DISTINCT type FROM tag"
    conn = create_connection(DATABASE)
    cur = conn.cursor()
    cur.execute(query)
    tag_list = cur.fetchall()
    conn.close()
    print(tag_list)
    tags = []
    for tag in tag_list:
        tags.append(tag[0])
    return tags

@app.route('/')
def render_home():
    return render_template("index.html", tags=get_tag_types())


@app.route('/tag/<tag_type>')
def render_html(tag_type):
    query = "SELECT name, description from tag WHERE type = ?"
    conn = create_connection(DATABASE)
    cur = conn.cursor()
    cur.execute(query, (tag_type, ))
    definitions = cur.fetchall()
    conn.close()

    return render_template("tags.html", definitions=definitions, tag_type=tag_type.upper(), tags=get_tag_types())


if __name__ == '__main__':
    app.run()
