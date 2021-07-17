from flask import Flask, render_template

import numpy as np

from sqlalchemy import create_engine
# Create a Session Object to Connect to DB
# ----------------------------------
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session

app = Flask(__name__)

#################################################
# Database Setup
#################################################
connection_string = "postgres:postgres@localhost:5432/migration_db"
engine = create_engine(f'postgresql://{connection_string}')
conn = engine.connect()
session = Session(bind=engine)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/california')
def CA():
    data = list(db.latest_data.find())

    header = "California"

    return render_template('state.html', header=header, inflow=inflow)

@app.route('/florida')
def FL():

    header = "Florida"

    return render_template('state.html', header=header, inflow=inflow)

@app.route('/indiana')
def IN():

    header = "Indiana"

    return render_template('state.html', header=header, inflow=inflow)

@app.route('/north_carolina')
def NC():

    header = "North Carolina"

    return render_template('state.html', header=header, inflow=inflow)

@app.route('/texas')
def TX():

    header = "Texas"

    return render_template('state.html', header=header, inflow=inflow)

if __name__ == "__main__":
    app.run(debug=True)