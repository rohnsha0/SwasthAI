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
import string


def getSymptomPredictionResponse(symptom_sentence: str):
    nltk.download('punkt')
    interpreter = tf.lite.Interpreter(model_path="diseasePredV1.tflite")
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    with open("nextSymptomData.pickle", "rb") as f:
        word_to_index, max_seq_len = pickle.load(f)
    sequence = symptom_sentence.lower()
    tokenized_sequence = nltk.word_tokenize(sequence)
    sequence_indices = [word_to_index.get(word, 0) for word in tokenized_sequence]
    padded_sequence = pad_sequences([sequence_indices], maxlen=max_seq_len, dtype='float32')

    interpreter.set_tensor(input_details[0]['index'], padded_sequence)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Find the index of the highest probability
    next_symptom_index = np.argmax(output_data[0])

    # Reverse the mapping to get the symptom word
    next_symptom_word = list(word_to_index.keys())[list(word_to_index.values()).index(next_symptom_index)]

    print("Given the sequence: ", symptom_sentence)
    print("The predicted next symptom is: ", next_symptom_word)
    return {
        "message": next_symptom_word,
    }

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

def getChatResponse(prompt: str):
    nltk.download('punkt')
    nltk.download('wordnet')
    with open('dataV3.pickle', 'rb') as f:
        word_index, classes, max_length = pickle.load(f)
    interpreter = tf.lite.Interpreter(model_path='chatV3.tflite')
    interpreter.allocate_tensors()

# Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    intents= json.loads(open(r"chatbot_dataset_generalV1.json").read())
    input_vector = bag_of_words(nltk.word_tokenize(prompt), word_index, max_length)
    input_vector = np.array([input_vector], dtype=np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_vector)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    results_index = np.argmax(output_data[0])
    tag = classes[results_index]

    for tg in intents['intents']:
        if tg['tag'] == tag:
            responses = tg['responses']
            print(random.choice(responses))
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