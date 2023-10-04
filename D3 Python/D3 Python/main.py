lista_comidas = ["El pastel de papas", "Las empanadas", "La tarta de verduras", "El guiso de lentejas", "El asado", "Las papas fritas", "La tortilla", "Los ravioles", "Los sorrentinos", "Los ñoquis"]

#Enumerate se guarda en {x} y cada elemento de la lista se recorre y se guarda en {i}
for x, i in enumerate(lista_comidas): 
    print(f"En la posicion {x} està/n {i}")