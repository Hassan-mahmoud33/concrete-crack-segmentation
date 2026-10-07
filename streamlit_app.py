import streamlit as st
from ultralytics import YOLO
from PIL import Image


model = YOLO('best.pt')

st.title('Crack-Segmentation')

uploaded = st.file_uploader('Upload An Image', type=['png', 'jpg','jpeg'])


if uploaded is not None :

    img = Image.open( uploaded )
    st.image( img , caption='Original' )

    if st.button('Predict') :

        results = model.predict( img , imgsz= 640 , conf=0.40 )
        annotated = results[0].plot()

        st.write('Results')
        st.image( annotated )

