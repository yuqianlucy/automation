import os
import azure.cognitiveservices.speech as speechsdk
from tkinter.messagebox import showinfo
from tkinter import filedialog

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
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
#text = input()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")