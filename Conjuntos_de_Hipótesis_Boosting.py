# Conjuntos de Hipótesis: Algoritmo de Boosting con Scikit-Learn
# Ejemplo de uso del clasificador AdaBoost

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
data = load_iris()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador de Árbol de Decisión como base para AdaBoost
base_classifier = DecisionTreeClassifier(max_depth=1)

# Crear un clasificador AdaBoost
clf = AdaBoostClassifier(base_classifier, n_estimators=50, random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Realizar predicciones
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo AdaBoost:", accuracy)

