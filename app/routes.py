
from flask import render_template, request
from app import app
from app import train
import os

@app.route('/', methods=['POST', 'GET'])
def get_pressure():
    if request.method == 'GET':
        return render_template('website.html')
    elif request.method == 'POST' :
        age = request.values.get("age") 
        weight = request.values.get("weight") 
        print(age)
        print(weight)

        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))
        
        pressure=train.load(age,weight)
        print(pressure) 


        return str(pressure)
    # return render_template('website.html')


    
