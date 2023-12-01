import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
st.subheader("Hi, I am Reign Heinz Jeisler Egnalig")
st.title("A Students from SNSU")
st.write("I am passionate to learn from this amazing school")

# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
        """
        On my journey of being a student i will show you the beautiful place to learn from this school for people that want to learn from this university:
        REQUIREMENTS TO ENROLL:
        - 2x2 pic
        - birth certificate
        - good moral and report card

        If you have any further question just message me in my Fb acc: Reign Heinz Jeisler Egnalig
        """
    
    
        
  
    
