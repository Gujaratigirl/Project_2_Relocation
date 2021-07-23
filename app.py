from flask import Flask, render_template, jsonify

import numpy as np
from us_states import statesData
import pandas as pd

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
# Create a Session Object to Connect to DB
# ----------------------------------
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session



app = Flask(__name__)

#################################################
# Database Setup
#################################################

rds_connection_string = "postgres:Hema@localhost:5432/migration_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

#print(Base.classes.keys())
Base = automap_base()
Base.prepare(engine, reflect=True)
Relo = Base.classes.relocation

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/test/<state_name>')
def api_pull2(state_name):
    state_name = state_name.upper()
    
    session = Session(engine)
    data = session.query(Relo).filter(func.upper(Relo.primary_state)==state_name).all()
    relo_list = []
    for row in data:
        dict = {}
        dict["secondary_state"] = row.secondary_state
        dict["inflow"] = row.inflow
        dict["outflow"] = row.outflow
        relo_list.append(dict)
    state_features = statesData["features"]
    for doc in state_features:
        for item in relo_list:
            if item["secondary_state"] == doc["properties"]["name"]:
                doc["properties"]["inflow"] = item["inflow"]
                doc["properties"]["outflow"] = item["outflow"]
    statesData["features"] = state_features
    session.close()
    return(jsonify(statesData))


if __name__ == "__main__":
    app.run(debug=True)