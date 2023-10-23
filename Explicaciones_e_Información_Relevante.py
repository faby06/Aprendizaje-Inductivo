# Explicaciones e Informaci�n Relevante
# Ejemplo de explicaci�n de clasificaci�n usando Scikit-Learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.inspection import plot_partial_dependence
import matplotlib.pyplot as plt

# Cargar el conjunto de datos Iris
data = load_iris()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador de Bosques Aleatorios (Random Forest)
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Realizar predicciones
y_pred = clf.predict(X_test)

# Calcular la precisi�n del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisi�n del modelo:", accuracy)

# Mostrar gr�ficos de importancia de caracter�sticas
features = data.feature_names
plot_partial_dependence(clf, X_train, features=features, grid_resolution=50)
plt.show()

