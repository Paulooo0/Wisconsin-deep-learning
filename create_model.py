import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from rebuild_dataset import get_data

data = get_data('dataset/rebuilded_cancer_wisconsin.csv')

x = data.drop('diagnosis', axis=1)
y = data['diagnosis']

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(30, input_dim=30, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x, y, epochs=100)

accuracy = model.evaluate(x, y, verbose=0)[1]
print(f"Model accuracy: {accuracy*100:.2f}%")

plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()

model.save('neural_model')
