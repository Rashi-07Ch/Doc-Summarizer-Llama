import requests

# -------- Chunking --------
def chunk_text(text, chunk_size=1500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# -------- Call Ollama --------
def call_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# -------- Summarize Each Chunk --------
def summarize_chunk(chunk):
    prompt = f"Summarize the following section:\n\n{chunk}"
    return call_ollama(prompt)


# -------- Final Structured Summary --------
def generate_final_summary(combined_summary):
    final_prompt = f"""
    Based on the following content generate:

    - Executive Summary
    - Key Points
    - Risks or Concerns
    - Opportunities
    - Action Items

    Content:
    {combined_summary}
    """
    return call_ollama(final_prompt)