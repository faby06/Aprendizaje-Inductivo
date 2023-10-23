# �rboles de Regresi�n: Algoritmo M5
# Ejemplo de construcci�n de un �rbol de regresi�n con Scikit-Learn

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos de diabetes
data = load_diabetes()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un regresor de �rbol de Regresi�n (M5)
regressor = DecisionTreeRegressor(random_state=42)

# Entrenar el modelo
regressor.fit(X_train, y_train)

# Realizar predicciones
y_pred = regressor.predict(X_test)

# Calcular el error cuadr�tico medio (MSE) del modelo
mse = mean_squared_error(y_test, y_pred)
print("Error cuadr�tico medio:", mse)

