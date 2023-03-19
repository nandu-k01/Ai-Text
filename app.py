import openai
import time
from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')


# replace with your actual API key
openai.api_key = ""

# # loading models
# tfid = pickle.load(open('vectorizer3.pkl', 'rb'))# 
# model = pickle.load(open('model3.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/generate',methods=['POST'])
def generate():
    prompt = request.form['prompt']
    processed_prompt = preprocess_input(prompt)
    response = call_openai_api(processed_prompt)
    return render_template('index.html', output=response)

def call_openai_api(prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
              prompt=prompt,
              max_tokens=1024,
              n=1,
              stop=None,
              temperature=0.7,
            )
            output = response.choices[0].text.strip()
        except Exception as e:
            output =  f"An error occurred: {e}"
        return output    

lemmatizer = WordNetLemmatizer()

# preprocessing input
def preprocess_input(input_text):
    tokens = word_tokenize(input_text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text

if __name__ == '__main__':
     app.run(debug=True)


