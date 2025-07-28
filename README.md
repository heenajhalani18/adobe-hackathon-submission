
# Adobe Hackathon – Connecting the Dots (Final Submission)

This package includes complete solutions for:
- **Round 1A** – Multimodal, OCR-enabled heading extraction
- **Round 1B** – PersonaGraph AI for ranking sections based on persona/job context

All code, Dockerfiles, instructions, and a sample persona.json are included so this zip can be directly evaluated without external dependencies.

---

## Highlights

- **Multimodal:** Text + layout features, optional OCR fallback
- **Multilingual:** Handles multiple languages
- **Embeddings:** Persona-driven section ranking with offline MiniLM model
- **Offline:** No network access required

---

## Instructions

### Round 1A
1. Navigate:
```
cd round1a
```
2. Build:
```
docker build --platform linux/amd64 -t round1a:latest .
```
3. Run:
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none round1a:latest
```

Output JSON files will be created in `/output`.

### Round 1B
1. Copy `round1a/output/*.json` to `round1b/input`.
2. Ensure `round1b/input/persona.json` is present (a sample file is included).
3. Build:
```
docker build --platform linux/amd64 -t round1b:latest .
```
4. Run:
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none round1b:latest
```

Ranked results will appear in `round1b/output/output.json`.

---

## Persona Input File Format

**persona.json**
```json
{
  "persona": "Investment Analyst",
  "job": "Analyze revenue trends, R&D investments, and market positioning strategies"
}
```

---

### Notes

- `round1b/model/` already contains the offline embedding model for evaluation.
- No internet is required during execution.
