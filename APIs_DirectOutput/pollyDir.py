import boto3
from pydub import AudioSegment
from pydub.playback import play
import io

# Initializing variables
CHANNELS = 1  # Polly's output is a mono audio stream
RATE = 16000  # Polly supports 16000Hz and 8000Hz output for PCM format
# OUTPUT_FILE_IN_WAVE = "../Evaluation/sample_SSML.wav"  # WAV format Output file  name
FRAMES = []
WAV_SAMPLE_WIDTH_BYTES = 2  # Polly's output is a stream of 16-bits (2 bytes) samples

# Initializing Polly Client
polly = boto3.client('polly',
                     region_name='us-east-1',
                     aws_access_key_id='AKIA2FN6DM6LMUCANVP2',
                     aws_secret_access_key='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')

INPUT = 'Hello Hongli! Mojitaba loves you.'
result = polly.synthesize_speech(Text=INPUT,
                                 OutputFormat='mp3',
                                 VoiceId='Kimberly')

audio = result['AudioStream'].read()
print(audio)
song = AudioSegment.from_file(io.BytesIO(audio), format="mp3")
play(song)
