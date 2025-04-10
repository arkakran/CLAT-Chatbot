# CLAT Exam Chatbot

⚖️ A Streamlit-based chatbot that provides information about the Common Law Admission Test (CLAT) in India.

## Overview

The CLAT Exam Chatbot is designed to help aspiring law students access accurate, concise information about the Common Law Admission Test (CLAT). The application leverages Groq's LLaMA 3 70B model to provide detailed responses to queries about exam patterns, syllabus, preparation strategies, eligibility criteria, and more.

## Features

- **Interactive Chat Interface**: Ask questions in natural language and receive detailed responses
- **Comprehensive CLAT Knowledge Base**: Built-in information about CLAT UG and PG exams
- **Real-time Responses**: Powered by Groq's LLaMA 3 70B large language model
- **Chat History**: Maintains conversation context throughout your session

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/clat-exam-chatbot.git
cd clat-exam-chatbot
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install streamlit groq
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. The application will open in your default web browser. If not, navigate to `http://localhost:8501`.

3. The app uses a pre-configured Groq API key. If needed, you can provide your own API key in the interface.

4. Start asking questions about CLAT in the chat input field.

## Sample Questions

- What is the syllabus for CLAT 2025?
- How many questions are in the English section?
- What are the cut-offs for NLSIU Bangalore?
- What is the eligibility criteria for CLAT UG?
- How should I prepare for the Legal Reasoning section?

## Customization

The knowledge base can be expanded or modified by updating the `CLAT_KNOWLEDGE` variable in the code. This allows you to add more specific information or update details as new CLAT information becomes available.

## Security Note

For production deployment, it's recommended to:
- Store your API key as an environment variable instead of hardcoding it
- Implement proper authentication if deploying publicly
- Consider rate limiting to control API usage costs

## License

[MIT License](LICENSE)

## Acknowledgements

- Powered by [Groq](https://groq.com/) LLaMA 3 model
- Built with [Streamlit](https://streamlit.io/)

## Contact

For questions or support, please open an issue on this repository or contact [your-email@example.com].
