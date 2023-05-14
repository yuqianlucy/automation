#!/usr/bin/env python3

# Importing the require library
import os
import json
import requests
import azure.cognitiveservices.speech as speechsdk
from tkinter.messagebox import showinfo
from tkinter import filedialog
from azure.identity import DefaultAzureCredential
from azure.cognitiveservices.speech import AudioDataStream

#Read the Azure credentials from the config file
with open('config.json','r') as f:
    config=json.load(f)



# setting up the variables
client_id=config['client_id']
client_secret=config['client_secret']
tenant_id=config['tenant_id']
# Setting up the Azure credentials
azure_credential = DefaultAzureCredential()

# Set subscription key and region
subscription_key = azure_credential.get_token("https://eastus.api.cognitive.microsoft.com/.default").token
REGION = "eastus"

# Create a speech synthesizer using the Cognitive Services Text-to-Speech API
speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=REGION)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Define a function to choose the text file
def chooseText():
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )
    # Use the filedialog module from tkinter to open a file dialog box and allow the user to select a text file.
    # Then read in the text from the selected file and return it as a string.
    filename = filedialog.askopenfilename(
        title='Please select a text file',
        filetypes=filetypes)
    with open(filename, encoding='utf-8') as file:
        text = file.read()

    # Display the selected file information
    showinfo(
        title='Selected File:',
        message=filename
    )

    return text

# Choose the text file
text = chooseText()

# Synthesize speech from the text
result = speech_synthesizer.speak_text_async(text).get()

# Save the synthesized speech to a .wav file
with open('output.mp3', 'wb') as audio_file:
    audio_data_mp3=result.audio_data
    audio_data_mp3=speechsdk.AudioDataStream.convert_to_mp3(audio_data_mp3)
    audio_file.write(audio_data_mp3)
