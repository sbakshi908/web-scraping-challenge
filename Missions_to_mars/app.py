# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html") #pass whatever variables in the render template to the html page


if __name__ == "__main__":
    app.run(debug=True)