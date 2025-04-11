import streamlit as st
import os
from groq import Groq

# Set page configuration
st.set_page_config(
    page_title="CLAT Exam Chatbot",
    page_icon="⚖️",
    layout="centered"
)

# Initialize Groq client
def initialize_groq_client():
    # First try to get API key from environment variables
    api_key = "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"
    
    # If not found in environment, ask the user
    if not api_key:
        api_key = st.text_input("Enter your Groq API Key:", type="password")
        if not api_key:
            st.warning("Please enter a valid Groq API Key to continue.")
            st.stop()
    
    return Groq(api_key=api_key)

# Define CLAT knowledge base for context
CLAT_KNOWLEDGE = """
CLAT (Common Law Admission Test) Knowledge Base:

General Information:
- CLAT is a national level entrance exam for admissions to undergraduate and postgraduate law programs in 22 National Law Universities in India.
- The exam is conducted by the Consortium of NLUs on a rotational basis.
- CLAT 2025 is likely to be conducted in May 2025.

CLAT UG Exam Pattern 2025:
- Total Questions: 120
- Total Time: 2 hours
- Marking Scheme: +1 for correct answers, -0.25 for incorrect answers
- Medium: English
- Mode: Computer-based test at designated centers

CLAT UG Syllabus 2025:
1. English Language (20% of the paper):
   - Reading comprehension
   - Grammar and vocabulary usage
   - Number of questions: ~24

2. Current Affairs & General Knowledge (25% of the paper):
   - Current national and international affairs
   - Static GK
   - Number of questions: ~30

3. Legal Reasoning (25% of the paper):
   - Legal principles and their application
   - Legal scenarios and passages
   - Number of questions: ~30

4. Logical Reasoning (20% of the paper):
   - Deductive and inductive reasoning
   - Analogy and pattern recognition
   - Number of questions: ~24

5. Quantitative Techniques (10% of the paper):
   - Basic mathematical concepts
   - Data interpretation
   - Number of questions: ~12

CLAT PG Syllabus:
- Constitutional Law
- Jurisprudence
- Other Law subjects from the Bachelor's curriculum
- Current Affairs & General Knowledge

Cut-offs from CLAT 2024:
- NLSIU Bangalore: 117.25 (General Category)
- NALSAR Hyderabad: 111.75 (General Category)
- NLIU Bhopal: 103.5 (General Category)
- NLU Delhi (separate entrance): Not applicable
- WBNUJS Kolkata: 107.25 (General Category)

Eligibility Criteria:
- For UG: 10+2 with minimum 45% marks (40% for SC/ST)
- For PG: LLB degree with minimum 55% marks (50% for SC/ST)

Important Preparation Tips:
- Focus on reading comprehension and critical thinking
- Stay updated with current affairs
- Practice previous year papers
- Develop analytical skills for legal reasoning
"""

# Function to get response from Groq
def get_groq_response(client, query):
    try:
        prompt = f"""You are a helpful assistant specifically knowledgeable about the Common Law Admission Test (CLAT) in India.
        Please provide accurate, concise, and helpful answers to questions about CLAT exam patterns, syllabus, preparation, eligibility, and related topics.
        
        Here is some information about CLAT that you can use:
        {CLAT_KNOWLEDGE}
        
        User Query: {query}
        
        Respond with accurate information based on the knowledge provided. If you don't have specific information about a query, acknowledge that and provide general guidance instead of speculating. Keep your answers focused and relevant to CLAT.
        """
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",  # Using Llama 3 70B model via Groq
            max_tokens=1024,
            temperature=0.3,
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Main app interface
def main():
    st.title("⚖️ CLAT Exam Chatbot")
    st.markdown("Ask any questions about CLAT exam syllabus, pattern, or preparation!")
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Initialize Groq client
    client = initialize_groq_client()
    
    # Handle user input
    if prompt := st.chat_input("Ask about CLAT..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response with a spinner while waiting
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_groq_response(client, prompt)
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Add sidebar with instructions
    with st.sidebar:
        st.subheader("About")
        st.markdown("""
        This chatbot helps you find information about the Common Law Admission Test (CLAT).
        
        **Sample Questions:**
        - What is the syllabus for CLAT 2025?
        - How many questions are in the English section?
        - What are the cut-offs for NLSIU Bangalore?
        - What is the eligibility criteria for CLAT?
        """)
        
        st.divider()
        st.caption("By Aryan Kakran")

if __name__ == "__main__":
    main()
