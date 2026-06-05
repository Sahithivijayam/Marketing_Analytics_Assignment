# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

# load_dotenv()

# engine = create_engine(os.getenv("DB_URL"))

# def get_data():
#     import pandas as pd
#     return pd.read_sql("SELECT * FROM unified_ads", engine)

import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(st.secrets["DB_URL"])

def get_data():
    return pd.read_sql("SELECT * FROM unified_ads", engine)