import streamlit as st
from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key="")

# Read external txt file for the description of the character
with open("qinche_description.txt", "r", encoding="utf-8") as file:
    qinche_description = file.read()

# Initial system message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": qinche_description}
    ]

st.title("秦彻 AI 助手")

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("猎人小姐: ")

if user_input:
    # Add user message to the conversation history
    st.session_state.messages.append({"role": "user", "content": f"猎人小姐: {user_input}"})
    
    with st.chat_message("user"):
        st.write(f"猎人小姐: {user_input}")

    # Generate a response from the model
    with st.spinner("秦彻正在思考..."):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0.85
        )

    # Get the assistant's reply
    assistant_reply = completion.choices[0].message.content
    
    # Add assistant reply to the conversation history
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    
    with st.chat_message("assistant"):
        st.write(f"秦彻: {assistant_reply}")

    # Get token usage from the response
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    total_tokens = completion.usage.total_tokens

    # Display token usage information
    st.sidebar.write(f"Tokens used - Input: {prompt_tokens}, Output: {completion_tokens}, Total: {total_tokens}")

# Clear chat button
if st.sidebar.button("清除对话"):
    st.session_state.messages = [{"role": "system", "content": qinche_description}]
    st.rerun()
