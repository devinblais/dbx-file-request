# Dropbox File Request

Use this script to quickly create a dropbox file request for technical interviews

## Initial Setup
1. Create a new dropbox app by visiting https://www.dropbox.com/developers/apps and clicking on the 'Create App' button. On the next screen select 'Dropbox API', then 'Full dropbox', and name it something amazing (but unique).
2. Once your app is created, create an access token by following the steps here: https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/
3. Update `MY_ACCESS_TOKEN` in create_request.py to your new access token.
4. Run `pip install dropbox`

## Usage
Run `python create_request.py` and follow the prompts
