import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

gender_df = pd.read_csv('gender_submission.csv')
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

st.title("Titanic Data")
sidebar = st.sidebar

selections = sidebar.multiselect("Select Datas", ["Train data","Test data", "Full data", "Graphs"])
for val in selections:
    if val == "Train data":
        st.write(train_df)
    if val == "Test data":
        st.write(test_df)

new_test = sidebar.multiselect("Test", ["Train data","Test data", "Full data", "Graphs"])
for val in new_test:
    st.write(train_df)
fig = sns.countplot(train_df.Survived)
st.pyplot(fig)

