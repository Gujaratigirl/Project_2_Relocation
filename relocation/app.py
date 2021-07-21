from flask import (Flask, render_template, jsonify)

from . import us_states
import os

# from sqlalchemy import create_engine, func
# from sqlalchemy.ext.automap import automap_base
# # Create a Session Object to Connect to DB
# # ----------------------------------
# # Session is a temporary binding to our DB
# from sqlalchemy.orm import Session

app = Flask(__name__)

#################################################
# Database Setup
#################################################
# rds_connection_string = os.environ.get('DATABASE_URL', '') or "postgresql://postgres:postgres@localhost:5432/migration_db"
# engine = create_engine(f'{rds_connection_string}')

# Base = automap_base()

# Base.prepare(engine, reflect=True)

# Relo = Base.classes.relocation

# session = Session(engine)

# statesData = us_states.statesData


@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/api/test/<state_name>')
# def api_pull2(state_name):
#     state_name = state_name.upper()
#     # rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
#     # engine = create_engine(f'postgresql://{rds_connection_string}')
#     # Base = automap_base()
#     # Base.prepare(engine, reflect=True)
    
#     # session = Session(engine)
#     data = session.query(Relo).filter(func.upper(Relo.primary_state)==state_name).all()
#     relo_list = []
#     for row in data:
#         dict = {}
#         dict["secondary_state"] = row.secondary_state
#         dict["inflow"] = row.inflow
#         dict["outflow"] = row.outflow
#         relo_list.append(dict)
#     state_features = statesData["features"]
#     for doc in state_features:
#         for item in relo_list:
#             if item["secondary_state"] == doc["properties"]["name"]:
#                 doc["properties"]["inflow"] = item["inflow"]
#                 doc["properties"]["outflow"] = item["outflow"]
#     statesData["features"] = state_features
#     session.close()

#     return(jsonify(statesData))


# @app.route('/api/statemigration/CA')
# def api_pull():
#     rds_connection_string = "postgres:postgres@localhost:5432/migration_db"
#     engine = create_engine(f'postgresql://{rds_connection_string}')
#     Base = automap_base()
#     Base.prepare(engine, reflect=True)
#     Relo = Base.classes.relocation
#     session = Session(engine)
#     data = session.query(Relo).filter(Relo.primary_state=='California').all()
#     relo_list = []
#     for row in data:
#         dict = {}
#         dict["secondary_state"] = row.secondary_state
#         dict["inflow"] = row.inflow
#         dict["outflow"] = row.outflow
#         relo_list.append(dict)
#     state_features = statesData["features"]
#     for doc in state_features:
#         for item in relo_list:
#             if item["secondary_state"] == doc["properties"]["name"]:
#                 doc["properties"]["inflow"] = item["inflow"]
#                 doc["properties"]["outflow"] = item["outflow"]
#     statesData["features"] = state_features
#     session.close()
#     return(jsonify(statesData))

# @app.route('/api/statemigration')
# def api_pull():
    

#     data = session.query(Relo).all()

#     relo_list = []

#     for row in data:
#         dict = {}
#         dict["primary_state"] = row.primary_state
#         dict["secondary_state"] = row.secondary_state
#         dict["inflow"] = row.inflow
#         dict["outflow"] = row.outflow
#         relo_list.append(dict)
        
#     state_features = statesData["features"]

#     for doc in state_features:
#         feature_list = []
#         for item in relo_list:
#             if item["secondary_state"] == doc["properties"]["name"]:
#                 dict = {}
#                 dict["primary_state"] = item["primary_state"]
#                 dict["inflow"] = item["inflow"]
#                 dict["outflow"] = item["outflow"]
#                 feature_list.append(dict)
#         doc["properties"]["flows"] = feature_list
#     statesData["features"] = state_features

#     session.close()

#     return(jsonify(statesData))


    # document = {}
    # document["primary_state"] = row.primary_state
    # document["secondary_state"] = row.secondary_state
    # document["inflow"] = row.inflow
    # document["outflow"] = row.outflow
    # data.append(document)

    # return render_template('index.html', header=header, inflow=inflow)

if __name__ == "__main__":
    app.run(debug=False)