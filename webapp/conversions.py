import pypandoc

def convert(sensible_file, output_format):
    content = sensible_file["content"]
    input_format = sensible_file["extension"]
    if output_format in ["odt", "docx", "epub", "epub3", "pdf"]:
        outfile = sensible_file["stem"] + "." + output_format
        pypandoc.convert_text(content, output_format, format=input_format, outputfile=outfile)
        return {"is_file": True, "content": None, "filename": outfile}
    outcountent = pypandoc.convert_text(content, output_format, format=input_format)
    return {"is_file": False, "content": outcontent, "filename": None}
