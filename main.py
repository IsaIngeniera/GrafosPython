"""
Aplicación principal para el algoritmo de K-Paths
MODIFICACIÓN: Marca de agua con color más visible
"""
import sys
import random
import math
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QGraphicsScene,
    QGraphicsTextItem,
    QMessageBox
)
from ui_main_window import Ui_MainWindow
from graph import Graph
from node import Nodo
from edge import Arista


class KPathsApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(KPathsApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Intentar cargar el logo de EAFIT
        try:
            pixmap = QtGui.QPixmap("logo_eafit.png")
            if pixmap.isNull():
                pixmap = self.crear_logo_simple()
            pixmap = pixmap.scaled(100, 70, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.ui.lblLogo.setPixmap(pixmap)
        except:
            pixmap = self.crear_logo_simple()
            self.ui.lblLogo.setPixmap(pixmap)
        
        # Configurar la escena del grafo
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        # Listas para almacenar nodos y aristas
        self.nodos = []
        self.aristas = []
        
        self.watermark = None
        
        self.ui.btnGenerarMatriz.clicked.connect(self.generar_matriz_aleatoria)
        self.ui.btnDibujarGrafo.clicked.connect(self.dibujar_grafo)
        self.ui.btnCalcularKPaths.clicked.connect(self.calcular_k_paths)
        
        # Inicializar con una matriz de ejemplo
        self.inicializar_matriz_ejemplo()
        
        self.actualizar_status("Aplicación iniciada. Siga la guía paso a paso.")
        
    def crear_logo_simple(self):
        """Crea un logo simple de EAFIT si no existe el archivo"""
        pixmap = QtGui.QPixmap(100, 70)
        pixmap.fill(QtGui.QColor(74, 144, 164))
        
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtGui.QColor(255, 255, 255))
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), QtCore.Qt.AlignCenter, "EAFIT")
        painter.end()
        
        return pixmap
    
    def inicializar_matriz_ejemplo(self):
        """Inicializa la matriz con valores de ejemplo"""
        valores_ejemplo = [
            [0, 4, 0, 0, 8],
            [4, 0, 8, 0, 0],
            [0, 8, 0, 7, 2],
            [0, 0, 7, 0, 9],
            [8, 0, 2, 9, 0]
        ]
        
        for i in range(5):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(str(valores_ejemplo[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(i, j, item)
    
    def limpiar_grafo(self):
        """Limpia el grafo de manera segura y completa"""
        try:
            # Eliminar aristas con todos sus componentes
            for arista in self.aristas[:]:
                try:
                    if hasattr(arista, 'text_item') and arista.text_item:
                        if arista.text_item.scene() == self.scene:
                            self.scene.removeItem(arista.text_item)
                    
                    if hasattr(arista, 'text_bg') and arista.text_bg:
                        if arista.text_bg.scene() == self.scene:
                            self.scene.removeItem(arista.text_bg)
                    
                    if arista.scene() == self.scene:
                        self.scene.removeItem(arista)
                except:
                    pass
            
            # Eliminar nodos con todos sus componentes
            for nodo in self.nodos[:]:
                try:
                    if hasattr(nodo, 'text_item') and nodo.text_item:
                        if nodo.text_item.scene() == self.scene:
                            self.scene.removeItem(nodo.text_item)
                    
                    if nodo.scene() == self.scene:
                        self.scene.removeItem(nodo)
                except:
                    pass
            
            # Eliminar marca de agua
            if self.watermark:
                try:
                    if self.watermark.scene() == self.scene:
                        self.scene.removeItem(self.watermark)
                except:
                    pass
            
            self.scene.clear()
            
            # Limpiar listas
            self.nodos.clear()
            self.aristas.clear()
            self.watermark = None
            
            # Forzar actualización de la vista
            self.ui.graphicsView.viewport().update()
            
        except Exception as e:
            self.scene.clear()
            self.nodos.clear()
            self.aristas.clear()
            self.watermark = None
    
    def generar_matriz_aleatoria(self):
        """Genera una matriz de adyacencia aleatoria"""
        try:
            self.limpiar_grafo()
            
            for tabla in [self.ui.tableK1, self.ui.tableK2, self.ui.tableK3]:
                for i in range(tabla.rowCount()):
                    for j in range(tabla.columnCount()):
                        tabla.setItem(i, j, QtWidgets.QTableWidgetItem(""))

            filas = self.ui.tableWidget.rowCount()
            columnas = self.ui.tableWidget.columnCount()
            
            for i in range(filas):
                for j in range(columnas):
                    if i == j:
                        valor = 0
                    elif i < j:
                        if random.random() > 0.3:
                            valor = random.randint(1, 20)
                        else:
                            valor = 0
                    else:
                        item = self.ui.tableWidget.item(j, i)
                        valor = int(item.text()) if item else 0
                    
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.tableWidget.setItem(i, j, item)
            
            self.actualizar_status("✅ Paso 1 completado: Nueva matriz generada. Ahora dibuje el grafo.")
        except Exception as e:
            self.mostrar_error(f"Error al generar matriz: {str(e)}")
    
    def obtener_matriz(self):
        """Obtiene la matriz de adyacencia de la tabla"""
        try:
            filas = self.ui.tableWidget.rowCount()
            columnas = self.ui.tableWidget.columnCount()
            matriz = []
            
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    item = self.ui.tableWidget.item(i, j)
                    valor = int(item.text()) if item and item.text().isdigit() else 0
                    fila.append(valor)
                matriz.append(fila)
            
            return matriz
        except Exception as e:
            self.mostrar_error(f"Error al obtener matriz: {str(e)}")
            return []
    
    def crear_marca_agua(self):
        """
        Crea la marca de agua con los nombres de los autores
        MODIFICADO: Color más visible (gris oscuro)
        """
        if self.watermark and self.watermark.scene():
            self.scene.removeItem(self.watermark)
        
        self.watermark = QGraphicsTextItem()
        self.watermark.setPlainText("Isabella Ocampo S - Maria Laura Tafur")
        self.watermark.setDefaultTextColor(QtGui.QColor(100, 100, 100, 200))
        
        font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.watermark.setFont(font)
        
        # Posicionar en la parte inferior del área del grafo
        text_width = self.watermark.boundingRect().width()
        x = (self.ui.graphicsView.width() - text_width) / 2
        y = self.ui.graphicsView.height() - 40
        
        self.watermark.setPos(x, y)
        self.watermark.setZValue(-1)
        self.scene.addItem(self.watermark)
    
    def dibujar_grafo(self):
        """Dibuja el grafo en el GraphicsView"""
        try:
            self.limpiar_grafo()
            
            matriz = self.obtener_matriz()
            if not matriz:
                return
            
            num_nodos = len(matriz)
            radius = 25
            
            x_min, x_max = 100, 550
            y_min, y_max = 100, 450
            
            # Generar posiciones aleatorias evitando solapamientos
            posiciones = []
            intentos_max = 100
            distancia_minima = radius * 4
            
            for i in range(num_nodos):
                colocado = False
                for intento in range(intentos_max):
                    x = random.randint(x_min, x_max)
                    y = random.randint(y_min, y_max)
                    
                    muy_cerca = False
                    
                    for pos_x, pos_y in posiciones:
                        distancia = math.sqrt((x - pos_x)**2 + (y - pos_y)**2)
                        if distancia < distancia_minima:
                            muy_cerca = True
                            break
                    
                    if not muy_cerca or intento == intentos_max - 1:
                        posiciones.append((x, y))
                        colocado = True
                        break
            
            # Crear nodos
            for i in range(num_nodos):
                x, y = posiciones[i]
                
                nodo = Nodo(x, y, radius, i + 1, self)
                nodo.setPos(x, y)
                self.scene.addItem(nodo)
                self.nodos.append(nodo)
            
            # Crear aristas
            aristas_count = 0
            for i in range(num_nodos):
                for j in range(i + 1, num_nodos):
                    peso = matriz[i][j]
                    if peso > 0:
                        nodo1 = self.nodos[i]
                        nodo2 = self.nodos[j]
                        
                        arista = Arista(nodo1, nodo2, peso, self.scene, self, i, j)
                        self.aristas.append(arista)
                        self.scene.addItem(arista)
                        
                        nodo1.agregar_arista(arista)
                        nodo2.agregar_arista(arista)
                        aristas_count += 1
            
            self.crear_marca_agua()
            
            self.actualizar_status(f"✅ Paso 2 completado: Grafo dibujado con {num_nodos} nodos y {aristas_count} aristas. Ahora calcule K-Paths.")
        except Exception as e:
            self.mostrar_error(f"Error al dibujar grafo: {str(e)}")
    
    def resaltar_celda_matriz(self, i, j):
        """Resalta la celda correspondiente en la matriz de adyacencia"""
        try:
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item:
                        item.setBackground(QtGui.QColor(255, 255, 255))
            
            for (row, col) in [(i, j), (j, i)]:
                item = self.ui.tableWidget.item(row, col)
                if item:
                    item.setBackground(QtGui.QColor(255, 218, 185))
        except Exception as e:
            print(f"Error al resaltar celda: {str(e)}")
    
    def calcular_k_paths(self):
        """Calcula las matrices K=1, K=2 y K=3"""
        try:
            matriz = self.obtener_matriz()
            if not matriz:
                return
            
            grafo = Graph(matriz)
            
            matriz_k1 = grafo.get_k1_matrix()
            matriz_k2 = grafo.get_k2_matrix()
            matriz_k3 = grafo.get_k3_matrix()
            
            self.mostrar_matriz_en_tabla(matriz_k1, self.ui.tableK1)
            self.mostrar_matriz_en_tabla(matriz_k2, self.ui.tableK2)
            self.mostrar_matriz_en_tabla(matriz_k3, self.ui.tableK3)
            
            self.actualizar_status("✅ Paso 3 completado: Matrices K-Paths calculadas exitosamente. Revise los resultados en el panel derecho.")
        except Exception as e:
            self.mostrar_error(f"Error al calcular K-Paths: {str(e)}")
    
    def mostrar_matriz_en_tabla(self, matriz, tabla):
        """Muestra una matriz en una tabla"""
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                valor = matriz[i][j]
                texto = str(int(valor)) if valor != float('inf') and valor > 0 else "∞" if valor == float('inf') else "-"
                item = QtWidgets.QTableWidgetItem(texto)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                
                if valor == 0 or texto == "-":
                    item.setBackground(QtGui.QColor(240, 240, 240))
                elif texto == "∞":
                    item.setBackground(QtGui.QColor(255, 200, 200))
                else:
                    item.setBackground(QtGui.QColor(200, 255, 200))
                
                tabla.setItem(i, j, item)
    
    def actualizar_status(self, mensaje):
        """Actualiza el mensaje de estado"""
        self.ui.lblStatus.setText(mensaje)
    
    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error"""
        QMessageBox.critical(self, "Error", mensaje)
        self.actualizar_status(f"❌ Error: {mensaje}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = KPathsApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
