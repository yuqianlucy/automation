#!/usr/bin/env python3 
#!pip install azure.identity
# Importing the require library
#pip install azure-identity
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# using the Subscription ID
SUBSCRIPTION_ID="017234a8-6f7b-4711-b658-24802bfcb30b"

# intialized an variable called azure_credential which is an instance of the DefaultAzureCredential
#authenticate  application using multiple authentication methods, including environment variables, managed identities, and user credentials
azure_credential=DefaultAzureCredential()

# Importing the require library
import os
import requests
# checking the environment variables
#os.getenv() Python function that is used to retrieve the value of an environment variable
endpoint=os.getenv('IDENTITY_ENDPOINT')+"?resource=https://management.azure.com/"
identityHeader=os.getenv('IDENTITY_HEADER')
# intialized an empty dictionary called payload
payload={}
# Initialized another dictionarys name header contain two key value pair
headers={
    'X-IDENTITY-HEADER':identityHeader,
    'Metadata':True
}
# taking care of the response
#a Python method used to send an HTTP GET request to a specified URL and retrieve the response.
response=requests.get(endpoint,headers)
print(response.text)


#create Python Compute client and start the virtual machine
# Initialized the client with the credential and subscriptions.
compute_client=ComputeManagementClient(
    azure_credential,
    SUBSCRIPTION_ID
)
# print to check when we start our virtual machine
print('\nStart virtual machine')
async_vm_start=compute_client.virtual_machines("MyResourceGroup","TestVM")
#The "wait" method is used to block the program execution until the asynchronous operation is completed. Once the operation is completed, the program can continue with the next instruction. 
async_vm_start.wait()
print('\nFinished start.')

# defining the main function
def main():
    pass

if __name__=="__main__":
    main()