import streamlit as st
import pandas as pd
import psycopg2
import getpass

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Titanic Data Dashboard",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Titanic Passenger Analysis Dashboard")

st.write("Analysis of Titanic passenger records using PostgreSQL and Python.")

# --------------------------------
# DATABASE CONNECTION
# --------------------------------

@st.cache_data
def load_data():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="titanic_db",
        user="postgres",
        password=st.secrets["db_password"]
    )

    query = """
        SELECT *
        FROM titanic_project.passengers
        ORDER BY passengerid;
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


# --------------------------------
# LOAD DATA
# --------------------------------

try:
    df = load_data()

    st.success("PostgreSQL Connected Successfully!")

except Exception as error:
    st.error(f"Database Error: {error}")
    st.stop()


# --------------------------------
# KPI METRICS
# --------------------------------

total_passengers = len(df)

survivors = int(df["survived"].sum())

deaths = total_passengers - survivors

survival_rate = survivors / total_passengers * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Passengers", total_passengers)

col2.metric("Survivors", survivors)

col3.metric("Deaths", deaths)

col4.metric("Survival Rate", f"{survival_rate:.2f}%")


st.divider()


# --------------------------------
# GENDER ANALYSIS
# --------------------------------

st.subheader("Gender Analysis")

gender_count = df["sex"].value_counts()

st.bar_chart(gender_count)


# --------------------------------
# PASSENGER CLASS ANALYSIS
# --------------------------------

st.subheader("Passenger Class Analysis")

class_count = df["pclass"].value_counts().sort_index()

st.bar_chart(class_count)


# --------------------------------
# SURVIVAL ANALYSIS
# --------------------------------

st.subheader("Survival Analysis")

survival_count = df["survived"].value_counts()

st.bar_chart(survival_count)


# --------------------------------
# AGE ANALYSIS
# --------------------------------

st.subheader("Age Distribution")

age_data = df["age"].dropna()

st.bar_chart(age_data.value_counts().sort_index())


# --------------------------------
# PASSENGER DATA TABLE
# --------------------------------

st.subheader("Titanic Passenger Records")

st.dataframe(df, use_container_width=True)

st.success("Dashboard Loaded Successfully!")