import streamlit as st
from PIL import Image
import os
import numpy as np
import pandas as pd
import re
from style_clip import image_generator, 

# from dataset_select import dataset_select
# from generator import image_generator
# from request_image import request_image
# import style-clip



# Paths - NOTE: CHANGE TO GCP
########################################################################################################################## 
original_path = '/Users/lucaskawasaki/Desktop/Project/replicate/original/'
output_path = '/Users/lucaskawasaki/Desktop/Project/replicate/generated/'
########################################################################################################################## 

# Images paths
########################################################################################################################## 
def catch_images_name(output_path):
    images=sorted(os.listdir(output_path))
    images_name = [re.sub('\.jpg$', '', image) for image in images if image.endswith(".jpg")]
    print(images_name)
    return images_name
########################################################################################################################## 

# Page and behavior setup
########################################################################################################################## 
st.set_page_config(layout="wide")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False
def click_button():
    st.session_state.clicked = True
########################################################################################################################## 







# Color configuration
########################################################################################################################## 
########################################################################################################################## 

# Slider Color Change
##########################################################################################################################      
ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 0 / 0%); } </style>''', unsafe_allow_html = True)


Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(255, 0, 0); box-shadow: rgb(255 0 0 / 100%) 0px 0px 0px 0.1rem;} </style>''', unsafe_allow_html = True)

col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                                rgb(1, 183, 158)0%, 
                                rgba(151, 166, 195, 0.25)0%, 
                                rgba(151, 166, 195, 0.25) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True) 
##########################################################################################################################     









def main():
    # Sidebar part 1
    ########################################################################################################################## 
    with st.sidebar:
        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
        
        text_input1 = st.text_input("Describe the features of a person you are looking for:",key='placeholder')
        upload_image = st.button('Upload image', on_click=click_button)
    
        text_input2 = st.text_input("Enter the feature you want to change:") #disabled=st.session_state.disabled)
        generate_image = st.button('Generate images', on_click=click_button)
    ########################################################################################################################## 

    # Input and Output text - Page
    ########################################################################################################################## 
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
            st.markdown('<p class="big-font">Input image</p>', unsafe_allow_html=True)
        with col2:
            st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)
            st.markdown('<p class="big-font">Output image</p>', unsafe_allow_html=True)
    ##########################################################################################################################   
    
    # To create a image
    ########################################################################################################################## 
    with st.container(): 
        # Create two columns with equal width
        col1, col2 = st.columns(2)
    
        if text_input1 and st.session_state.clicked:
            # Call image from dataset and treat on style_clip_original
            
            # original_image_path = dataset_select(text_input1) # path
            # original_image = image_generator(image=original_image_path, target='a face', manipulation=0.0)
            # original_image = request_image(link=original_image, folder_path=original_path, manipulation=0.0)
    
            # Original image
            #############################################################    
            with col1:
                #image1 = Image.open(original_image) # return from previous part
                image1 = Image.open(f'{output_path}3.0.jpg') # return from previous part
                disabled=st.session_state
                st.image(image1, use_column_width=True)
 

        if text_input1 and text_input2 and st.session_state.clicked:  
            # Call style_clip and web_load_images
            # style-clip(image=original_image, target=text_input2)
            
        
            # Sidebar part 2
            #############################################################  
            with st.sidebar:
                color = st.select_slider(
                    'Select the level of change',
                    options=catch_images_name(output_path),
                    value=('4.6')
                )
            # Generated image
            #############################################################  
            with col2:
                image2 = Image.open(f'{output_path}{color}.jpg')
                st.image(image2, use_column_width=True) 
            
    ##########################################################################################################################   
    
    # Download, Accept and Reset image button
    # There is more columns to make a side-by-side button
    ##########################################################################################################################   
    if text_input1 and text_input2 and st.session_state.clicked:  
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([1,1,1,1,1,1,0.78,1,1,1])

        with col1: st.write('')
        with col2: st.write('')
        with col3: st.write('')
        with col4: st.write('')
        with col5: st.write('')
        with col6:
            st.button('Download')
            # Download image
        with col7:
            st.button('Accept')
            # Same this as 'original image' and make change in this image
        with col8:
            st.button('Reset')
            # Return to original image
        with col9: st.write('')
        with col10: st.write('')
    ##########################################################################################################################   
    

if __name__ == "__main__":
    main()