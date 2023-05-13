#!/usr/bin/env python3 
#!pip install azure.identity
# Importing the require library
#pip install azure-identity
from azure.common.credentials import ServicePrincipalCredentials
#from azure.mgmt.automation.automation_management_client import AutomationManagementClient
#from azure.mgmt.automation.automation_management_client import AutomationManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.automation import AutomationManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import azure.cognitiveservices.speech as speechsdk
from msrestazure.azure_active_directory import AADTokenCredentials
from tkinter.messagebox import showinfo
from tkinter import filedialog
import azure.mgmt.automation
import azure.mgmt.resource
from azure.identity import InteractiveBrowserCredential
#import automationassets
#from automationassets import AutomationAssetNotFound

# taking care of the InteractiveBrowserCredential()
ibc=InteractiveBrowserCredential()
# taking care of the token
addToken=ibc.get_token("https://cognitiveservices.azure.com/.default")
# Define the Azure Automation account details
CLIENT_ID="e630d5b7-946a-4910-9a42-fb47d07888d4"
TENANT="389e7904-856a-4ac6-baf1-6ffa7374170e"
SECRET="83193e32-1ea2-4fad-9a81-9f5baee94443"

SUBSCRIPTION_ID="017234a8-6f7b-4711-b658-24802bfcb30b"
AUTOMATION_ACCOUNT="lucy999"
RESOURCE_GROUP="script-to-speech"

client_id=CLIENT_ID
secret=SECRET
tenant=TENANT
# setting up the credentials
# Define the credentials to access the Azure Automation API
credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=secret,
    tenant=tenant
)


subscription_id = SUBSCRIPTION_ID
resource_group = RESOURCE_GROUP
automation_account = AUTOMATION_ACCOUNT

# Create the AutomationManagementClient object
client = AutomationManagementClient(credentials, subscription_id)

# Retrieve the credential asset
credential = client.assets.get(resource_group, automation_account, 'CredentialName', 'Certificate')

# Extract the username and password from the credential asset
username = credential.properties['username']
password = credential.properties['password']

# # Get a credential
# cred=automationassets.get_automation_credential("credtest")
# # print to check wheyher the username and pasword are correct
# print(cred["username"])
# print(cred["password"])

# intialized an variable called azure_credential which is an instance of the DefaultAzureCredential
#authenticate  application using multiple authentication methods, including environment variables, managed identities, and user credentials
azure_credential=DefaultAzureCredential(excluded_iteractive_browser_credential=False)


# Importing the require library
import os
import requests
# checking the environment variables
#os.getenv() Python function that is used to retrieve the value of an environment variable
# endpoint=os.getenv('IDENTITY_ENDPOINT')+"?resource=https://management.azure.com/"
# identityHeader=os.getenv('IDENTITY_HEADER')
# # intialized an empty dictionary called payload
# payload={}
# # Initialized another dictionarys name header contain two key value pair
# headers={
#     'X-IDENTITY-HEADER':identityHeader,
#     'Metadata':True
# }
# # taking care of the response
# #a Python method used to send an HTTP GET request to a specified URL and retrieve the response.
# response=requests.get(endpoint,headers)
# print(response.text)


#create Python Compute client and start the virtual machine
# Initialized the client with the credential and subscriptions.
# compute_client=ComputeManagementClient(
#     azure_credential,
#     SUBSCRIPTION_ID
# )
# # print to check when we start our virtual machine
# print('\nStart virtual machine')
# async_vm_start=compute_client.virtual_machines("MyResourceGroup","TestVM")
# #The "wait" method is used to block the program execution until the asynchronous operation is completed. Once the operation is completed, the program can continue with the next instruction. 
# async_vm_start.wait()
# print('\nFinished start.')

# Creating another function to choose the text file
def chooseText():

    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )
    #the filedialog module from tkinter to open a file dialog box and allows the user to select a text file. It then reads in the text from the selected file and returns it as a string.
    filename = filedialog.askopenfilename(
        title = 'Please select a text file',
        filetypes = filetypes)
    # read in text from the select file
    with open(filename,encoding='utf-8') as file:
        text=file.read()
    
    # we suppose some information
    showinfo(
        title = 'Selected File: ',
        message = filename
    )

    return text

#choosing the text file we want
text=chooseText()
# AUTHENTICATION
# using the Subscription ID
# set subscription key and region
subscription_key=azure_credential.get_token("https://eastus.api.cognitive.microsoft.com/").token
SUBSCRIPTION_ID="017234a8-6f7b-4711-b658-24802bfcb30b"
REGION="eastus"

# defining the main function
def main():
    subscription_key="44050913e67a4750b8195c793312d74d"
    region=REGION
    # set audio file format and output file name
    audio_config=speechsdk.audio.PushAudioOutputConfig(use_default_speaker=True)
    # setting the file_name
    file_name='output.mp3'

    # next, we are creating a speech synthesizer object with subscription key and regon
    speech_config=speechsdk.SpeechConfig(subscription=subscription_key,region=region)
    # setting up 
    synthesizer=speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)
    # generate audio from text and save it to an output 
    result=synthesizer.speak_text_async(text).get()
    # next we need an if statement to check whether the file is generated, if not
    # we will print out there is error
    if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
        with open(file_name,'wb') as file:
            file.write(result.audio_data)
        print("Audio file created:{}".format(file_name))
    else:
        print("There is an error")
    # if file is generated, we will print out success
    # url="https://{}.tts.speech.microsoft.com/cognitiveservices/v1".format(region)
    # header={
    #     "Ocp-Apim-Subscription-Key": subscription_key,
    #     "Content-Type":"text",
    #     "X-Microsoft-OutputFormat": "audio-48khz-192kbitrate-mono-mp3"



    # }
    
    #with
    # Code for taking care of the automation
    # Creating two global variable
    # One for the speech key
    subscription_key=SUBSCRIPTION_ID
    # Another one is for the region
    region=REGION
    
    # Replace with your own text and file name
    # text=chooseText()
    # file_name='result.wav'

    # # Creating a speech config object with subsubscription key and region
    # speech_config=speechsdk.SpeechConfig(subscription=subscription_key,region=region)
    # #Create a synthesizer object and specify and desired audio format
    # synthesizer=speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=speechsdk.audio.AudioOutputConfig(filename=file_name))
    # # Generate the audio from text
    # result=synthesizer.speak_text_async(text).get()
    # if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    #     print("Audio file created:{}".format(file_name))
    # else:
    #     print(azure_credential)
    #     print("There is an error")
    # we also need one varibale to store the url
    # url="https://{}.tts.speech.microsoft.com/cognitiveservies/v1".format(region)
    # # another variable called header, which is an dictionary
    # headers={
    #     "Ocp-Apim-Subscription-Key":subscription_key,
    #     "Content-Type":"application/ssml+xml",
    #     "X-Microsoft-OutputFormat":"audio-48khz-192kbitrate-mono-mp2"
    # }

    # # we need to open the file we need to convert into speech
    # with open("./sample/path/my_pitch.ssml") as file:
    #     ssml=file.readlines()
    # ssml=" ".join(ssml)
    # ssml=ssml.encode('utf-8')
    # # getting the response
    # response=requests.post(url=url,data=ssml,headers=headers)

    # # open the mp3 file we just generated
    # with open("output.mp3","wb") as f:
    #     f.write(response.content)

if __name__=="__main__":
    
    main()