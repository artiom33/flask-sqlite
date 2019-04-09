from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import sqlite3
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists(app.config["DATABASE_NAME"]):
    conn = sqlite3.connect(app.config["DATABASE_NAME"])
    # cur = conn.cursor()
    # cur.execute("CREATE TABLE iris (sepal_length REAL, sepal_width REAL,"
    #             "petal_length REAL, petal_width REAL, species TEXT);")
    # conn.commit()
    iris_df = pd.read_csv(app.config["DATA_URL"])
    iris_df.to_sql('iris', conn, dtype={'sepal_length': 'REAL',
                                        'sepal_width': 'REAL',
                                        'petal_length': 'REAL',
                                        'petal_width': 'REAL',
                                        'species': 'VARCHAR(255)'})

db = SQLAlchemy(app)

from app import routes  # noqa
