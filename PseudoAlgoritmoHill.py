import random

# función de evaluación
def f(x):
    return -x**2+5

def hill_climbing():
    # SP
    current = random.uniform(-10,10)
    while True:
        # Punto actual en f
        current_value = f(current)
        # Selección de vecino aleatorio
        neighbor = current + random.uniform(-1,1)
        neighbor_value = f(neighbor)
        
        # Evaluar al vecino
        if neighbor_value > current_value:
            current = neighbor
        else:
            return  current, current_value
        
result = hill_climbing()
    