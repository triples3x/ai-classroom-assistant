# app.py – AI Classroom Assistant (Gemini version)
import streamlit as st
import os
import google.generativeai as genai

# --- Page Setup ---
st.set_page_config(page_title="🤖 AI Classroom Assistant – AP CSP Edition")
st.title("🤖 AI Classroom Assistant – AP CSP Edition")
st.caption("AI-generated • Teacher-reviewed • Ethical & Educational")

# --- API Setup ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("⚠️ Please set your GEMINI_API_KEY in Streamlit Secrets.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# --- Sidebar (Lesson Planner) ---
st.sidebar.header("🧠 Lesson Planner")
topic = st.sidebar.selectbox("Choose an AP CSP topic:", [
    "Algorithms",
    "Data Structures",
    "Abstraction",
    "Variables and Expressions",
    "Lists and Data Structures",
    "The Internet",
    "Cybersecurity"
])
duration = st.sidebar.slider("Lesson Duration (minutes):", 30, 120, 90)

# --- Student Help Bot ---
st.subheader("💬 Student Help Bot")
question = st.text_input("Ask a question about computer science:")

# --- Gemini Logic ---
if st.button("Generate Lesson Plan"):
    with st.spinner("Creating your lesson plan..."):
        prompt = f"Create a detailed {duration}-minute lesson plan for AP CSP on {topic}."
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.success("Lesson plan ready!")
        st.write(response.text)
        st.caption("— Ethics note: Verify AI suggestions and adapt them for your students.")

if question:
    with st.spinner("Thinking..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Answer this AP CSP question: {question}")
        st.write(response.text)
