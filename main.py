from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini_communication import ask_gemini
from speech_text import listen_with_timeout
from text_to_speech import text_to_speech

app = FastAPI()

# due to diffrent origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_speech/")
async def process_speech():

    # convert speech to text
    text = listen_with_timeout()

    # deliver the text to google gemma 3 model
    gemini_response = ask_gemini(text)

    # convert the responce text to speech
    text_to_speech(gemini_response)

    return {
        "recognized_text": text,
        "gemini_response": gemini_response
    }
if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
