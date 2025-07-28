
# Approach Explanation

## Round 1A – OCR + Multimodal Headings Extraction
1. Parse PDF text blocks using PyMuPDF.
2. If no text: use Tesseract OCR fallback.
3. Identify hierarchical headings using visual and textual cues.
4. Output structured JSON.

## Round 1B – PersonaGraph Multimodal AI
1. Load all structured JSON files from Round 1A.
2. Build embeddings for each section and persona.
3. Rank sections based on semantic similarity to persona+job.
4. Output JSON with ranked sections and metadata.

---

## Key Technologies
- PyMuPDF, pdfplumber
- Tesseract OCR
- OpenCV
- SentenceTransformers (MiniLM multilingual, offline)
- Scikit-learn cosine similarity
