from flask import Flask, render_template, jsonify

import numpy as np
from us_states import statesData
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
# Create a Session Object to Connect to DB
# ----------------------------------
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session

import json

app = Flask(__name__)

#################################################
# Database Setup
#################################################

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/statemigration/CA')
def api_pull():
    rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Relo = Base.classes.relocation

    session = Session(engine)

    data = session.query(Relo).filter(Relo.primary_state=='California').all()

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

@app.route('/api/statemigration/FL')
def api_pull():
    rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Relo = Base.classes.relocation

    session = Session(engine)

    data = session.query(Relo).filter(Relo.primary_state=='Florida').all()

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

@app.route('/api/statemigration/IN')
def api_pull():
    rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Relo = Base.classes.relocation

    session = Session(engine)

    data = session.query(Relo).filter(Relo.primary_state=='Indiana').all()

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

@app.route('/api/statemigration/NC')
def api_pull():
    rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Relo = Base.classes.relocation

    session = Session(engine)

    data = session.query(Relo).filter(Relo.primary_state=='North Carolina').all()

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

@app.route('/api/statemigration/TX')
def api_pull():
    rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Relo = Base.classes.relocation

    session = Session(engine)

    data = session.query(Relo).filter(Relo.primary_state=='Texas').all()

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


    # document = {}
    # document["primary_state"] = row.primary_state
    # document["secondary_state"] = row.secondary_state
    # document["inflow"] = row.inflow
    # document["outflow"] = row.outflow
    # data.append(document)

    # return render_template('index.html', header=header, inflow=inflow)

if __name__ == "__main__":
    app.run(debug=True)