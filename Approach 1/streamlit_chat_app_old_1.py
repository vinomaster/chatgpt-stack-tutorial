import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-proj-zkmbQAHkUYodRgXAHI1pT3BlbkFJu6ZVbs92vlY9QKnmg6rv'

def query_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title("Domain-Specific Text Analytics Chat")

user_input = st.text_input("Ask your question about the corpus:")

if user_input:
    response = query_openai(user_input)
    st.write(response)
