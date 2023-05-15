import os
import azure.cognitiveservices.speech as speechsdk
from tkinter.messagebox import showinfo
from tkinter import filedialog

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='zh-CN-XiaoxiaoNeural'
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

# Set the filename and format for the output audip file
# output_format=speechsdk.audio.AudioOutputStream('MP3')
# output_filename='output.mp3'
# output_stream = speechsdk.PullAudioOutputStream(speechsdk.AudioStreamFormat(encoding=speechsdk.AudioStreamContainerFormat.MP3))
# with open(output_filename, 'wb') as file:
#     output_stream.write = lambda b: file.write(b)
#output_stream = speechsdk.audio.PushAudioOutputStream.create_file(output_format, output_filename)
# Create an AudioFileOutputConfig object with the desired filename and format
# audio_config=speechsdk.audio.AudioOutputConfig(output_filename,output_format)
# # Synthesize the text and save the audio output to the specifiec file
# result=speech_synthesizer.speak_text_async(text,audio_config=audio_config).get()
# # # printing out the result
# # print("Speech synthesized for text [{}]".format(text))
# set audio file format and utput file name
audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
# setting the file name
file_name='output.mp3'
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
# next, we need an if statement to check whether the file is generated,if not
# we will print out there is an error
if speech_synthesis_result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    with open(file_name,'wb') as file:
        file.write(speech_synthesis_result.audio_data)
    print("Audio file created:{}".format(file_name))
else:
    print("There is an error")


# # next we need an if statement to check whether the file is generated, if not
# # we will print out there is error
# if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
#         with open(output_filename,'wb') as file:
#             file.write(result.audio_data)
#         print("Audio file created:{}".format(output_filename))
# else:
#         print("There is an error")




# speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()


# if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized for text [{}]".format(text))
# elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = speech_synthesis_result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")