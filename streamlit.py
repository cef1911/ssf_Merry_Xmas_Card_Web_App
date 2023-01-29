import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
from PIL import Image




image = Image.open("sunrise.jpeg")

st.image(image, caption='Amanda Franklin, Happy Heavenly Birthday')

st.write("Tribute To Amanda Franklin")


imagetwo = Image.open("birthday.jpeg")

st.image(imagetwo, caption='Amanda Franklin')


imagethree = Image.open("memories.png")

st.image(imagethree, caption='Amanda Franklin')


st.write("Love the Franklins, Chris")



