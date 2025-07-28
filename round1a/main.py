
import fitz
import json
import os
import subprocess

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def ocr_page(pdf_path, page_num):
    out = f"/tmp/page_{page_num}.ppm"
    subprocess.run(["pdftoppm", "-f", str(page_num+1), "-l", str(page_num+1), pdf_path, "/tmp/page", "-singlefile"])
    txt = subprocess.check_output(["tesseract", out, "stdout"])
    return txt.decode("utf-8")

def extract(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")
    for page_num, page in enumerate(doc, start=0):
        blocks = page.get_text("blocks")
        if not blocks:
            texts = [ocr_page(pdf_path, page_num)]
        else:
            texts = [b[4] for b in blocks]
        for t in texts:
            t = t.strip()
            if not t: continue
            level = "H3"
            if len(t.split()) < 5:
                level = "H1" if t.isupper() else "H2"
            outline.append({"level": level, "text": t, "page": page_num+1})
    return {"title": title, "outline": outline}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(INPUT_DIR):
        if f.endswith(".pdf"):
            data = extract(os.path.join(INPUT_DIR, f))
            with open(os.path.join(OUTPUT_DIR, f.replace(".pdf", ".json")), "w") as out:
                json.dump(data, out, indent=2)

if __name__ == "__main__":
    main()
