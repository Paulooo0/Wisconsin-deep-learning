import tensorflow as tf
from tensorflow import keras
from rebuild_dataset import get_data

new_model = tf.keras.models.load_model('neural_model')
new_model.summary()

data = get_data('dataset/rebuilded_cancer_wisconsin.csv')

x = data.drop('diagnosis', axis=1)
y = data['diagnosis']

loss, acc = new_model.evaluate(x, y, verbose=2)
print(f"Model accuracy: {acc*100:.2f}%")