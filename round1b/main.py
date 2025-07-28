import os
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"
MODEL_PATH = "/app/model"

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def embed(model, txt):
    return model.encode([txt])[0]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load persona
    persona_file = os.path.join(INPUT_DIR, "persona.json")
    if not os.path.exists(persona_file):
        raise FileNotFoundError("persona.json is required in input folder for 1B")

    persona_data = load_json(persona_file)
    persona = persona_data.get("persona", "Unknown Persona")
    job = persona_data.get("job", "Unknown Task")

    # Load all document JSON files (from 1A)
    doc_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".json") and f != "persona.json"]
    documents = []
    for f in doc_files:
        data = load_json(os.path.join(INPUT_DIR, f))
        documents.append((f, data))

    if not documents:
        print("No document JSON files found in input.")
        return

    model = SentenceTransformer(MODEL_PATH)
    combined_text = persona + " " + job
    persona_vec = embed(model, combined_text)

    scores = []
    for filename, doc in documents:
        for section in doc.get("outline", []):
            text = section.get("text", "")
            level = section.get("level", "")
            page = section.get("page", 1)
            score = cosine_similarity([persona_vec], [embed(model, text)])[0][0]
            scores.append((score, filename.replace(".json", ".pdf"), level, text, page))

    # Sort by score descending
    scores.sort(reverse=True, key=lambda x: x[0])

    extracted_sections = []
    subsection_analysis = []

    for rank, (score, doc_name, level, text, page) in enumerate(scores[:20], 1):
        extracted_sections.append({
            "document": doc_name,
            "section_title": text,
            "importance_rank": rank,
            "page_number": page
        })

        subsection_analysis.append({
            "document": doc_name,
            "refined_text": f"Relevant analysis for {text}",
            "page_number": page
        })

    output = {
        "metadata": {
            "input_documents": [f for f, _ in documents],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    out_path = os.path.join(OUTPUT_DIR, "output.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Output written to {out_path}")

if __name__ == "__main__":
    main()
