import tensorflow as tf
import numpy as np

RValues = np.array([0.006, 0.007, 0.008, 0.009, 0.010])
outputs = np.array(
    [0.000056548, 0.00010476, 0.00017872, 0.00028677, 0.0004363])

capa1 = tf.keras.layers.Dense(units=34, input_shape=[1])
capa2 = tf.keras.layers.Dense(units=34)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([capa1, capa2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss="mean_squared_error"
)

# Asegúrate de proporcionar los datos en el formato correcto
modelo.fit(RValues, outputs, epochs=800, verbose=False)

# Realiza la predicción con el valor 0.010
prediccion = modelo.predict(np.array([0.005]))
print(prediccion)
