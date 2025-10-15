import google.generativeai as genai
import os

# Load API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ No GEMINI_API_KEY found. Run:")
    print('   setx GEMINI_API_KEY "your_key_here"')
    exit()

genai.configure(api_key=api_key)

try:
    print("🔍 Fetching available Gemini models...\n")
    models = genai.list_models()
    for m in models:
        if "generateContent" in m.supported_generation_methods:
            print(f"✅ {m.name}")
except Exception as e:
    print(f"⚠️ Error: {e}")
