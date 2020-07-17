# Import MatPlotLib
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import Numpy and Pandas
import numpy as np
import pandas as pd

# Import DateTime
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

###########################################################
# Database Setup
###########################################################
engine = create_engine("sqlite:///Resources/Colins_SQL.sqlite")
connection = engine.connect()

# Declare bases and map class
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# view all of the classes
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

###########################################################
# Flask setup
###########################################################
app = Flask(__name__)

###########################################################
# Flask Route
###########################################################
# Home page
# List all routes that are available
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Convert the query results to a dictionary using date as the key and prcp as the value
# Return the JSON representation of your dictionary
@app.route("/api/v1.0/data")
def data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query results to a dictionary using date as the key and prcp as the value
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date).\
        order_by(Measurement.date).all()

    session.close()

    # List date and precipitation
    all_date = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["precipitation"] = prcp
        all_date.append(measurement_dict)
    
    # Jsonify the data
    return jsonify(all_date)

if __name__ == "__main__":
    app.run(debug=True)