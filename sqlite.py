"""
References
----------
csvs-to-sqlite, https://github.com/simonw/csvs-to-sqlite
"""

import pandas as pd
import sqlite3

con = sqlite3.connect("kiva.db")
loans = pd.read_sql("SELECT * FROM loans", con)
loans
