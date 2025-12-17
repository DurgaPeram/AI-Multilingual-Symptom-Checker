import google.generativeai as genai
import os
import json

# ✅ Configure Gemini API
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
else:
    print("⚠️ GEMINI_API_KEY not found. Please set it using:")
    print('   setx GEMINI_API_KEY "your_key_here"')

# ✅ Supported Languages
SUPPORTED_LANGS = {
    "en": "English",
    "te": "Telugu",
    "hi": "Hindi",
    "ta": "Tamil",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
    "gu": "Gujarati",
    "mr": "Marathi",
    "ur": "Urdu",
    "fr": "French",
    "es": "Spanish"
}


def ai_diagnose(symptoms, lang="en"):
    """
    Takes list of symptoms and returns probable disease info in selected language.
    """
    if not GEMINI_KEY:
        return {"error": "Gemini API key not found."}

    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
    symptom_text = ", ".join(symptoms)

    base_prompt = f"""
    You are a professional and empathetic medical assistant.
    A patient reports the following symptoms: {symptom_text}.
    Based on these, predict the most likely disease and provide:
    - Disease name
    - Short description
    - Causes
    - Precautions / home remedies
    - When to seek medical help

    Return output ONLY in this JSON format:

    {{
      "disease": "Disease name",
      "description_en": "Brief explanation of the disease in English.",
      "causes": "List of possible causes.",
      "precautions": "Self-care or prevention methods.",
      "when_to_seek_help": "When to see a doctor or hospital.",
      "confidence": 0.85
    }}
    """

    try:
        response = model.generate_content(base_prompt)
        text = response.text.strip()

        start = text.find("{")
        end = text.rfind("}") + 1
        data = json.loads(text[start:end])

        # ✅ English output by default
        if lang == "en":
            return data

        # ✅ Translation to selected language
        if lang in SUPPORTED_LANGS:
            lang_name = SUPPORTED_LANGS[lang]
            translation_prompt = f"""
            Translate the following medical information from English to {lang_name}.
            Maintain medical accuracy and empathy.
            Keep the same JSON structure (translate values only, not keys).

            Input JSON:
            {json.dumps(data, ensure_ascii=False)}
            """

            t_response = model.generate_content(translation_prompt)
            t_text = t_response.text.strip()
            t_start = t_text.find("{")
            t_end = t_text.rfind("}") + 1

            try:
                translated = json.loads(t_text[t_start:t_end])
                return translated
            except Exception:
                data["note"] = f"⚠️ Translation to {lang_name} failed. Showing English version."
                return data
        else:
            data["note"] = f"⚠️ Language code '{lang}' not supported."
            return data

    except Exception as e:
        return {"error": f"AI diagnosis failed: {e}"}
