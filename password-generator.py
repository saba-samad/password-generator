import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
        
    if use_special_chars:
        characters += string.punctuation
        
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select the length of the password", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include digits")
use_special_chars = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.success(f"Generated Password: {password}")

st.write("----------------------------------------------------------")

st.write("Build with ❤️ by [Saba Samad](https://github.com/saba-samad)")
        
        
