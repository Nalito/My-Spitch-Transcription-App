# Import the required modules
import streamlit as st
from spitch import Spitch
import os
import tempfile

def transcribe_audio(audio_file, lang):
    # Instantiate a Spitch client
    os.environ["SPITCH_API_KEY"] = "YOUR-API-KEY"
    client = Spitch()

    # Save the uploaded audio file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(audio_file.read()) 
        temp_path = temp_file.name 

    # Transcribe the uploaded audio file to text using the Spitch transcribe function
    with open(temp_path, "rb") as f:
        response = client.speech.transcribe(
            language=lang,
            content=f.read()
        )
    return response.text

def main():
    st.title("My Spitch Transcription App")
    st.write("Upload an audio file to transcribe it to text.")
    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/wav')
        st.write("Select the language of the audio:")
        language = st.selectbox("Language", ["English", "Yoruba", "Igbo", "Hausa"])

        # Encode selected language
        lang = {'English': 'en', 'Yoruba': 'yo', 'Igbo': 'ig'}.get(language, 'ha')

        if st.button("Transcribe"):
            with st.spinner("Transcribing..."):
                transcript = transcribe_audio(audio_file, lang)
                st.success("Transcription completed!")
                st.text_area("Transcript", transcript, height=200)
                
                # Make the transcript downloadable as a txt file
                with open("transcript.txt", "w", encoding="utf-8") as f:
                    f.write(transcript)
                st.download_button("Download Transcript", data=transcript, file_name="transcript.txt", mime="text/plain")

if __name__ == "__main__":
    main()