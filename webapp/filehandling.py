import pathlib

def extension(filename):
    return pathlib.Path(filename).suffix

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
    return {formname: {"filename": filename,
                       "content": filecontent,
                       "stem": stem(filename),
                       "extension": extension(filename),
                       "formnane": formname}}

def make_files_sensible(flask_files_dict):
    output = [sort_out_file((k, v)) for k, v in flask_files_dict.items()]
    return output
