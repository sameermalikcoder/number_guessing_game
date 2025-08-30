import streamlit as st
import random

st.set_page_config(page_title='Number Guessing Game', layout='centered')

st.title('Number Guessing Game')
st.text('I have a number in my mind between 1 to 100.')

# Initialize gaem state 
if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1,100)
    st.session_state.attempts  = 10
    st.session_state.count = 0
    st.session_state.score = 0
    st.session_state.game_over = False

st.write(f"Attemps left: {st.session_state.attempts  - st.session_state.count}")

#Input
guess = st.text_input("Enter a number between 1 - 100", "")

# Dynamic Buttons
btn_label = 'Play' if not st.session_state.game_over else ('Play again')

if st.button(btn_label):
    if st.session_state.game_over:
        # Reset Game
        st.session_state.secret = random.randint(1,100)
        st.session_state.attempts  = 10
        st.session_state.count = 0
        st.session_state.score = 0
        st.session_state.game_over = False
    else:
        # Progress Game
        if guess.isdigit():
            guess = int(guess)
            st.session_state.count += 1
            diff = abs(st.session_state.secret - guess)
    
            if diff == 0:
                st.success("😎 Perfect! Your Guess is right.")
                st.write(f"You took {st.session_state.count} attempts to guess the number.")
                st.write(f"Your score is {1000 -(st.session_state.count * 100)}.")
                st.session_state.game_over = True
            elif diff <= 3:
                st.warning("🔥 You are too close!")
            elif diff <= 8:
                st.warning("⚡ You are close!")
            elif diff <= 15:
                st.warning("📉 You are far!")
            else:
                st.warning("🥶 Cold!")
    
            if st.session_state.count >= st.session_state.attempts and not st.session_state.game_over:
                st.write(f"You are out of attempts. The secret was {st.session_state.secret}.")
                st.session_state.game_over = True
    
        else:
            st.error("❌ Invalid input. Please enter a number between 1-100.")
