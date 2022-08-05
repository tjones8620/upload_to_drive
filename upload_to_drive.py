import os
import os.path

from google.auth.transport.requests import Request 
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Want to specify scope - what the script will do 
SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_creds():
    creds = None
    # Checks if a token exists:
    # Loads creds if token already exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no creds or creds not valid 
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else: 
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def main(folder_id, file_directory, file_ext):
    
    creds = get_creds()
    
    try:
        # Builds the drive service
        service = build("drive", "v3", credentials=creds)

        # Looks for all files in chosen directory
        # that end with the desired extension.
        for file in os.listdir(f"{file_directory}"):
            if file.endswith(f"{file_ext}"):
                # Create the request metatdata, letting 
                # Drive API know what it's receiving.
                file_metadata = {
                    "name": file,
                    "parents": [folder_id]
                }
                # Uploads desired file(s) to specified Drive folder
                media = MediaFileUpload(f"{file_directory}/{file}")
                upload_file = service.files().create(body=file_metadata, 
                                                    media_body=media, 
                                                    fields="id").execute()
                print("Backed up file: " + file)

    except HttpError as e:
        print('Error:' + str(e))

if __name__ == "__main__":
    main()

