import machinetranslation as mt
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = mt.translator.englishToFrench(textToTranslate)
    return translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = mt.translator.frenchToEnglish(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
