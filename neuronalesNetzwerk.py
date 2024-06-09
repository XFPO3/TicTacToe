from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
import numpy as np
import csv
import tensorflow as tf

# Function to read CSV data and convert it into a list
def getCSVtoList(file):
    with open(file, 'r') as f:
        output = list(csv.reader(f, quoting=csv.QUOTE_NONNUMERIC))
    return output

# Function to define the neural network model
def nn_model():
    model = Sequential()
    model.add(Dense(128, input_shape=(9,), kernel_initializer='normal', activation='relu'))
    model.add(Dense(9, kernel_initializer='normal', activation='softmax'))  # Ensure the output layer has 9 units
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Load the data
dataX = getCSVtoList('output.txt')  # Features data
var = getCSVtoList('zug_output.txt')  # Labels data

# Prepare input data
dataY = [int(i[0]) - 1 for i in var]
trainX = np.array(dataX)
trainY = to_categorical(np.array(dataY), num_classes=9)  # Convert labels to one-hot encoded vectors

# Train the model
model = nn_model()
model.summary()

train_dataset = tf.data.Dataset.from_tensor_slices((trainX, trainY))
train_dataset = train_dataset.batch(32).repeat()  # Repeat the dataset infinitely
history = model.fit(trainX, trainY, epochs=250, batch_size=50, verbose=1)

# Save the model
model.save('ai_trained.keras')

# Evaluate the model
figure, axis = plt.subplots(1, 2)

# Plot model accuracy
axis[0].plot(history.history['accuracy'], color='blue', linestyle='-', linewidth=2)
axis[0].set_title('Model Accuracy', fontsize=14)
axis[0].set_ylabel('Accuracy', fontsize=12)
axis[0].set_xlabel('Epoch', fontsize=12)
axis[0].legend(['Training'], loc='upper left')
axis[0].grid(True)

# Plot model loss
axis[1].plot(history.history['loss'], color='red', linestyle='--', linewidth=2)
axis[1].set_title('Model Loss', fontsize=14)
axis[1].set_ylabel('Loss', fontsize=12)
axis[1].set_xlabel('Epoch', fontsize=12)
axis[1].legend(['Training'], loc='upper left')
axis[1].grid(True)

plt.show()
