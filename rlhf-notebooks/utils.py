from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

def authenticate():
    #return "DLAI_CREDENTIALS", "DLAI_PROJECT_ID"
    # Path to the json key associated with your service account from google cloud
    key_path = '../.env/llmops-462607-305d3f0929d9.json'
    # Create credentials from service account file
    credentials = Credentials.from_service_account_file(
        key_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    if credentials.expired:
        credentials.refresh(Request())
    
    #Set project ID according to environment variable    
    PROJECT_ID = "llmops-462607"
    STAGING_BUCKET = "llm-ft-bucket"
        
    return credentials, PROJECT_ID, STAGING_BUCKET

def print_d(d, indent=0):
    for key, val in d.items():
        indentation = "  " * indent
        print(f"{indentation}" + "-"*50)
        print(f"{indentation}key:{key}\n")
        if isinstance(val, dict):
            print(f"{indentation}val")
            print_d(val,indent=indent+1)
        else:
            print(f"{indentation}val:{val}")