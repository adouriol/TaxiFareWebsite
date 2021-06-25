import streamlit as st
import pandas as pd
import requests
from datetime import date
import webbrowser


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
today_date = date.today()
title_date= st.text_input('longitude pick up', today_date)
title_longitudep = st.text_input('longitude pick up')


title_latitudep = st.text_input('latitude pick up')


title_longitudd_drop = st.text_input('longitude drop off')


title_latitude_drop = st.text_input('latitude drop off')

option = st.slider('Select numbers of passagers', 1, 8,1)


if st.button('Calculate'):
    if title_longitudep == '' or title_latitude_drop =='' or title_latitudep == '' or title_longitudd_drop == '':
        st.error('Yo brother you missing something')
    else: 
        flaot_title_longitudep = float(title_longitudep)
        flaot_title_latitudep = float(title_latitudep)
        flaot_title_longitudd_drop = float(title_longitudd_drop)
        flaot_title_latitude_drop = float(title_latitude_drop)
        data = pd.DataFrame({
        'awesome cities' : ['pick up','drop off'],
        'lat' : [flaot_title_latitudep,flaot_title_latitude_drop],
        'lon' : [flaot_title_longitudep,flaot_title_latitude_drop]
        })
        st.map(data,zoom=7)
        webbrowser.open('https://www.uber.com/fr/fr/ride/?utm_campaign=CM2056849-search-google-brand_61_-99_FR-National_driver_web_acq_cpc_fr_Generic_BMM_%2Buber_kwd-38545560932_473517162666_114286613209_b_c&utm_source=AdWords_Brand')
        formatted_pickup_datetime = today_date.strftime("%Y-%m-%d %H:%M:%S")
        params = {
            "pickup_datetime" : str(formatted_pickup_datetime),
            "pickup_longitude" : flaot_title_longitudep,
            "pickup_latitude" : flaot_title_latitudep,
            "dropoff_longitude" : flaot_title_longitudd_drop,
            "dropoff_latitude" : flaot_title_latitude_drop,
            "passenger_count" : str(option)
        }
        url= 'https://taxifare.lewagon.ai/predict'
        reponse = requests.get(url,params=params).json()
        st.text('Price is '+ str(round(int(reponse['prediction']),2)))
        
        
        
    



