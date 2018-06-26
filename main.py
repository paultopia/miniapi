from flask import Flask, send_file
import pypandoc, uuid, os, glob

app = Flask(__name__)

testmd = '''
# Hello Paul!

You should check out [your own webpage](https://gowder.io)!
'''

testhtml = pypandoc.convert_text(testmd, 'html', format='md')


@app.route("/")
def hello():
    return pypandoc.convert_file("test.md", "html")

# let's try making a pdf now.

def clear_pdf_directory():
    files = glob.glob('temp_pdfs/*')
    for f in files:
        os.remove(f)

def make_pdf(markdown):
    clear_pdf_directory()
    filename = "temp_pdfs/" + str(uuid.uuid1()) + ".pdf"
    pypandoc.convert_text(markdown, "pdf", format="md", outputfile=filename)
    return filename

@app.route("/pdf")
def pdf():
    with open("test.md") as md:
        filename = make_pdf(md.read())
    return send_file(filename, attachment_filename=filename)



if __name__ == "__main__":
    app.run()
