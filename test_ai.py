from utils_AI import ai_diagnose
import os

# Ensure the OPENAI_API_KEY is set in environment or in .streamlit/secrets.toml
key = os.environ.get('OPENAI_API_KEY')
if not key:
    print('OPENAI_API_KEY not found in environment. Make sure .streamlit/secrets.toml or env var is set.')

symptoms = ['fever', 'sore throat', 'runny nose']
try:
    result = ai_diagnose(symptoms, openai_key=key)
    print('AI diagnosis result:')
    if isinstance(result, dict):
        for k, v in result.items():
            print(f"{k}:\n{v}\n")
    else:
        # result is likely an error message or raw text
        print(result)
except Exception as e:
    print('AI diagnose failed:', e)
