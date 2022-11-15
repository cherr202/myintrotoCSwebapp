#Import out library and packages
from flask import Flask, render_template

#create our web application
app = Flask(__name__)

#Create our routes
@app.route('/')
def home():
    return render_template("index.html")

#Start our application
if __name__=="__main__":
    app.run(debug=True, port=3050)