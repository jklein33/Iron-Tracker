import streamlit as st
import pandas as pd
import snowflake.connector
import configparser

st.title('Welcome to the Iron Tracker')

st.header('Insert Workouts')

st.text('Enter Exercise details to database')
exerciseType = st.text_input('Exercise Type')
exerciseDesc = st.text_input('Exercise Description')
difficultyLevel = st.text_input('Difficulty Level')
muscleGroup = st.text_input('Muscle Group')
