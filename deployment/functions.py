import pickle
from tensorflow import keras
import numpy as np
import nltk
import random
import json
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

def getAISymptomsResponse(symptom_sentence: str):
    nltk.download('punkt')
    interpreter = tf.lite.Interpreter(model_path="symptom_checker_model.tflite")
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    with open('symptom_varsV1.pickle', 'rb') as f:
        disease_labels, symptom_to_idx, max_length = pickle.load(f)

    data= pd.read_csv('disease_sympts_prec_full.csv')

    symptoms = word_tokenize(symptom_sentence.lower())
    tokenized_symptoms = [symptom_to_idx.get(token, 0) for token in word_tokenize(' '.join(symptoms).lower())]
    padded_symptoms = pad_sequences([tokenized_symptoms], maxlen=max_length)
    input_tensor = np.array(padded_symptoms, dtype=np.float32)


    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_tensor)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_index = np.argmax(output_data[0])
    predicted_disease = disease_labels[predicted_index]

    # Print the predicted disease
    print(f"Predicted disease: {predicted_disease}")
    precautions = data[data['disease'] == predicted_disease]['precautions'].iloc[0]
    print(f"Precautions: {precautions}")
    
    return {
            'message': f"Based on the symptoms you provided, you may have {predicted_disease}. Here are some precautions you can take: {precautions}"
    }

def getChatResponse(message: str):
    nltk.download('punkt')
    nltk.download('wordnet')
    with open('dataV1.pickle', 'rb') as f:
        words, classes, training, output = pickle.load(f)
    model= keras.models.load_model('chatbot_modelV1.h5')
    intents= json.loads(open(r"chatbot_dataset_generalV1.json").read())
    word_index = {word: index for index, word in enumerate(words)}
    max_length = max(len(doc) for doc in training)

    input_vector = bag_of_words(nltk.word_tokenize(message), word_index, max_length)
    results = model.predict(np.array([input_vector]))[0]
    results_index = np.argmax(results)
    tag = classes[results_index]

    for tg in intents['intents']:
        if tg['tag'] == tag:
            responses = tg['responses']
    return {
        'message': random.choice(responses)
    }

def bag_of_words(s, words, max_length): 
    bag = [0 for _ in range(len(words))]
    lemmatizer= nltk.stem.WordNetLemmatizer()
    word_index = {word: index for index, word in enumerate(words)}

    word_indices = [word_index.get(lemmatizer.lemmatize(word.lower()), len(word_index)) for word in s]
    padded_indices = sequence.pad_sequences([word_indices], maxlen=max_length, padding='post')[0]
    return padded_indices