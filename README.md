# Upload to Google Drive with Python using the Drive API

The script was written to upload local files to a specific folder location within Google Drive. There are a number of prequisites for running this script, with the steps as follows:


1. Create a python virtual environment and install the packages in the `requirements_driveapi.txt` file in this repository. You can use `pip install -r requirements_driveapi.txt` to easily install all package requirements once the virtual environment is activated using `source ~/Environments/<virtual_env>/bin/activate`. 

2. Create a project in https://console.cloud.google.com :
- Go to APIs & Services > Enabled APIs and Services and enable the Drive API for this project.
- Go to OAuth Consent Screen within APIs & Services. Select External User Type. Fill in the required fields such as App Name, User Support Email, Developer Contact Information. Don't need to define any scopes as these are defined within the python script itself. Add your Google account as a test user and then return to dashboard.
- Go to credentials and create OAuth client credentials. Select Destop App as the Application Type.  When prompted download the json file containing the credentials to a file called `credentials.json` and save this in the same location as the main python script. 

3. The main function in the python script takes three string arguments: `folder_id`, `file_directory`, `file_ext`. 
- The folder ID can be found by navigating to the desired Drive Folder for uploading to. The folder ID is the string at the end of the URL. (I found it was easier to use this string rather than a method using folder names as the files would upload to any nested folders with this folder name). 
- The file directory is pretty self explanatory - just the path to the files that you want to upload. 
- I added the file extension argument in order to allow uploads of specific file types.

4. Add own folder id, file directory, file extension etc into the main function where it is called at the bottom of the code.

5. Run the script in the terminal (make sure you are in the files directory. If you want to run the file from your home directory you will have to edit the python file to contain the full path to the .json files). 

6. When running for the first time the `token.json` file will not exist so it will allow you to sign in and authenticate. The terminal output contains a link and you will see the OAuth Consent Screen that was configured in the project. Sign in with the Google account you are using (must be defined as a test user) and copy the code that is given. Paste this back into the prompt in the terminal window and the authentication should be complete. Next time you run the script in the terminal it will not ask you to authenticate. 
