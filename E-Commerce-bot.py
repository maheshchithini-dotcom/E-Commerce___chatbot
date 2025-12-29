import streamlit as st
import os
from google import genai
from google.genai import types

# --- 1. SETUP PAGE ---
st.set_page_config(
    page_title="E-Commerce Return & Refund Explainer",
    page_icon="🛒",
    layout="centered"
)

# --- 2. API KEY SETUP ---
# FIXED: We use the key string directly. No 'os.environ.get' needed here.
API_KEY = "AIzaSyBInIwAWGe3YnSFhyFqW-3WKQH1j1CblqU"

# FIXED: Use a currently active model
MODEL_NAME = "gemini-3-flash-preview"

SYSTEM_PROMPT = """
You are an E-Commerce Return & Refund Process Explainer Chatbot.

Your role is to ONLY explain e-commerce return, refund, and replacement processes.

You must:
- Explain return eligibility
- Explain return steps
- Explain inspection and refund stages
- Explain refund timelines and delays

STRICT RULES:
- Do NOT initiate or track returns or refunds
- Do NOT access user accounts or order details
- Do NOT promise refund dates or approvals
- Do NOT give legal or financial advice

If user asks for actions:
Reply: "I can explain the process, but I can’t access or modify orders."

Be clear, friendly, and professional.
"""

# --- 3. INITIALIZE CLIENT ---
@st.cache_resource
def init_client():
    try:
        # We pass the key directly here
        return genai.Client(api_key=API_KEY)
    except Exception as e:
        st.error(f"Failed to initialize API client: {e}")
        return None

client = init_client()

# --- 4. CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I can explain return and refund processes. How can I help you?"}
    ]

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input area
user_input = st.chat_input("Ask about returns or refunds...")

if user_input and client:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=SYSTEM_PROMPT + "\n\nUser Question:\n" + user_input
                    )
                ],
            )
        ]

        # Config without "thinking" (safer for this model)
        config = types.GenerateContentConfig(
            temperature=0.5,
        )

        try:
            for chunk in client.models.generate_content_stream(
                model=MODEL_NAME,
                contents=contents,
                config=config
            ):
                if chunk.text:
                    full_response += chunk.text
                    response_placeholder.markdown(full_response)
            
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
            
        except Exception as e:
            st.error(f"Error generating response: {e}")