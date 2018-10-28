#coding: utf-8

# this file is for the editorial app (ios) workflow to send a markdown here to convert to pdf. 
import editor, requests, workflow

IP_ADDRESS = "SECRET"  # yeah this is crappy security but who cares? worst case scenario you HAXOR MY PANDOC INSTALLATION 1337 PWNAGE!!!

target= "http://" + IP_ADDRESS + ":8080/mdpdf"

# this comes from workflow actions "get current file name" and then "set variable" (Input to "filename")
filename = workflow.get_variable("filename") + ".pdf"

markdown = editor.get_text(True)

data = {"filename": filename, "markdown": markdown}
response = requests.post(target, data=data)
pdf = response.content
editor.set_file_contents(filename, pdf, 'dropbox')

print('done!')

workflow.stop()