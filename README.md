# Meeting-Assistance

This GenAI Meeting Assistant app processes audio files from meetings, transcribes them, and generates summarized meeting minutes with action items, key points, and sentiment analysis. The results are saved in a `.docx` document.

Used OpenAI's Whisper and GPT-4 models to develop an automated meeting minutes generator. The application transcribes audio from a meeting, provides a summary of the discussion, extracts key points and action items, and performs a sentiment analysis.

https://platform.openai.com/docs/tutorials/meeting-minutes
## Features

- **Transcription**: Uses OpenAI Whisper to convert audio to text.
- **Summarization**: Abstract summary of the transcription.
- **Key Points Extraction**: Identifies main points discussed.
- **Action Item Extraction**: Extracts tasks assigned in the meeting.
- **Sentiment Analysis**: Determines the general sentiment of the meeting.

## Requirements

- Python 3.10+
- `openai`
- `pydub`
- `python-docx`
- `ffmpeg-python`

Install dependencies with:
```bash
pip install -r requirements.txt
