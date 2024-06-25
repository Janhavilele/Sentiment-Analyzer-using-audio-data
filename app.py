from flask import Flask, render_template, request
import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob

app = Flask(__name__)

def recognize_speech(language):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"Please start speaking in {language}...")
        audio_input = recognizer.listen(source)
    
    try:
        print("Processing audio...")
        text_output = recognizer.recognize_google(audio_input, language=language)
        return text_output
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error occurred; {e}")
        return ""

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    language = request.form['language']
    speech_text = recognize_speech(language)
    if not speech_text:
        return render_template('index.html', error="Sorry, could not understand audio.")

    translated_text = translate_text(speech_text, language, 'en')
    sentiment = perform_sentiment_analysis(translated_text)

    return render_template('result.html', 
                           speech_text=speech_text,
                           translated_text=translated_text,
                           sentiment=sentiment)
                           
if __name__ == '__main__':
    app.run(debug=False)
