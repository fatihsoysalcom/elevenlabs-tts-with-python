import os
import requests

# This script demonstrates how to use the ElevenLabs v3 Text-to-Speech API.
# It requires an ElevenLabs API key, which you should set as an environment variable.

# --- Configuration ---
# Replace with your actual ElevenLabs API key or set it as an environment variable.
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "YOUR_ELEVENLABS_API_KEY")

# The API endpoint for text-to-speech
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

# --- Input Parameters ---
# The text you want to convert to speech
TEXT_TO_SYNTHESIZE = "Merhaba, bu ElevenLabs v3 ve DigitalOcean ile yapay zeka ses üretimi üzerine bir denemedir."

# The voice ID you want to use. You can find available voice IDs in the ElevenLabs documentation.
# Example: '21m00Tcm4Tlv7q8f297f' (Adam)
VOICE_ID = "21m00Tcm4Tlv7q8f297f"

# The model to use. 'eleven_monolingual_v1' is a good general-purpose model.
MODEL_ID = "eleven_monolingual_v1"

# Output filename for the generated audio
OUTPUT_FILENAME = "output.mp3"

# --- Main Function ---
def generate_speech(text, voice_id, model_id, api_key):
    """Generates speech from text using the ElevenLabs API."""

    if api_key == "YOUR_ELEVENLABS_API_KEY":
        print("Error: Please set your ELEVENLABS_API_KEY environment variable or replace the placeholder.")
        return

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text,
        "model_id": model_id,
        "voice_id": voice_id
    }

    try:
        response = requests.post(API_URL, json=data, headers=headers, stream=True)
        response.raise_for_status() # Raise an exception for bad status codes

        with open(OUTPUT_FILENAME, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        print(f"Successfully generated speech and saved to {OUTPUT_FILENAME}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if response.status_code == 401:
            print("Check your API key.")
        elif response.status_code == 422:
            print("Check your voice ID or model ID.")

# --- Execution ---
if __name__ == "__main__":
    generate_speech(TEXT_TO_SYNTHESIZE, VOICE_ID, MODEL_ID, ELEVENLABS_API_KEY)
