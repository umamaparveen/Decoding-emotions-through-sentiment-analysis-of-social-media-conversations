from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Store messages in memory
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ''
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = 'Positive 😊'
        elif polarity < 0:
            sentiment = 'Negative 😞'
        else:
            sentiment = 'Neutral 😐'

        # Save to history
        history.append({'text': text, 'sentiment': sentiment})

    return render_template('index_emo.html', sentiment=sentiment, history=history)

if __name__ == '__main__':
    app.run(debug=True)
