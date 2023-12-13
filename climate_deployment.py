import joblib
import datetime
from statsmodels.tsa.arima.model import ARIMA
import streamlit as st

humidity_model = joblib.load('humidity_model.joblib')
temperature_model = joblib.load('temperature_model.joblib')
def make_prediction(model, model_type):
    if st.button(f'Predict {model_type}', key=model_type):
        last_training_time = datetime.datetime(2023, 11, 22, 23, 00,00)
        current_time = datetime.datetime.now()
        hour_diff = int((current_time - last_training_time).total_seconds() /3600)

        forecast = model.get_forecast(steps=hour_diff+1)
        prediction = forecast.predicted_mean.tail(2)
        st.success(f'Current {model_type}: {int(prediction[0])}')
        st.success(f'Next hour {model_type}: {int(prediction[1])}')

st.title('Weather Forcasting App')
make_prediction(humidity_model, 'Humidity')
make_prediction(temperature_model, 'Temperature')

