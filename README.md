# My Spitch Transcription App

## Initial Setup 🦾
Clone repo and create a virtual environment
```
$ git clone https://github.com/Nalito/My-Spitch-Transcription-App.git
$ cd My-Spitch-Transcription-App
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install -r requirements.txt
```

## Running the Streamlit App 🏗️
```
$ (venv) streamlit run app.py
```
You can go ahead to deploy the application to the Streamlit Community Cloud, just be sure to replace the dummy API key with your own API key in line 9 in [app.py](app.py). *PS. You'll get an Authentication error if you don't do so.*
If you don't have a Spitch API key yet, please head over to [dev.spi-tch.com](https://dev.spi-tch.com) to create a Spitch developer account and access your API key.

The application demo video is available [here](demo_video.mp4)

## More on Spitch 💫
This project was built using the [Spitch](https://spi-tch.com) transcription feature. Spitch is a language company focused on developing small language models for African languages, and as at now, they have currently created models for Yoruba, Igbo, Hausa, and English with more languages coming soon.
In addition to the speech transcription feature, [Spitch](https://spi-tch.com) has also developed three other revolutionalizing features;
1. **Machine Translation**: To convert text in one language to text in another language.
2. **Speech Generation (Text-to-Speech)**: To convert text in one language to audio in the same language.
3. **Tone Marking (Diacritics)**: To format text in one language with the proper intonations.

Head over to the [Playground](https://dev/spi-tch.com) to try it out, and if you're itching to get started coding with our APIs, we have a reliable [documentation](https://docs.spi-tch.com) to get started.
