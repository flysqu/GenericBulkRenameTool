import os

def search_and_replace(search, replace, filename):
    output = filename.replace(search, replace)

    return output

def remove_characters(froom, to, filename):
    # CHECK IF POSITION IS SAME AS "END" MAKE POSITION THE SAME AS LENGHT OF FILENAME
    if froom == 0 or to == 0:
        return filename

    output = filename[:froom-1] + filename[to:]
    return output

def insert_text(text, position, filename):
    # CHECK IF POSITION IS SAME AS "END" MAKE POSITION THE SAME AS LENGHT OF FILENAME

    output = filename[:position] + text + filename[position:]

    return output

def list_files(path):
    files = os.listdir(path) 
    files = [f for f in files if os.path.isfile(path+'/'+f)]

    return files