#En este proyecto pondremos en practica lo aprendido... Usando un arbol de desiciones 

#importacion de la librerias descargadas
import pandas
import matplotlib.pyplot as plt
import numpy as np

#Importaremos el modulo para el arbol
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

#Vamos a cargar nuestros datos
DatCar = pandas.read_csv('Datos\car.csv', header=None)

#Aplicaremos los encabezados
DatCar.columns = ['Precio', 'Mantenimiento', 'Puertas', 'Capacidad', 'Tamaño', 'Seguridad', 'Desicion']

#Para comenzar con el arbol de desiciones, cambiaremos los datos a numeros
#Datos de precio
DatCar.Precio.replace(('vhigh', 'high', 'med', 'low'), (4, 3, 2, 1), inplace = True) 
#Datos de mantenimiento
DatCar.Mantenimiento.replace(('vhigh', 'high', 'med', 'low'), (4, 3, 2, 1), inplace = True) 
#Datos de puertas
DatCar.Puertas.replace(('2', '3', '4', '5more'), (4, 3, 2, 1), inplace = True)
#Datos de capacidad
DatCar.Capacidad.replace(('2', '4', 'more'), (3, 2, 1), inplace = True)
#Datos de tamaño
DatCar.Tamaño.replace(('small', 'med', 'big'), (3, 2, 1), inplace = True)
#Datos de seguridad
DatCar.Seguridad.replace(('low', 'med', 'high'), (3, 2, 1), inplace = True)

#Para la toma deseciones (para ser mas entendible) cambiaremos la desicion 
DatCar.Desicion.replace(('unacc', 'acc', 'good', 'vgood'), (4, 3, 2, 1), inplace = True)

#Comenzaremos con el aprendizaje 
#Meteremos todos los datos de la tabla a una nueva variable
Aprendizaje = DatCar.values

#Ahora insertaremos las columnas que aprendera
X = Aprendizaje[:, 0:6]
Y = np.asarray(Aprendizaje[:, 6], dtype = 'S6')

#**SKLEARN PARA EL ARBOL **
#Vamos a configurar los parametros para el entrenamiento 
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#Creamos nuestro arbol
Arbol = tree.DecisionTreeClassifier(max_depth= 10)
#Lo entrenamos
Arbol.fit(X_Train, Y_Train)

#Porbaremos si en efecto esta entrenado
Y_Prediccion = Arbol.predict(X_Test)
print(Y_Prediccion)

#Vamos a calcular el Score (o puntaje) de precision para nuestro arbol
Puntaje = Arbol.score(X_Test, Y_Test)
print('La precision de nuestro arbol es: %0.4f' % (Puntaje))