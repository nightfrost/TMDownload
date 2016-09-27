from urllib import request
import json
import os
import sys


# retrieves metadata from file storage
def retrieve_metadata():
    try:
        metadata_url = "" # Insert link to metadata
        request.urlretrieve(metadata_url, "metadata.json")
        # ensure_dir(os_path)
    except Exception as e:
        print("Something went wrong...\n") + print(e)


# Finds download link based on criteria and then downloads the file.
def get_url(isNightly, mv):  # mv = 3.2
    if isNightly == "n":
        latestNightOrRelease = "latestNightly"
        nightOrRelease = "nightlies"
    else:
        latestNightOrRelease = "latestRelease"
        nightOrRelease = "releases"

    with open('metadata.json', 'r') as f:
        data = json.load(f)
        info = data["majorVersions"][mv]
        latestversion = info[latestNightOrRelease]
        url = info[nightOrRelease][latestversion]
        filename = os_path + latestversion + ".zip"
        request.urlretrieve(url, filename)
        print("Download has finished, file is located at: " + filename)


# Ensures that the folder is there, if it is not present it gets created
def ensure_dir(path):
    if os.path.exists(path):
        print("Path exists, no folder will be created")
        return True
    else:
        print("Path: " + path + " Did not exist. Will be created")
        os.makedirs(path)
        return True


os_path = "C:/temp/"
version = ""
isNightly = False
# iterates through sys.argv and adds valid keys to variables.
for arg in sys.argv[1:]:
    if arg[0] is '/':
        switch = arg[1:].lower()

        if switch == "n":
            isNightly = True
        else:
            print("Unknown switch '" + switch + "'")
            exit(3)
    else:
        if version == "":
            version = arg
        else:
            print("Ignoring extra version '" + arg + "'")
            exit(2)

if version == "":
    print("No version")
    exit(1)

retrieve_metadata()
confirmdir = ensure_dir(os_path)
if confirmdir is True:
    get_url("n" if isNightly else "l", version)
else:
    print("Could not start, possibly an issue with directionary")
