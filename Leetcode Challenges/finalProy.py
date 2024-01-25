# TensorFlow y tf.keras
import tensorflow as tf
from tensorflow import keras

# Librerias de ayuda
import numpy as np
import matplotlib.pyplot as plt

# Imprime la versión de TensorFlow
print(tf.__version__)

# Importa datasets de moda  de MNIST (4 arreglos Numpy)
# El arreglo train_images y train_labels son los arreglos que training set—el modelo de datos usa para aprender.
#  el modelo es probado contra los arreglos test set, el test_images, y test_labels.
# Las imagenes son 28x28 arreglos de NumPy, con valores de pixel que varian de 0 a 255.
#  Los labels son un arreglo de integros, que van del 0 al 9. Estos corresponden a la class de ropa que la imagen representa.

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

# Los Class names no están incluidos en el dataset, almacénelos acá para usarlos luego cuando se visualicen las imágenes:
class_names = ['Playera', 'Pantalon', 'Jersey', 'Vestido', 'Camisa',
               'Sandalia', 'Shirt', 'Sneaker', 'Bolso', 'Botín']

# Se realiza una exploración del dataset. Hay 60k de imágenes en el set de entrenamiento.
# Cada imagen representada por píxeles de 28x28

# Muestra la forma de las imágenes de entrenamiento
train_images.shape

# Muestra el número de etiquetas en el set de entrenamiento y algunas etiquetas.
len(train_labels)
# Hay 60k de etiquetas en el set de entrenamiento. Cada etiqueta es un entero entre 0 y 9
train_labels

# Muestra el número de imágenes en el set de prueba.
test_images.shape

# Muestra el número de etiquetas en el set de prueba.
len(test_labels)

# Se genera un plot para ver la composición de cada imagen.
# El set de datos tiene que ser pre-procesado antes de entrenar la red porque en el set de entrenamiento,

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# Los valores de los píxeles van de 0 a 255. Lo que tenemos que hacer es escalar los valores antes de alimentarlos al modelo de
#  red neuronal.

train_images = train_images / 255.0
test_images = test_images / 255.0

# Para verificar que el set de datos está en el formato adecuado y que están listos para construir y entrenar la red,
# vamos a desplegar las primeras 25 imágenes de el training set y despleguemos el nombre de cada clase debajo de cada imagen.

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# El primer paso de la construcción del modelo es la configuración de las capas. Lo que hacen las capas es extraer
# representaciones de los datos. Si tenemos suerte, estas muestras o extracciones son representativas o respresentaciones
# considerables de los datos y nos sirven para hacer predicciones

# 1) La capa tf.keras.layers.Flatten, transforma el formato de las imágenes de un arreglo bi-dimensional (de 28 por 28 píxeles)
# a un arreglo uni-dimensional (de 28*28 píxeles = 784 píxeles).
# Observe esta capa como una capa no apilada de filas de píxeles en la misma imagen y alineándolos.
# Esta capa no tiene parámetros que aprender, solamente reformatea el set de datos.

# 2) y 3) Después de que los píxeles están "aplanados", la secuencia consiste de dos capas tf.keras.layers.Dense.
# Estas están densamente conectadas, o completamente conectadas.
# La primera capa Dense tiene 128 nodos (o neuronas).
# La segunda (y última) capa es una capa de 10 nodos softmax que devuelve un arreglo de 10 probabilidades que suman a 1.
# Cada nodo contiene una calificación que indica la probabilidad que la actual imagen pertenezca a una de las 10 clases.

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# El siguiente paso es la compilación del modelo.
# Antes de que el modelo esté listo para entrenar, se necesitan algunas configuraciones más.
# Estas son agregadas durante el paso de compilación del modelo:

# * Loss function —
#                Esto mide qué tan exacto es el modelo durante el entrenamiento.
#                Quiere minimizar esta función para dirigir el modelo en la dirección adecuada.
# * Optimizer —
#                Esto es como el modelo se actualiza basado en el set de datos que ve y la función de pérdida.
# * Metrics —
#                Se usan para monitorear los pasos de entrenamiento y de pruebas.
#                El siguiente ejemplo usa accuracy, la fracción de las imágenes que son correctamente clasificadas.

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Ahora sí podemos entrenar el modelo.
# Entrenar el modelo de red neuronal requiere de los siguientes pasos:
#  1) Entregar los datos de entrenamiento al modelo. En este ejemplo, el set de datos de entrenamiento está en los arrays
#     train_images y train_labels.
#  2) El modelo aprende a asociar imágenes y etiquetas.
#  3) Le pedimos al modelo que haga predicciones sobre un set de datos que se encuentran en el ejemplo,
#     incluido en el arreglo test_images. Tenemos que tener verificado que las predicciones sean iguales a las etiquetas de el
#     array test_labels.

model.fit(train_images, train_labels, epochs=10)

# A medida que el modelo entrena, la pérdida y la exactitud son desplegadas.
# Este modelo alcanza una exactitud de 0.88 (o 88%) sobre el set de datos de entrenamiento.

# Evaluamos el rendimiento del modelo sobre el set de datos:
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('Test de precisión', test_acc)

# Una vez que tenemos el modelo entrenado podemos usarlo para hacer predicciones.
predictions = model.predict(test_images)

# Una predicción es un arreglo de 10 números. Estos representan el nivel de "confianza" del modelo sobre las imágenes
#  de cada uno de los 10 artículos de moda/ropa. Ustedes pueden revisar cuál tiene el nivel más alto de confianza:


# Se generan las funciones para graficar set de la predicción de las 10 clases.
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


i = 0
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

i = 12
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

# Traza las primeras X imágenes de prueba, sus etiquetas predichas y las etiquetas verdaderas.
# Colorea las predicciones correctas en azul y las predicciones incorrectas en rojo.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

# Grab an image from the test dataset.
img = test_images[1]

print(img.shape)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img, 0))

print(img.shape)

predictions_single = model.predict(img)

print(predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
