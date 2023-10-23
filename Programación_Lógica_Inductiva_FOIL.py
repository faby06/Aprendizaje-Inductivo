# Programación Lógica Inductiva: Algoritmo FOIL (Primera Orden de Aprendizaje Inductivo)
# Ejemplo de uso del algoritmo FOIL

def foil(examples, target_predicate):
    positive_examples = [example for example in examples if target_predicate(example)]
    negative_examples = [example for example in examples if not target_predicate(example)]
    
    if len(positive_examples) == 0:
        return False
    
    most_specific_hypothesis = positive_examples[0].copy()
    
    for example in positive_examples:
        for i, feature in enumerate(most_specific_hypothesis):
            if feature != example[i]:
                most_specific_hypothesis[i] = '?'
    
    return most_specific_hypothesis

# Ejemplo de conjunto de datos de entrenamiento
training_data = [
    (1, 1, 1, True),
    (1, 0, 0, True),
    (0, 1, 0, False),
    (1, 0, 1, True)
]

# Clase objetivo
target_predicate = lambda x: x[-1] == True

# Aplicar el algoritmo FOIL
hypothesis = foil(training_data, target_predicate)

print("Hipothesis:", hypothesis)

