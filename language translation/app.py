from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# Initialize the translator
translator = Translator()

def translate_text(text, src, dest):
    # Translate the text between the chosen languages
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    # Extract the text and languages from the POST request
    text = data.get('text')
    src_lang = data.get('src_lang')
    dest_lang = data.get('dest_lang')

    try:
        # Translate the input text
        translated_text = translate_text(text, src_lang, dest_lang)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        # Handle any errors that occur during translation
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
