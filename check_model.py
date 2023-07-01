from tensorflow import keras
from rebuild_dataset import get_data

def check(path):
    model = keras.models.load_model(path)
    model.summary()

    data = get_data('dataset/rebuilted_cancer_wisconsin.csv')

    x = data.drop('diagnosis', axis=1)
    y = data['diagnosis']

    loss, acc = model.evaluate(x, y, verbose=2)
    print(f"Model accuracy: {acc*100:.2f}%")
    

if __name__ == '__main__':
    check('neural_model')