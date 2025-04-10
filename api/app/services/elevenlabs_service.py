# app/services/elevenlabs_service.py
from io import BytesIO
from elevenlabs.client import ElevenLabs
import os

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def transcribe_audio(file_bytes: bytes, filename: str) -> str:
    audio_data = BytesIO(file_bytes)
    result = client.speech_to_text.convert(
        file=audio_data,
        model_id="scribe_v1",
        language_code="kor",
        diarize=True,
        tag_audio_events=True
    )

    print(f"Transcription result: {result.text}")
    return result.text
