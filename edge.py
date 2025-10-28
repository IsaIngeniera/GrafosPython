"""
Clase Arista: Representa una arista visual en el grafo
MODIFICACIONES:
- Las líneas ahora parten del borde del círculo, no del centro
- Los números de peso están directamente sobre las líneas sin fondo blanco
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsTextItem
from PyQt5.QtCore import Qt
import math

class Arista(QGraphicsLineItem):
    def __init__(self, nodo1, nodo2, peso, scene, app=None, i=0, j=0):
        super().__init__()
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.peso = peso
        self.scene = scene
        self.app = app
        self.i = i
        self.j = j
        
        self.node_radius = 25
        
        # Colores pasteles
        self.color_normal = QtGui.QColor(150, 150, 150)
        self.color_selected = QtGui.QColor(255, 160, 122)
        
        self.setPen(QtGui.QPen(self.color_normal, 2))
        self.setFlag(QGraphicsLineItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        
        self.text_item = QGraphicsTextItem(str(self.peso))
        self.text_item.setDefaultTextColor(QtGui.QColor(50, 50, 50))
        font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.text_item.setFont(font)
        
        self.scene.addItem(self.text_item)
        self.text_item.setZValue(2)
        
        self.actualizar_posiciones()
    
    def calcular_punto_borde(self, x_centro, y_centro, x_destino, y_destino):
        """
        Calcula el punto en el borde del círculo en dirección al destino
        """
        # Calcular el ángulo desde el centro hacia el destino
        dx = x_destino - x_centro
        dy = y_destino - y_centro
        distancia = math.sqrt(dx**2 + dy**2)
        
        if distancia == 0:
            return x_centro, y_centro
        
        # Normalizar y multiplicar por el radio
        x_borde = x_centro + (dx / distancia) * self.node_radius
        y_borde = y_centro + (dy / distancia) * self.node_radius
        
        return x_borde, y_borde
        
    def actualizar_posiciones(self):
        """
        Actualiza la posición de la línea y el texto
        MODIFICADO: Las líneas ahora parten del borde del círculo
        """
        # Obtener centros de los nodos
        x1_centro, y1_centro = self.nodo1.scenePos().x(), self.nodo1.scenePos().y()
        x2_centro, y2_centro = self.nodo2.scenePos().x(), self.nodo2.scenePos().y()
        
        x1, y1 = self.calcular_punto_borde(x1_centro, y1_centro, x2_centro, y2_centro)
        x2, y2 = self.calcular_punto_borde(x2_centro, y2_centro, x1_centro, y1_centro)
        
        self.setLine(x1, y1, x2, y2)
        
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx**2 + dy**2)
        
        if length > 0:
            # Vector perpendicular normalizado
            perp_x = -dy / length
            perp_y = dx / length
            
            # Desplazar el texto 12 píxeles perpendicular a la línea
            offset = 12
            mid_x += perp_x * offset
            mid_y += perp_y * offset
        
        text_rect = self.text_item.boundingRect()
        self.text_item.setPos(mid_x - text_rect.width()/2, mid_y - text_rect.height()/2)
    
    def paint(self, painter, option, widget=None):
        """
        Dibuja solo la línea - el texto se maneja automáticamente por QGraphicsTextItem
        """
        super().paint(painter, option, widget)
    
    def mousePressEvent(self, event):
        """Resalta la arista, nodos y celda en la matriz al hacer clic"""
        self.setPen(QtGui.QPen(self.color_selected, 4))
        self.nodo1.setBrush(QtGui.QBrush(QtGui.QColor(255, 218, 185)))
        self.nodo2.setBrush(QtGui.QBrush(QtGui.QColor(255, 218, 185)))
        
        if self.app:
            self.app.resaltar_celda_matriz(self.i, self.j)
        
        super().mousePressEvent(event)
        
    def mouseReleaseEvent(self, event):
        """Restaura el color original"""
        self.setPen(QtGui.QPen(self.color_normal, 2))
        super().mouseReleaseEvent(event)
    
    def hoverEnterEvent(self, event):
        """Cambia el cursor al pasar sobre la arista"""
        self.setCursor(Qt.PointingHandCursor)
        super().hoverEnterEvent(event)
    
    def hoverLeaveEvent(self, event):
        """Restaura el cursor al salir de la arista"""
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(event)
