from tensorflow import keras
import matplotlib.pyplot as plt
from rebuild_dataset import get_data

data = get_data('dataset/rebuilted_cancer_wisconsin.csv')

x = data.drop('diagnosis', axis=1)
y = data['diagnosis']

def create_sequential_bin(layer1, layer2, layer3, input_dim):
    model = keras.Sequential()
    model.add(keras.layers.Dense(layer1, input_dim=input_dim, activation='relu'))
    model.add(keras.layers.Dense(layer2, activation='relu'))
    model.add(keras.layers.Dense(layer3, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


model = create_sequential_bin(30,10,1, input_dim=30)
fit_model = model.fit(x, y, epochs=100)

accuracy = model.evaluate(x, y, verbose=0)[1]
print(f"Model accuracy: {accuracy*100:.2f}%")

plt.plot(fit_model.history['accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()

model.save('neural_model')