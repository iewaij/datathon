"""
Query data from Oracle database.

Steps
-----
1. Follow instructions on [cx_Oracle](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html) and put `instantclient_19_8` in the datathon folder or put `instantclient_19_8`'s path in `lib_dir`.
2. Install `cx_Oracle` and `sqlalchemy` using pip or conda.
3. Run this scripts in your code editor or jupyter notebook. 

References
----------
Query Oracle databases with Python and SQLAlchemy, https://gist.github.com/DGrady/7fb5c2214f247dcff2cb5dd99e231483
"""

import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

# cosmetic options for matplotlib and seaborn
set_matplotlib_formats("svg")
rc = {
    "figure.figsize": (6.4, 4.8),
    "figure.dpi": 300,
    "axes.titlesize": "large",
    "axes.titleweight": "bold",
    "axes.titlepad": 12,
    "axes.titlelocation": "left",
}

sns.set_theme(context="notebook", style="darkgrid", color_codes=True, rc=rc)

# initialize client library, only need initialize once
cx_Oracle.init_oracle_client(lib_dir="instantclient_19_8")

# create connection string
oracle_connection_string = (
    "oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}"
)

# create connection engine
engine = create_engine(
    oracle_connection_string.format(
        username="MADS_021",
        password="MADS_021",
        hostname="svr-oracle-dbee.francecentral.cloudapp.azure.com",
        port="1521",
        database="dbee",
    )
)

# query data into pandas
data = pd.read_sql(
    """SELECT LOA_ID FROM MADS_KIVA.kiva_loans
    WHERE LOA_COUNTRY_CODE = 'BO'
    """,
    engine,
)

data.plot()
