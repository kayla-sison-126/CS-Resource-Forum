# database simuation:
# saves submissions to a JSON file

import json
import os # we need this to check if certain files exist

DATA_FILE = 'data/submissions.json' # save the name of the data file for easy use

def save_submission(name, email): # function that saves data to the file
    try:
        if not os.path.exists(DATA_FILE): # if file DNE yet,
            with open(DATA_FILE, 'w') as f: # create file (open in Write mode)
                json.dump([], f)            # init file with empty JSON array ([])

        with open(DATA_FILE, 'r') as f: # open file in Read mode
            data = json.load(f)         # store data from JSON file into a list called data

        data.append({"name": name, "email": email}) # append new submission to list

        with open(DATA_FILE, 'w') as f: # open file again in Write mode
            json.dump(data, f, indent=2) # dump the whole list back into the JSON file

        return True
    except Exception as e: # if any error occurs during the operations above,
        print(f"Error saving submission: {e}") # print error msg
        return False
