class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    #regresar verdadero si la lista esta vacia
    def estaVacia(self):
        return self.cabeza == None
    
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    

    def buscarxmlData(self, xmlData):
        palabras = xmlData
        actual = self.cabeza
        contador=0
        resultadoTexto=""
        while actual:
            for palabra in palabras:
                if palabra.startswith("#") and palabra.endswith("#"):
                    palabra = palabra.replace("#", "")
                    print("compara ->"+palabra+" con ->"+actual.valor)
                    if actual.valor == palabra:
                        contador += 1
                        resultadoTexto += "#"+palabra + "# :"+ str(contador) + " \n"
            contador=0
            actual = actual.siguiente

        return resultadoTexto
    
    def buscarxmlDataMenciones(self, xmlData):
        palabras = xmlData
        actual = self.cabeza
        contador=0
        resultadoTexto=""
        while actual:
            for palabra in palabras:
                if palabra.startswith("@"):
                    palabra = palabra.replace("@", "")
                    print("compara ->"+palabra+" con ->"+actual.valor)
                    if actual.valor == palabra:
                        contador += 1
                        resultadoTexto += "@"+palabra + " :"+ str(contador) + "\n"
            contador=0
            actual = actual.siguiente

        return resultadoTexto
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

