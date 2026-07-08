GovGuide Knowledge Pipeline

Offline knowledge base construction pipeline for the GovGuide RAG system.

Features
- PDF text extraction
- Unicode normalization
- Text preprocessing
- Knowledge object creation
- JSON export

Project Structure

code/
data/
output/

Requirements

Python 3.12

Installation

pip install -r requirements.txt

Run

python text_extraction.py
python build_knowledge_objects.py

Future Work

- Automatic parser
- Semantic chunking
- BGE-M3 embeddings
- Qdrant indexing