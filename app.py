import os
from dotenv import load_dotenv
import openai
import transcription,summarization,file_operations
from pydub import AudioSegment
import streamlit as st

load_dotenv()
openapikey = os.getenv('input_key')
openai.api_key = openapikey

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"  # Replace with your actual API key

# Streamlit app UI
st.title("Meeting Assistant")
st.write("Upload an audio file to transcribe and generate meeting minutes.")

# Audio file upload
uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_uploaded_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    # Preprocess audio to limit it to the first 3 minutes
    audio_segment = AudioSegment.from_file("temp_uploaded_audio.mp3")
    first_3_minutes = audio_segment[:3 * 60 * 1000]  # 3 minutes in milliseconds
    first_3_minutes.export("temp_short_audio.mp3", format="mp3")

    # Transcribe audio
    st.write("Transcribing audio, please wait...")
    transcription_result = transcription.transcribe_audio("temp_short_audio.mp3")
    transcription_text = transcription_result['text']
    st.subheader("Transcription")
    st.text_area("Meeting Transcription:", transcription_text, height=300)

    # Generate meeting minutes
    if st.button("Generate Meeting Minutes"):
        st.write("Processing transcription for meeting minutes...")

        audio_file_path = 'sampleAudio.mp3'        
        audio_file_segment = AudioSegment.from_mp3(audio_file_path)

        # PyDub handles time in milliseconds
        ten_minutes = 3 * 60 * 1000
        first_3_minutes = audio_file_segment[:ten_minutes]
        first_3_minutes.export("sample.mp3", format="mp3")
        

        audio_file_path = 'sample.mp3'
        transcription = transcription.transcribe_audio(audio_file_path)
        minutes = summarization.meeting_minutes(transcription['text'])
        file_operations.save_as_docx(minutes, 'sampleAudio.docx')
        st.success("Meeting minutes saved as 'MeetingMinutes.docx'")
else:
    st.info("Please upload an audio file to begin.")
