import pypandoc
from filehandling import extension

def addargs(output_format):
    if output_format == "pdf":
        return ["--pdf-engine=xelatex"]
    return []

def base_conversion(content, output_format, input_format, outfile):
    if output_format in ["odt", "docx", "epub", "epub3", "pdf"]:
        pypandoc.convert_text(content, output_format, format=input_format, outputfile=outfile, extra_args = addargs(output_format))
        return {"is_file": True, "content": None, "filename": outfile}
    outcontent = pypandoc.convert_text(content, output_format, format=input_format, extra_args = addargs(output_format))
    return {"is_file": False, "content": outcontent, "filename": None}


def convert_file(sensible_file, output_format):
    content = sensible_file["content"]
    input_format = sensible_file["extension"]
    outfile = sensible_file["stem"] + "." + output_format
    return base_conversion(content, output_format, input_format, outfile)


def convert_text(content, input_format, outfile):
    output_format = extension(outfile)
    return base_conversion(content, output_format, input_format, outfile)
