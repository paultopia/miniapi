from flask import Flask, send_file, request
import pypandoc, json
from filehandling import make_files_sensible

import os, sys, json
from flask_heroku import Heroku
app = Flask(__name__)
heroku = Heroku(app)

testmd = '''
# Hello Paul!

You should check out [your own webpage](https://gowder.io)!
'''

testhtml = pypandoc.convert_text(testmd, 'html', format='md')


@app.route("/")
def roottest():
    return pypandoc.convert_file("test.md", "html")


@app.route("/testflask")
def testflask():
    return "flask works, and so does heroku push from ipad."

# let's try making a pdf now.

def make_pdf(markdown):
    pypandoc.convert_text(markdown, "pdf", format="md", outputfile="output.pdf")
    return True

@app.route("/pdf")
def pdf():
    with open("test.md") as md:
        make_pdf(md.read())
    return send_file("output.pdf", attachment_filename="output.pdf")

def get_request_info():
    args = str(request.args)
    form = str(request.form)
    files = str(request.files)
    maybe_json = request.get_json(silent=True, cache=False)
    if maybe_json:
        thejson = json.dumps(maybe_json)
    else:
        thejson = "no json"
    output = "args: \n\n " + args + "\n\n form: \n\n" + form + "\n\n files: \n\n" + files + "\n\njson: \n\n" + thejson
    return output

@app.route("/seerequest", methods=['GET', 'POST'])
def seerequest():
    return get_request_info()

def find_md_file(filesdict):
    for k, v in filesdict.items():
        if v.filename.endswith(".md"):
            return v
    return None

def grab_first_md_file():
    fls = request.files
    if fls:
        return find_md_file(fls)
    return None

@app.route("/mdfile", methods=['POST'])
def mdfile():
    themd = grab_first_md_file()
    if themd:
        mdtext = themd.read()
        return mdtext
    return "no markdown file"


@app.route("/firstfile", methods=['POST'])
def firstfile():
    fls = request.files
    if fls:
        thefile = list(fls.items())[0][1]
        thefilename = thefile.filename
        filecontent = thefile.read()
        # werkzeug refuses to document what type any of the stuff returned from the FileStorage object is so we have to do this bullshit.
        try:
            content = filecontent.decode("utf-8")
        except:
            content = filecontent
        try:
            filename = thefilename.decode("utf-8")
        except:
            filename = thefilename
        return filename + "\n\n" + content
    return "no file"

@app.route("/allfiles", methods=["POST"])
def allfiles():
    fls = request.files
    if fls:
        incoming_files = make_files_sensible(fls)
        return json.dumps(incoming_files, indent=4, sort_keys=True)
    return "no files"

###############################################################


## the actual useful bits

def make_named_pdf(markdown, filename):
    pypandoc.convert_text(markdown, "pdf", format="md", outputfile=filename)
    return True

@app.route("/mdpdf", methods=['GET', 'POST'])
def mdpdf():
    if request.method == 'GET':
        return "the endpoint is findable, now send a post request"
    filename = request.form["filename"]
    markdown = request.form["markdown"]
    make_named_pdf(markdown, filename)
    return send_file(filename, attachment_filename=filename)

def make_named_docx(markdown, filename):
    pypandoc.convert_text(markdown, "docx", format="md", outputfile=filename)
    return True

@app.route("/mddocx", methods=['GET', 'POST'])
def mddocx():
    if request.method == 'GET':
        return "the endpoint is findable, now send a post request"
    filename = request.form["filename"]
    markdown = request.form["markdown"]
    make_named_docx(markdown, filename)
    return send_file(filename, attachment_filename=filename)



if __name__ == "__main__":
    app.run()
