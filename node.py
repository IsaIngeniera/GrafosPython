"""
Clase Nodo: Representa un nodo visual en el grafo
(Sin cambios en funcionalidad)
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsItem

class Nodo(QGraphicsEllipseItem):
    def __init__(self, x, y, radius, id, app):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        
        # Colores pasteles suaves
        self.color_normal = QtGui.QColor(173, 216, 230)
        self.color_hover = QtGui.QColor(255, 182, 193)
        self.color_selected = QtGui.QColor(255, 218, 185)
        
        self.setBrush(QtGui.QBrush(self.color_normal))
        self.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100), 2))
        self.id = id
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        
        # Texto del nodo
        self.text_item = QGraphicsTextItem(f"{self.id}", self)
        self.text_item.setDefaultTextColor(QtGui.QColor(50, 50, 50))
        font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.text_item.setFont(font)
        
        # Centrar el texto
        text_rect = self.text_item.boundingRect()
        self.text_item.setPos(-text_rect.width()/2, -text_rect.height()/2)
        
        self.app = app
        self.aristas = []
        
    def agregar_arista(self, arista):
        """Agrega una arista conectada a este nodo"""
        self.aristas.append(arista)
        
    def itemChange(self, change, value):
        """Actualiza las aristas cuando el nodo se mueve"""
        if change == QGraphicsItem.ItemPositionChange:
            for arista in self.aristas:
                arista.actualizar_posiciones()
        return super().itemChange(change, value)
    
    def hoverEnterEvent(self, event):
        """Cambia el color cuando el mouse entra"""
        self.setBrush(QtGui.QBrush(self.color_hover))
        super().hoverEnterEvent(event)
        
    def hoverLeaveEvent(self, event):
        """Restaura el color cuando el mouse sale"""
        self.setBrush(QtGui.QBrush(self.color_normal))
        super().hoverLeaveEvent(event)
