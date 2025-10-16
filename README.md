# Multilingual Symptom Checker

A Streamlit-based web app that provides preliminary health guidance by matching user-entered symptoms to likely diseases and showing multilingual descriptions. Designed for quick local testing and demonstration.

# Access this site through
https://ai-multilingual-symptom-checker-jsxjtfj4ayeehyftvuv54d.streamlit.app/

## Features

- Enter up to 4 symptoms and get a probable diagnosis.
- Multilingual descriptions (English, Telugu, Tamil, Hindi) where available.
- Health tips slideshow on the left panel.
- Simple, responsive UI built with Streamlit and custom CSS.
- Local image embedding so slideshow works inside Streamlit's iframe.

## Project structure (key files)

- `Home.py` - Main Streamlit application.
- `utils.py` - Helper functions for loading data, processing user input and matching diseases.
- `pages/` - Additional Streamlit pages (About, Government Schemes, Feedback, Help).
- `static/` - Images and static assets used by the UI.
- `styles/` - Custom CSS files.
- `requirements.txt` - Python dependencies.
- `.gitignore` - Files and folders excluded from git.

## Requirements

- Python 3.8+ (3.10 or 3.11 recommended)
- pip
- A modern browser (Chrome/Edge/Firefox)

## Quick start (Windows PowerShell)

1. Open PowerShell and change to the project directory:

```powershell
cd "C:\MINOR 1\symptom_checker_streamlit"
```

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the Streamlit app:

```powershell
streamlit run Home.py
```

5. Open the URL shown in the terminal (usually `http://localhost:8501`).

## How to add/change slideshow images

- Put image files in `static/images/`.
- Update the `image_files` list inside `Home.py` if you add different file names.
- The app embeds images as base64 to ensure they display correctly inside Streamlit's HTML iframe.

## Data and descriptions

- Symptom and disease mapping is read by helper functions in `utils.py` from the CSV files in the project root.
- If you add dataset files, ensure they are excluded in `.gitignore` if they are large or private.

## Common troubleshooting

- If Streamlit fails to start: make sure you installed the packages and are running the right Python interpreter.
- Port conflict: if port 8501 is in use, set a different port when running:

```powershell
streamlit run Home.py --server.port 8502
```

- Images not appearing in slideshow: ensure images exist in `static/images/` and are readable by the app.

- If translations are missing: check `disease_descriptions.csv` to ensure descriptions exist for the selected language code.

## Development notes

- The slideshow uses inline CSS/JS injected via `components.html(...)` to run inside Streamlit's iframe.
- Result text is rendered as an HTML block to allow multilingual text and custom styling.

## Contributing

If you'd like to contribute:

1. Fork the repository on GitHub.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Make changes and commit: `git commit -m "Add feature"`.
4. Push to your fork and open a Pull Request.

## License

This project is provided under the MIT License. See the `LICENSE` file (if present) or add one to fit your needs.


## AI-based diagnosis (optional)

This project includes an optional AI-based diagnosis flow using OpenAI. To enable it:

1. Install the OpenAI package (already added to `requirements.txt`):

```powershell
pip install -r requirements.txt
```

2. Set your OpenAI API key either as an environment variable or in Streamlit secrets:

- Environment variable (PowerShell):

```powershell
$env:OPENAI_API_KEY = "sk-..."
```

- Streamlit secrets: create a file `.streamlit/secrets.toml` with:

```toml
OPENAI_API_KEY = "sk-..."
```

3. Run the AI-enabled app file `Home_AI.py` instead of `Home.py`:

```powershell
streamlit run Home_AI.py
```

Notes:
- The AI flow calls Google Gemini's ChatCompletion API and returns a JSON-like response parsed into fields. Keep your API key secret and monitor usage to avoid unexpected charges.
- The AI diagnosis is provided for informational purposes only and is not a substitute for professional medical advice.
