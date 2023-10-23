# Espacio de Versiones y AQ
# Ejemplo de clasificación usando el algoritmo Version Space y AQ

def version_space_hypotheses(training_data, target):
    version_space = []
    for instance in training_data:
        if instance[-1] == target:
            version_space.append(instance[:-1])
    return version_space

def classify_with_version_space(version_space, instance):
    for hypothesis in version_space:
        if all([instance[i] == value for i, value in enumerate(hypothesis)]):
            return 1  # Clase positiva
    return 0  # Clase negativa

# Ejemplo de conjunto de datos de entrenamiento
training_data = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Clase objetivo
target_class = 1

# Construir el espacio de versiones
vs = version_space_hypotheses(training_data, target_class)

# Ejemplo de clasificación con el espacio de versiones
new_instance = [1, 0, 1]
result = classify_with_version_space(vs, new_instance)
print("Resultado de clasificación:", result)

