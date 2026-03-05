import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import chunk_text, summarize_chunk, generate_final_summary

st.title("📄 DOC Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Chunking document..."):
        chunks = chunk_text(text)

    partial_summaries = []

    for i, chunk in enumerate(chunks):
        with st.spinner(f"Summarizing chunk {i+1}/{len(chunks)}..."):
            summary = summarize_chunk(chunk)
            partial_summaries.append(summary)

    combined_summary = "\n".join(partial_summaries)

    with st.spinner("Generating final structured summary..."):
        final_summary = generate_final_summary(combined_summary)

    st.subheader("Structured Summary Output")
    st.write(final_summary)