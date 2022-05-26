import streamlit as st
import pyautogui
try:
    st.success("welcome to streamlit community!")
except:
   pyautogui.hotkey("ctrl","F5")
