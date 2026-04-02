
import streamlit as st
import random
# Background CSS
st.markdown("""
<style>
/* Page background gradient */
.stApp {
    background-image: url("https://img.freepik.com/free-psd/3d-rendering-questions-background_23-2151455632.jpg?semt=ais_hybrid&w=740&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Title and subtitle */
h1 {
    color: black !important;
    text-align: center;
    font-size: 40px;
}
p {
    color: black !important;
    text-align: center;
    font-size: 20px;
}

/* Input box styling */
div.stNumberInput > div > input {
    background-color: white !important;
    color: black !important;
    border: 2px solid #000000;
    border-radius: 5px;
    padding: 5px;
}

/* Button styling */
div.stButton > button {
    color: white !important;
    background: linear-gradient(to right, #4CAF50, #2E7D32) !important;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Store jackpot in session state
if "jackpot" not in st.session_state:
    st.session_state.jackpot = random.randint(1, 100)
    st.session_state.attempts = 0
    
st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 100")

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.jackpot:
        st.warning("Guess Higher ⬆️")
    elif guess > st.session_state.jackpot:
        st.warning("Guess Lower ⬇️")
    else:
        st.success("🎉 Right answer! You guessed it right!")
        st.write("Attempts:", st.session_state.attempts)

        # restart game
        st.session_state.jackpot = random.randint(1, 100)
        st.session_state.attempts = 0
