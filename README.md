 Doc Summarizer:

An AI-powered document summarization tool built using Python, Streamlit, and Ollama (LLaMA 3). 
This application allows users to upload PDF documents and generate intelligent summaries locally without using paid APIs.


Features:-

- Upload PDF documents
- Extract text from PDF
- Generate AI-based summaries using LLaMA 3
- Runs completely locally
- Simple and interactive Streamlit UI


Tech Stack:-

- Python
- Streamlit
- Ollama (LLaMA 3)
- PyPDF

Doc-Summarizer-Llama/
│
├── app.py # Main Streamlit application
├── pdf_utils.py # PDF text extraction logic
├── summarizer.py # LLM summarization logic
├── requirements.txt # Project dependencies
└── README.md # Project documentation



---Installation & Setup:

1. Clone the Repository - 
git clone https://github.com/Rashi-07Ch/Doc-Summarizer-Llama.git
cd Doc-Summarizer-Llama


2. Create Virtual Environment-
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux

3. Install Dependencies-
   pip install -r requirements.txt

4. Install Ollama - "Then pull the LLaMA 3 model: ollama pull llama3"

5. Run the Application-
   streamlit run app.py
