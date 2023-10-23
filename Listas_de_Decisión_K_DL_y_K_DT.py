# Listas de Decisión: Algoritmo K-DL (Decision List) y K-DT (Decision Table)
# Ejemplo de construcción de una lista de decisión con reglas

def decision_list(decision_table):
    rules = []
    for row in decision_table:
        condition = row[:-1]
        decision = row[-1]
        rule = (condition, decision)
        rules.append(rule)
    return rules

def classify_with_decision_list(rules, instance):
    for condition, decision in rules:
        if all([instance[i] == value for i, value in enumerate(condition)]):
            return decision
    return None

# Ejemplo de conjunto de datos de decision table
decision_table = [
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1]
]

# Construir la lista de decisiones a partir de la decision table
rules = decision_list(decision_table)

# Ejemplo de clasificación con la lista de decisiones
new_instance = [1, 0, 1]
result = classify_with_decision_list(rules, new_instance)
print("Resultado de clasificación:", result)

