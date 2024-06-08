import os
import uuid
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    original_text = ""
    translated_text = ""
    input_lang = ""
    output_lang = ""
    if request.method == 'POST':
        original_text = request.form['inputText']
        input_lang = request.form['inputLang']
        output_lang = request.form['outputLang']

        if original_text and input_lang and output_lang:
            key = '9257553e89ae411c893a771aabbf5359'
            endpoint = 'https://api.cognitive.microsofttranslator.com/'
            location = 'centralindia'

            path = '/translate?api-version=3.0'
            target_language_parameter = '&to=' + output_lang
            constructed_url = endpoint + path + target_language_parameter

            headers = {
                'Ocp-Apim-Subscription-Key': key,
                'Ocp-Apim-Subscription-Region': location,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }

            body = [{'text': original_text}]
            translator_request = requests.post(constructed_url, headers=headers, json=body)
            translator_response = translator_request.json()
            translated_text = translator_response[0]['translations'][0]['text']
        else:
            translated_text = "Please provide all required inputs."
    return render_template('index.html',original_text=original_text, translated_text=translated_text, input_language=input_lang, output_language=output_lang)

if __name__ == '__main__':
    app.run(debug=True)
