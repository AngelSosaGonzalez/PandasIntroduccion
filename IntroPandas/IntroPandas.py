""" Proyecto o trabajo introductorio a Pandas, Pandas es un modulo para la manipulacion de datos """

#importacion de la librerias descargadas
import pandas
import matplotlib.pyplot as plt

#Vamos a cargar nuestros datos
DatCar = pandas.read_csv('Datos\car.csv', header=None)

#Aplicaremos los encabezados
DatCar.columns = ['Precio', 'Costo de mantenimiento', 'Numero de puertas', 'Capacidad', 'Tamaño', 'Seguridad', 'Desicion']

#Mostraremos nuestos datos (Primeros)
print(DatCar.head(5))

#Mostramos los ultimos datos
print(DatCar.tail(5))

#Mostrar informacion de la lista (columnas y registros)
print('Los registros y columnas de esta tabla son:', DatCar.shape)

#Mostrar el tamaño total de nuestra tabla
print('El tamaño total de la tabla es:', DatCar.size)

#Realizar una consula solamente mostrando una columna en especifico
print(DatCar['Tamaño'].head(5))

#Pero tambien podemos utilizar rangos (Algo de Python basico)
print(DatCar['Precio'][:3])

#Consulta mas de una columna
print(DatCar[ ['Precio', 'Tamaño'] ].head(3))

#Ordenar datos y agrupar datos 
#Contaremos los registros
print(DatCar['Tamaño'].value_counts()) #Que no se te olvide que se escribe counts con 's'

#Ordenamiento de datos
#Ascendente
print(DatCar['Tamaño'].value_counts().sort_index(ascending = True))

#Descendente
print(DatCar['Tamaño'].value_counts().sort_index(ascending = False))

#*** GRAFICAR LOS DATOS ***
#Antes de todo para no escribir todo el codigo guardaremos una consulta en una variable
ConsulCar = DatCar['Tamaño'].value_counts().sort_index(ascending = False)

#Ahora en base a esta consulta vamos a graficar 
ConsulCar.plot(kind = 'bar')
#'plt' sale del modulo de 'matplotlib.pyplot', solamente que es su alias para invocarlo mas facil
plt.show()

#Veremos los valores que contiene cada columna de la tabla
print(DatCar['Precio'].unique())

#Remplasaremos los datos de la colmuna precio a numeros
DatCar['Precio'].replace(('vhigh', 'high', 'med', 'low'), (4, 3, 2, 1), inplace = True)
#Comprobamos 
print(DatCar['Precio'].unique())

#*** GRAFICAR LOS DATOS ***
#Creamos nuestra variable
Precio = DatCar['Precio'].value_counts()

#Las barras las caracterizamos con colores (Para que se vea chula), cada color es por cada categoria hay 4 en total
Colores = ['#3BCD69', '#CD563B', '#3BA7CD', '#CD3BB9']

#Ahora creamos nuestra grafica
Precio.plot(kind = 'bar', color = Colores)
#Vamos a marcar los parametros de la grafica
plt.xlabel('Precio')
plt.ylabel('Auto')
#Titulo de la grafica 
plt.title('Precio de los autos')
#Y lo visulizamos 
plt.show()

#*** GRAFICAR DATOS (Con otra grafica) ***
#Usamos 'unique' solo para visualizar cuantos datos hay en la columna
print(DatCar['Capacidad'].unique())

#Realizaremos un conteo de los datos
print(DatCar['Capacidad'].value_counts())

#Vamos a etiquetar (o meter a una variable)
Columns = ['2', '4', 'more']
Tamaño = [576, 576, 576]
#Vamos a reciclar los colores
Colores = ['#3BCD69', '#CD563B', '#3BA7CD']
#Espacios de los datos, estos sirve para separar los datos de la grafica, como por ejemplo destacar un pedazo o solamente estetico
Espacios = [0, 0, 0]

#Ahora vamos a graficar 
#Parametros de la grafica 
plt.pie(Tamaño, labels=Columns, colors=Colores, explode=Espacios, shadow=True, autopct='%.2f%%')
#Titulo de la grafica
plt.title('Tabla de capacidad', fontsize = 10)
#En la descripcion de X y Y nos tenemos nada asi que lo ocultaremos 
plt.axis('off')
#Agregaremos descipcion
plt.legend(loc = 'best')
plt.show()

#NOTA: Hay otro metodo para la visualizacion de los datos llamado 'Sample', este sirver para ver los datos de manera aleatoria
print(DatCar['Precio'].sample(3))