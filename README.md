# My Spitch Transcription App

## Initial Setup:
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

## Streamlit App
```
$ (venv) streamlit run app.py
```
You can go ahead to deploy the application to the Streamlit Community Cloud, just be sure to replace the dummy API key with your own API key in line 9 in [app.py](app.py).
If you don't have a Spitch API key yet, please head over to [dev.spi-tch.com](https://dev.spi-tch.com) to create a Spitch developer account and access your API key.

The application demo video is available [here](demo_video.py)
