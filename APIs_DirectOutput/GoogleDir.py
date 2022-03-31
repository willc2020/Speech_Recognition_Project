from google.cloud import texttospeech
import os
from pydub import AudioSegment
from pydub.playback import play
import io

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/willchen/Desktop/499Project/TTS_APIs/hazel-delight-343602-666dbe2a8e0b.json"
# Instantiates a client
client = texttospeech.TextToSpeechClient()

INPUT = 'Hi Jackson!'
synthesis_input = texttospeech.SynthesisInput(text=INPUT)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
print(response.audio_content)
song = AudioSegment.from_file(io.BytesIO(response.audio_content), format="mp3")
play(song)
