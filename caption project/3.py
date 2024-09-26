import random
import nltk
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np
import pickle

# Ensure nltk data is downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Intents dictionary for mental health support
intents = {
    "intents": [
        {"tag": "greeting", "patterns": ["Hi", "Hello", "Hey", "Good day"], "responses": ["Hello! How can I support you today?"]},
        {"tag": "goodbye", "patterns": ["Bye", "Goodbye", "See you"], "responses": ["Take care! Reach out whenever you need support."]},
        {"tag": "depression", "patterns": ["I feel sad", "I'm depressed", "I'm down", "I feel hopeless"], "responses": ["I'm sorry you're feeling this way. Have you tried talking to someone you trust?"]},
        {"tag": "anxiety", "patterns": ["I'm anxious", "I feel nervous", "I'm worried", "I'm feeling overwhelmed"], 
         "responses": ["It's okay to feel anxious. Deep breathing exercises might help."]},
        {"tag": "self-harm", "patterns": ["I want to hurt myself", "I'm thinking about self-harm", "I can't take this anymore"], 
         "responses": ["I'm really sorry you're feeling this way. Please consider talking to a professional or calling a helpline."]},
        {"tag": "encouragement", "patterns": ["I'm feeling hopeless", "I can't do this", "I feel stuck"], 
         "responses": ["You are stronger than you think. Taking one step at a time can help."]},
        {"tag": "general_distress", "patterns": ["I just want to feel better", "I'm struggling with my emotions", "I don't know how to cope"], 
         "responses": ["It's okay to feel this way. Talking about it can really help."]},
        {"tag": "seeking_help", "patterns": ["I need someone to talk to", "Can you help me with my problems?", "I'm feeling lost right now"], 
         "responses": ["I'm here for you. Please share what's on your mind."]}
    ]
}

# Prepare training data
words = []
classes = []
documents = []
ignore_words = ['?', '!']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [nltk.WordNetLemmatizer().lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save words and classes
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Prepare training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [nltk.WordNetLemmatizer().lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Create the model
model = Sequential()
model.add(Dense(128, input_shape=(len(training[0][0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(classes), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Separate training data into x and y
train_x = np.array([x[0] for x in training])
train_y = np.array([x[1] for x in training])

# Train the model
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('mental_health_chatbot.keras')

# Classification functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [nltk.WordNetLemmatizer().lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def classify_local(sentence):
    ERROR_THRESHOLD = 0.25
    p = bow(sentence)
    res = model.predict(np.array([p]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Example usage
sentence = "need for encouragement"
results = classify_local(sentence)
print(results)