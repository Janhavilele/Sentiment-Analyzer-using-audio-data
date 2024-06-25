# TransLingual-Sentiment-Analyzer-using-audio-data

Created a model that can do sentiment analysis by taking audio data in english,hindi and marathi.


_**Steps :**_'

**1) Input audio :**
- According to the model that is being described, the input audio consists of the spoken words that are recorded by a microphone that is attached to the user's device and acts as a platform for running the Flask application.
- Users can choose which language they would like to communicate in within the application's interface; the available languages are Hindi, Marathi, and English.After selecting their preferred language, users begin the process by turning on the microphone by clicking a "Process" button.
- After this, the microphone is ready to receive audio input and waits for the user to start speaking.

**2) Speech Recognition:**
- In this part the model tries to understand what the user is speaking . It listens to the user by using a special tool (speech recognition) and sets up a microphone so that it can hear clearly.
- Then the user is asked to select their choice of language. Once the user has selected their choice of language , they can start speaking after clicking on the process button.
- The model then starts listening to the user and after the user has finished it tries to convert the spoken audio into text using Google Speech to text which is the input for the next step.
- If the model does not understand what the user is speaking it displays an error message.

**3) Speech Translation:**
- This step is only needed when the spoken language is marathi or hindi.
- After performing speech recognition on the user spoken language  the model translates the text into english by using the Translator class from googletrans library

**4) Sentiment Analysis:**
- In this step the model wants to understand the overall feelings behind the user words.
- After performing speech recognition and translation the input obtained is fed into a tool called  TextBlob which helps the model to understand the emotions behind the text.
- It calculates sentiment score and based on that score it classifies the text into neutral,negative,positive.
- The sentiment score below zero is known as  negative sentiment , Sentiment score of zero is known as neutral and the sentiment score above zero is known as positive sentiment.
- If your speech expresses some happy or complimentary words then its sentiment score will be above zero and it will be considered as a positive sentence .
- If your speech expresses some frustration or unhappy words then its sentiment score will be below zero and it will be considered as a negative sentence.
- If your speech does not convey any strong emotional tone then its sentiment score will be zero and it will be considered as a neutral sentence .

_**Conclusion:**_

- This model can be helpful to overcoming linguistic barriers by allowing cross-culture communication for sentiment analysis in multilingual communities. 
- The project depicts robust translingual functionalities by predicting and translating sentiments.


