import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

def get_data(path):
    return pd.read_csv(path)
    
path = ('dataset/rebuilded_cancer_wisconsin.csv')
data = get_data(path)

x = data.drop('diagnosis', axis=1)
y = data['diagnosis']

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(5, input_dim=30, activation='relu'))
model.add(tf.keras.layers.Dense(3, activation='relu'))
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