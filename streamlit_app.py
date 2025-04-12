# streamlit_app.py

import streamlit as st
from PIL import Image
from material_info import material_data

# MOCK PREDICTION FUNCTION (you'll replace this later)
def fake_predict(image)
    # Just returns plastic for now
    return plastic

# HEADER
st.title(♻️ Smart Material Classifier)
st.write(Upload a photo of an object. The app will detect its material and tell you how to dispose of it.)

# IMAGE UPLOAD
uploaded_image = st.file_uploader(Upload an image, type=[jpg, jpeg, png])

if uploaded_image
    image = Image.open(uploaded_image)
    st.image(image, caption=Uploaded Image, use_column_width=True)

    with st.spinner(Analyzing...)
        predicted_material = fake_predict(image).lower()

    st.subheader(🔍 Material Detected)
    st.success(predicted_material.capitalize())

    info = material_data.get(predicted_material)

    if info
        st.subheader(♻️ Recyclability)
        st.write(Recyclable, Yes ✅ if info[recyclable] else No ❌)
        st.write(Bin, info[bin])
        st.write(Environmental Harm if Not Recycled)
        st.info(info[harm])
    else
        st.warning(Sorry, we don’t have information for that material yet.)
