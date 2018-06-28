import dropbox
import os
import sys

MY_ACCESS_TOKEN=os.environ['DROPBOX_ACCESS_TOKEN']
INTERVIEW_DIRECTORY='/Everyone/Interviewing/interviews'

dbx = dropbox.Dropbox(MY_ACCESS_TOKEN)

autoMode = len(sys.argv) > 1

if not autoMode:
    interviewee = input("What is the name of the candidate?\n")
else:
    interviewee = sys.argv[1]

folder_name = interviewee.replace(' ', '-').lower()
file_request_title = "Technical Interview - {}".format(interviewee)
folder_path = os.path.join(INTERVIEW_DIRECTORY, folder_name)
existing_folder = None

if not autoMode:
    input("\nCreating folder: {}\nCreating file request: {}\nPress enter to continue. ".format(folder_path, file_request_title))

try:
    existing_folder = dbx.files_get_metadata(folder_path)
except dropbox.exceptions.ApiError as e:
    # Folder doesn't exist, create it
    if type(e.error) is dropbox.files.GetMetadataError and e.error.get_path().is_not_found():
        dbx.files_create_folder(folder_path)
    else:
        print("\nUnhandled exception {}".format(e))
        quit()

if existing_folder is not None and not autoMode:
    use_existing = input("\nExisting folder named {} found. Do you want to use this folder and continue? (y/n) ".format(existing_folder.name))
    if use_existing.lower()[0] == 'n':
        quit()

file_request = dbx.file_requests_create(file_request_title, folder_path)

print("\nFile request created: \n{}".format(file_request.url))

