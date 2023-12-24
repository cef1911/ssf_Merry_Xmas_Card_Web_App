import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
from PIL import Image



st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:75px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Merry Christmas To Stacey Franklin!!</p>', unsafe_allow_html=True)


image = Image.open("twistedpizzasf.PNG")

st.image(image, caption='Stacey Franklin, Happy Birthday Year')

st.write("Tribute To Stacey Franklin")


# imagetwo = Image.open("birthday.jpeg")

# st.image(imagetwo, caption='Amanda Franklin')


imagethree = Image.open("memories.png")

st.image(imagethree, caption='Stacey Franklin')


st.write("Love You Stacey, Chris")

st.balloons()

st.snow()

