"""
Clase Graph: Implementa el algoritmo de k-caminos más cortos
(Sin cambios - lógica matemática preservada)
"""
import sys

class Graph:
    def __init__(self, matriz_adyacencia):
        """
        Inicializa el grafo con una matriz de adyacencia
        :param matriz_adyacencia: Matriz de pesos entre nodos
        """
        self.n = len(matriz_adyacencia)
        self.matriz = [[matriz_adyacencia[i][j] if matriz_adyacencia[i][j] > 0 else (0 if i == j else float('inf'))
                        for j in range(self.n)] for i in range(self.n)]
        
    def floyd_warshall_k_paths(self, k=1):
        """
        Algoritmo de Floyd-Warshall modificado para encontrar k-caminos más cortos
        :param k: Número de caminos más cortos a encontrar (1, 2, o 3)
        :return: Matriz con los k-ésimos caminos más cortos
        """
        dist = [[[] for _ in range(self.n)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if self.matriz[i][j] != float('inf'):
                    dist[i][j].append(self.matriz[i][j])
        
        for k_node in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][k_node] and dist[k_node][j]:
                        for d1 in dist[i][k_node]:
                            for d2 in dist[k_node][j]:
                                new_dist = d1 + d2
                                dist[i][j].append(new_dist)
                                dist[i][j] = sorted(list(set(dist[i][j])))[:k]
        
        resultado = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if len(dist[i][j]) >= k:
                    resultado[i][j] = dist[i][j][k-1]
                elif len(dist[i][j]) > 0:
                    resultado[i][j] = dist[i][j][-1]
                    
        for i in range(self.n):
            for j in range(self.n):
                if resultado[i][j] == float('inf'):
                    resultado[i][j] = 0
                    
        return resultado
    
    def get_k1_matrix(self):
        """Retorna la matriz de caminos más cortos (k=1)"""
        return self.floyd_warshall_k_paths(1)
    
    def get_k2_matrix(self):
        """Retorna la matriz de segundos caminos más cortos (k=2)"""
        return self.floyd_warshall_k_paths(2)
    
    def get_k3_matrix(self):
        """Retorna la matriz de terceros caminos más cortos (k=3)"""
        return self.floyd_warshall_k_paths(3)
