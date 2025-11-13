# Love Proposal - Streamlit app

Place photos in `assets/photos/` and optional audio in `assets/audio/`.

Run locally:
1. python -m venv .venv
2. source .venv/bin/activate   # or .venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. streamlit run app.py

Build and run with Docker:
1. docker build -t love-proposal .
2. docker run -p 8501:8501 love-proposal

Open http://localhost:8501
