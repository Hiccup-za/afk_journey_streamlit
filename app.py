import streamlit as st
import pandas as pd
from data import true_data, false_data 

st.set_page_config(
    page_title="AFK Journey",
    page_icon="🧙‍♂️",
    layout="wide"
)

data = {**true_data, **false_data}
df = pd.DataFrame(list(data.items()), columns=["Question", "Answer"])
true_df = df[df['Question'].isin(true_data.keys())]
false_df = df[df['Question'].isin(false_data.keys())]
error_message = "No matching question found."
word_count_error = "Please enter at least two words."

def returnQuestion(user_question):
    user_question_lower = user_question.lower()
    for index, row in df.iterrows():
        if user_question_lower in row["Question"].lower():
            answer = ":green[True]" if row["Answer"] else ":red[False]"
            return row["Question"], answer
    return None, error_message

st.title("🧙‍♂️ Trivia Quiz")

containerQuestion = st.container()
containerList = st.container()

with containerQuestion:
    with st.form(key='question_form'):
        user_question = st.text_input("Question", label_visibility="collapsed", placeholder="Enter the trivia question ...")
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            if not user_question.strip():
                st.error("Question cannot be empty.")
            elif len(user_question.split()) < 3:
                st.error(word_count_error)
            else:
                full_question, answer = returnQuestion(user_question)
                if answer == error_message:
                    st.error(answer)
                else:
                    st.markdown(f"**Question:** {full_question}")
                    st.markdown(f"**Answer:** {answer}")

with containerList:
    st.title("Question List")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("True")
        st.dataframe(true_df[["Question"]], hide_index=True, use_container_width=True)
    with col2:
        st.subheader("False")
        st.dataframe(false_df[["Question"]], hide_index=True, use_container_width=True)