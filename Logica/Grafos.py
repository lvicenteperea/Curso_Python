class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)
    
    def obtener_vertices(self):
        return list(self.vertices.keys())
    
    def obtener_adyacentes(self, vertice):
        if vertice in self.vertices:
            return self.vertices[vertice]
        else:
            return None

    def __str__(self):
        return '\n'.join([f'{v}: {self.vertices[v]}' for v in self.vertices])




# Crear una instancia del grafo
grafo = Grafo()

# Agregar los vértices
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)
grafo.agregar_vertice(5)
grafo.agregar_vertice(6)

# Agregar las aristas (conexiones entre los nodos)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(2, 5)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 5)
grafo.agregar_arista(4, 6)

# Imprimir el grafo para ver su estructura
print(grafo)
