from flask import Flask
import pypandoc

app = Flask(__name__)

testmd = '''
# Hello Paul!

You should check out [your own webpage](https://gowder.io)!
'''

testhtml = pypandoc.convert_text(testmd, 'html', format='md')


@app.route("/")
def hello():
    return pypandoc.convert_file("test.md", "html")

if __name__ == "__main__":
    app.run()
