def ConfereClasses(listaDeClasses, classeDesejada):
    for var in listaDeClasses:
        if classeDesejada.lower() == var.lower():
            return True
    return False