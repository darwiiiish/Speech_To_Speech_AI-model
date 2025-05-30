import google.generativeai as genai

GENAI_API_KEY = "AIzaSyDqfJsm4sLI7xMC4J1__ZEaqE3XuCNE7QQ"
genai.configure(api_key=GENAI_API_KEY)

def ask_gemini(prompt):
    # (choose model from these)
    # models/chat-bison-001
    # models/text-bison-001
    # models/embedding-gecko-001
    # models/gemini-1.0-pro-vision-latest
    # models/gemini-pro-vision
    # models/gemini-1.5-pro-latest
    # models/gemini-1.5-pro-001
    # models/gemini-1.5-pro-002
    # models/gemini-1.5-pro
    # models/gemini-1.5-flash-latest
    # models/gemini-1.5-flash-001
    # models/gemini-1.5-flash-001-tuning
    # models/gemini-1.5-flash
    # models/gemini-1.5-flash-002
    # models/gemini-1.5-flash-8b
    # models/gemini-1.5-flash-8b-001
    # models/gemini-1.5-flash-8b-latest
    # models/gemini-1.5-flash-8b-exp-0827
    # models/gemini-1.5-flash-8b-exp-0924
    # models/gemini-2.5-pro-exp-03-25
    # models/gemini-2.0-flash-exp
    # models/gemini-2.0-flash
    # models/gemini-2.0-flash-001
    # models/gemini-2.0-flash-exp-image-generation
    # models/gemini-2.0-flash-lite-001
    # models/gemini-2.0-flash-lite
    # models/gemini-2.0-flash-lite-preview-02-05
    # models/gemini-2.0-flash-lite-preview
    # models/gemini-2.0-pro-exp
    # models/gemini-2.0-pro-exp-02-05
    # models/gemini-exp-1206
    # models/gemini-2.0-flash-thinking-exp-01-21
    # models/gemini-2.0-flash-thinking-exp
    # models/gemini-2.0-flash-thinking-exp-1219
    # models/learnlm-1.5-pro-experimental
    # models/gemma-3-4b-it
    # models/gemma-3-12b-it
    # models/gemma-3-27b-it
    # models/embedding-001
    # models/text-embedding-004
    # models/gemini-embedding-exp-03-07
    # models/gemini-embedding-exp
    # models/aqa
    # models/imagen-3.0-generate-002
    model = genai.GenerativeModel("gemma-3-27b-it")
    response = model.generate_content(prompt)
    return response.text
