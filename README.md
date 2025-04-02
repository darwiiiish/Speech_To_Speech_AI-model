# Speech-to-Speech AI System

This project is a **Speech-to-Speech AI system** powered by the **Gemini 3 model**. It enables real-time speech conversion, starting with recognizing spoken words, processing them through the Gemini 3 AI model for context-based response generation, and finally converting the response back into speech. The system leverages advanced AI and speech technologies to create a seamless conversational experience.

---

## Key Features:

- **Speech Recognition**: 
  - Utilizes the `speech_recognition` library to listen to audio input and transcribe spoken words into text.
  - Supports a **timeout function**, allowing users to speak freely for a set amount of time or stop early by saying a specific phrase ("thanks").
  
- **AI Response Generation**:
  - The recognized speech is sent to Google’s Gemini 3 model (via the `google.generativeai` library).
  - The AI processes the input and generates a relevant, intelligent response based on the prompt received.

- **Text-to-Speech**:
  - Converts the AI-generated response back to speech using **Google Text-to-Speech** (`gTTS`).
  - Plays the speech back to the user through the `pygame` library.

- **Backend API**: 
  - Built with **FastAPI**, the backend exposes an endpoint (`/process_speech/`) that receives user input (speech), processes it through the AI, and returns the AI-generated response as speech.

- **Frontend**: 
  - The frontend is built using **HTML**, **CSS**, and **JavaScript**, providing a simple interface for user interaction.

---

## Flow:

1. **User Input**: 
   - The user speaks into a microphone.
   
2. **Speech Recognition**: 
   - The system listens to the input and converts the speech into text.
   
3. **AI Processing**: 
   - The recognized text is sent to the **Gemini 3 AI model** for processing and response generation.

4. **Response Playback**: 
   - The generated response is converted back to speech and played to the user.

---

## Tech Stack:

- **Frontend**: 
  - HTML, CSS, JavaScript
  
- **Backend**: 
  - FastAPI, Python
  
- **Speech Recognition**: 
  - `speech_recognition` library
  
- **Text-to-Speech**: 
  - `gTTS` (Google Text-to-Speech), `pygame`
  
- **AI Processing**: 
  - Google Gemini 3 API (`google.generativeai`)
