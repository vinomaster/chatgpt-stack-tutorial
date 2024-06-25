import os
import streamlit as st
from openai import OpenAI

# Estalish API Client Variable from Session Variable
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

# Deprecated Models. See https://platform.openai.com/docs/deprecations/instructgpt-models
def query_openai(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title("Domain-Specific Text Analytics Chat")

user_input = st.text_input("Ask your question about the corpus:")

if user_input:
    response = query_openai(user_input)
    st.write(response)