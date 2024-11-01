# modules/transcription.py
import openai

def transcribe_audio(audio_file_path):
  with open(audio_file_path, 'rb') as audio_file:
    transcription = openai.Audio.transcribe(model='whisper-1', file=audio_file)
  return transcription#['text']