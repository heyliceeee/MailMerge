import os
OUTPUT_FOLDER_PATH = "/Output"
READY_TO_SEND_FOLDER_PATH = "/ReadyToSend"
PLACEHOLDER = "[name]"

all_invented_names = []
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file
output_folder_absolute_path = dir_path + OUTPUT_FOLDER_PATH # absolute path of the Output folder
ready_to_send_folder_absolute_path = output_folder_absolute_path + READY_TO_SEND_FOLDER_PATH # absolute path of the ReadyToSend folder

def create_folders():
    """
    create the folders: Output/ReadyToSend
    """
    if not os.path.exists(output_folder_absolute_path): # check if the Output folder not exists
        os.makedirs(output_folder_absolute_path) # create the Output folder
        print(f"created folder: {OUTPUT_FOLDER_PATH}")

    if not os.path.exists(ready_to_send_folder_absolute_path): # check if the ReadyToSend folder not exists
        os.makedirs(ready_to_send_folder_absolute_path)  # create the ReadyToSend folder
        print(f"created folder: {READY_TO_SEND_FOLDER_PATH}")
def get_names_from_file():
    """
    get names from the invented_names.txt
    :return: list of names
    """
    file_path = dir_path + "/Input/Names/invited_names.txt"
    with open(file_path, "r") as file:
        return file.readlines()
def get_letter_from_file():
    """
        get a letter from the starting_letter.txt
        :return: letter
    """
    file_path = dir_path + "/Input/Letters/starting_letter.txt"
    with open(file_path, "r") as file:
        return file.read()
def create_letter_file(name):
    """
    create the letter to the file
    :param name: invented name
    """
    file_path = ready_to_send_folder_absolute_path + "/letter_for_" + name + ".txt" # absolute path of the letter file
    with open(file_path, "w") as file:
        file.write(letter.replace(PLACEHOLDER, name)) # replace the [name] placeholder with the invented name
    print(f"created letter file: {file_path}")
def save_letters():
    """
    save the letters in the ReadyToSend folder
    """
    for name in all_invented_names: # for each name in the invented_names.txt
        create_letter_file(name) # create the letter


create_folders() # create the folders: Output/ReadyToSend
all_invented_names = [name.strip() for name in get_names_from_file()] # remove the \n from the names from the invented_names.txt
letter = get_letter_from_file() # get the letter from the starting_letter.txt
save_letters() # save the letters in the ReadyToSend folder