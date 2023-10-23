# �rboles de Decisi�n: Algoritmo ID3
# Ejemplo de construcci�n de un �rbol de decisi�n con Scikit-Learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
data = load_iris()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador de �rbol de Decisi�n (ID3)
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Realizar predicciones
y_pred = clf.predict(X_test)

# Calcular la precisi�n del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisi�n del modelo:", accuracy)

