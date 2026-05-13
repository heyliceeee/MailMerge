import os
OUTPUT_FOLDER_PATH = "/Output"
READY_TO_SEND_FOLDER_PATH = "/ReadyToSend"

# 2. create the letters using starting_letter.txt
# 3. replace the [name] placeholder with each name in invented_names.txt
# 4. save the letters in the ReadyToSend folder


def create_folders():
    """
    create the folders: Output/ReadyToSend
    """
    dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file
    output_folder_absolute_path = dir_path + OUTPUT_FOLDER_PATH # absolute path of the Output folder
    ready_to_send_folder_absolute_path = output_folder_absolute_path + READY_TO_SEND_FOLDER_PATH # absolute path of the ReadyToSend folder

    if not os.path.exists(output_folder_absolute_path): # check if the Output folder not exists
        os.makedirs(output_folder_absolute_path) # create the Output folder
        print(f"created folder: {OUTPUT_FOLDER_PATH}")

    if not os.path.exists(ready_to_send_folder_absolute_path): # check if the ReadyToSend folder not exists
        os.makedirs(ready_to_send_folder_absolute_path)  # create the ReadyToSend folder
        print(f"created folder: {READY_TO_SEND_FOLDER_PATH}")

# Output
#   ReadyToSend
#       letter_for_Alice.txt
#       letter_for_Bob.txt
#       ...


create_folders() # create the folders: Output/ReadyToSend