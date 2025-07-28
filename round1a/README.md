# Round 1A – Document Parsing & Outline Extraction

## Overview
This Docker container processes input PDF files and extracts:
- Page-level text
- Outline/section headings with page numbers

The output for each PDF is stored as a JSON file in `/app/output`.

## Input
Place one or more `.pdf` files in the `input/` folder before running.

## Output
For every input PDF, a corresponding `.json` file is created in the `output/` folder with the structure:

```json
{
  "filename": "sample.pdf",
  "outline": [
    { "level": "Heading 1", "text": "Introduction", "page": 1 },
    { "level": "Heading 2", "text": "Methodology", "page": 2 }
  ]
}

