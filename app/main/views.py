from . import main

@main.route('/')
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
