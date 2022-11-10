#Import out library and packages
from flask import Flask
import random

#create our web application
app = Flask(__name__)

#Create our routes
@app.route('/')
def home():
    return "Hello World"

#Start our application
if __name__=="__main__":
    app.run(
        port= random.randint(2000,8000)
    )