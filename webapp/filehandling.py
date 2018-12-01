import pathlib
from collections import ChainMap

def extension(filename):
    return pathlib.Path(filename).suffix.replace(".", "")

def stem(filename):
    return pathlib.Path(filename).stem

def sort_out_file(filetuple):
    try:
        formname = filetuple[0].decode("utf-8")
    except:
        formname = filetuple[0]
    file_object = filetuple[1]
    fn = file_object.filename
    try:
        filename = fn.decode("utf-8")
    except:
        filename = fn
    fc = file_object.read()
    try:
        filecontent = fc.decode("utf-8")
    except:
        filecontent = fc
    return {"filename": filename,
            "content": filecontent,
            "stem": stem(filename),
            "extension": extension(filename),
            "formnane": formname}

def make_files_sensible(flask_files_dict):
    filelist = {k: sort_out_file((k, v)) for k, v in flask_files_dict.items()}
    return filelist

# {k:v for d in filelist for k, v in d.items()}  # just flatten the list of dicts
