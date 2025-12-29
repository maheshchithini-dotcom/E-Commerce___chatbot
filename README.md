# E-Commerce Return & Refund Explainer Bot

An AI-powered chatbot that helps customers understand the return and refund processes of e-commerce platforms.

## Features
- **Explains Return Eligibility**: Clarifies rules for returns.
- **Workflow Guidance**: Explains what happens after a return request.
- **Refund Timelines**: Details on processing stages and bank delays.
- **Safe & Secure**: Does NOT process transactions or modify orders.

## Tech Stack
- **Gemini 3 Flash Preview**: Fast and consistent generative AI responses.
- **Streamlit**: Elegant web interface for interaction.
- **Python**: Core logic and API integration.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Setup**:
   - Get a Google AI Studio API Key from [Google AI Studio](https://aistudio.google.com/).
   - Copy `.env.example` to `.env` and add your key:
     ```bash
     cp .env.example .env
     ```
   - Alternatively, you can enter the key directly in the app's sidebar.

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## Example Queries to Try
- "What is the return policy for electronics?"
- "I requested a return yesterday, what happens next?"
- "Explain why my refund is taking 5-7 days."
- "Can you process a refund for my last order?" (Watch the bot politely decline!)
