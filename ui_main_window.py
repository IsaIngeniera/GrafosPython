"""
Interfaz de usuario generada para la aplicación de grafos
(Sin cambios)
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        
        MainWindow.setStyleSheet("background-color: #F5F5F0;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        # Logo EAFIT
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(20, 10, 100, 70))
        self.lblLogo.setObjectName("lblLogo")
        self.lblLogo.setScaledContents(True)
        
        # Título principal
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(130, 10, 1250, 35))
        self.lblTitulo.setStyleSheet("""
            font: bold 18pt 'Arial';
            color: #4A90A4;
            background-color: transparent;
        """)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        
        # Subtítulo
        self.lblSubtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblSubtitulo.setGeometry(QtCore.QRect(130, 45, 1250, 20))
        self.lblSubtitulo.setStyleSheet("""
            font: 11pt 'Arial';
            color: #6B6B6B;
            background-color: transparent;
        """)
        self.lblSubtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSubtitulo.setObjectName("lblSubtitulo")
        
        self.groupGuia = QtWidgets.QGroupBox(self.centralwidget)
        self.groupGuia.setGeometry(QtCore.QRect(20, 90, 360, 200))
        self.groupGuia.setStyleSheet("""
            QGroupBox {
                font: bold 12pt 'Arial';
                color: #4A90A4;
                border: 2px solid #B8D4E0;
                border-radius: 8px;
                margin-top: 12px;
                background-color: #FFFFFF;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px 0 8px;
            }
        """)
        self.groupGuia.setTitle("Guía Paso a Paso")
        
        self.lblGuiaTexto = QtWidgets.QLabel(self.groupGuia)
        self.lblGuiaTexto.setGeometry(QtCore.QRect(15, 30, 330, 160))
        self.lblGuiaTexto.setStyleSheet("""
            font: 10pt 'Arial';
            color: #2C5F6F;
            background-color: transparent;
            line-height: 1.6;
        """)
        self.lblGuiaTexto.setWordWrap(True)
        self.lblGuiaTexto.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblGuiaTexto.setText(
            "<p style='margin-bottom: 8px;'><b>1. Generar Matriz:</b><br/>"
            "Crea una matriz de adyacencia aleatoria y limpia el grafo anterior.</p>"
            
            "<p style='margin-bottom: 8px;'><b>2. Dibujar Grafo:</b><br/>"
            "Visualiza el grafo con posiciones aleatorias de nodos.</p>"
            
            "<p style='margin-bottom: 8px;'><b>3. Calcular K-Paths:</b><br/>"
            "Obtén las matrices de caminos más cortos para K=1, K=2 y K=3.</p>"
            
            "<p style='color: #6B6B6B; font-size: 9pt; margin-top: 10px;'>"
            "Nota: Puedes editar manualmente los valores de la matriz antes de dibujar.</p>"
        )
        
        self.lblMatrizInput = QtWidgets.QLabel(self.centralwidget)
        self.lblMatrizInput.setGeometry(QtCore.QRect(20, 300, 200, 25))
        self.lblMatrizInput.setStyleSheet("font: bold 11pt 'Arial'; color: #4A90A4;")
        self.lblMatrizInput.setText("Matriz de Adyacencia:")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 330, 360, 200))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 2px solid #B8D4E0;
                border-radius: 8px;
                gridline-color: #E0E0E0;
            }
            QHeaderView::section {
                background-color: #B8D4E0;
                color: #2C5F6F;
                font-weight: bold;
                border: 1px solid #A0C4D0;
                padding: 4px;
            }
        """)
        
        for i in range(5):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(f"v{i+1}"))
            self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(f"v{i+1}"))
        
        button_style = """
            QPushButton {
                background-color: #B8D4E0;
                color: #2C5F6F;
                border: 2px solid #A0C4D0;
                border-radius: 10px;
                font: bold 11pt 'Arial';
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #A0C4D0;
            }
            QPushButton:pressed {
                background-color: #88B4C4;
            }
        """
        
        self.btnGenerarMatriz = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarMatriz.setGeometry(QtCore.QRect(20, 540, 170, 40))
        self.btnGenerarMatriz.setObjectName("btnGenerarMatriz")
        self.btnGenerarMatriz.setStyleSheet(button_style)
        
        self.btnDibujarGrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btnDibujarGrafo.setGeometry(QtCore.QRect(200, 540, 180, 40))
        self.btnDibujarGrafo.setObjectName("btnDibujarGrafo")
        self.btnDibujarGrafo.setStyleSheet(button_style)
        
        self.btnCalcularKPaths = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcularKPaths.setGeometry(QtCore.QRect(20, 590, 360, 45))
        self.btnCalcularKPaths.setObjectName("btnCalcularKPaths")
        self.btnCalcularKPaths.setStyleSheet(button_style)
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(400, 90, 600, 650))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("""
            QGraphicsView {
                background-color: #FFFFFF;
                border: 2px solid #B8D4E0;
                border-radius: 8px;
            }
        """)
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(1020, 90, 360, 650))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border: 2px solid #B8D4E0;
                border-radius: 8px;
                background-color: #FAFAFA;
            }
            QScrollBar:vertical {
                border: none;
                background: #F0F0F0;
                width: 12px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #B8D4E0;
                min-height: 20px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #A0C4D0;
            }
        """)
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 340, 750))
        
        self.lblK1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblK1.setGeometry(QtCore.QRect(10, 10, 320, 25))
        self.lblK1.setStyleSheet("font: bold 12pt 'Arial'; color: #4A90A4;")
        self.lblK1.setObjectName("lblK1")
        
        self.tableK1 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableK1.setGeometry(QtCore.QRect(10, 40, 320, 150))
        self.tableK1.setRowCount(5)
        self.tableK1.setColumnCount(5)
        self.tableK1.setObjectName("tableK1")
        self.tableK1.setStyleSheet("""
            QTableWidget {
                background-color: #FFF8F0;
                border: 2px solid #D4C4B0;
                border-radius: 8px;
                gridline-color: #E8E0D8;
            }
            QHeaderView::section {
                background-color: #E8D4C0;
                color: #5F4C3F;
                font-weight: bold;
                border: 1px solid #D4C4B0;
                padding: 4px;
                font-size: 9pt;
            }
        """)
        
        self.lblK2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblK2.setGeometry(QtCore.QRect(10, 200, 320, 25))
        self.lblK2.setStyleSheet("font: bold 12pt 'Arial'; color: #4A90A4;")
        self.lblK2.setObjectName("lblK2")
        
        self.tableK2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableK2.setGeometry(QtCore.QRect(10, 230, 320, 150))
        self.tableK2.setRowCount(5)
        self.tableK2.setColumnCount(5)
        self.tableK2.setObjectName("tableK2")
        self.tableK2.setStyleSheet("""
            QTableWidget {
                background-color: #F0F8FF;
                border: 2px solid #B0C4D4;
                border-radius: 8px;
                gridline-color: #D8E0E8;
            }
            QHeaderView::section {
                background-color: #C0D4E8;
                color: #3F4C5F;
                font-weight: bold;
                border: 1px solid #B0C4D0;
                padding: 4px;
                font-size: 9pt;
            }
        """)
        
        self.lblK3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblK3.setGeometry(QtCore.QRect(10, 410, 320, 25))
        self.lblK3.setStyleSheet("font: bold 12pt 'Arial'; color: #4A90A4;")
        self.lblK3.setObjectName("lblK3")
        
        self.tableK3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableK3.setGeometry(QtCore.QRect(10, 440, 320, 150))
        self.tableK3.setRowCount(5)
        self.tableK3.setColumnCount(5)
        self.tableK3.setObjectName("tableK3")
        self.tableK3.setStyleSheet("""
            QTableWidget {
                background-color: #FFF0F8;
                border: 2px solid #D4B0C4;
                border-radius: 8px;
                gridline-color: #E8D8E0;
            }
            QHeaderView::section {
                background-color: #E8C0D4;
                color: #5F3F4C;
                font-weight: bold;
                border: 1px solid #D4B0C4;
                padding: 4px;
                font-size: 9pt;
            }
        """)
        
        for table in [self.tableK1, self.tableK2, self.tableK3]:
            for i in range(5):
                table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(f"v{i+1}"))
                table.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(f"v{i+1}"))
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(20, 750, 1360, 30))
        self.lblStatus.setStyleSheet("""
            font: 10pt 'Arial';
            color: #6B6B6B;
            background-color: #E8E8E0;
            border: 1px solid #D0D0C8;
            border-radius: 5px;
            padding: 5px;
        """)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "K-Paths Algorithm - EAFIT"))
        self.lblTitulo.setText(_translate("MainWindow", "Algoritmo de K-Caminos Más Cortos"))
        self.lblSubtitulo.setText(_translate("MainWindow", "Implementación para k=1, k=2 y k=3"))
        self.btnGenerarMatriz.setText(_translate("MainWindow", "Generar Matriz"))
        self.btnDibujarGrafo.setText(_translate("MainWindow", "Dibujar Grafo"))
        self.btnCalcularKPaths.setText(_translate("MainWindow", "Calcular K-Paths"))
        self.lblK1.setText(_translate("MainWindow", "📊 Matriz K=1 (Caminos más cortos):"))
        self.lblK2.setText(_translate("MainWindow", "📊 Matriz K=2 (Segundos más cortos):"))
        self.lblK3.setText(_translate("MainWindow", "📊 Matriz K=3 (Terceros más cortos):"))
        self.lblStatus.setText(_translate("MainWindow", "Listo para comenzar"))
        self.tableWidget.setToolTip(_translate("MainWindow", "Matriz de adyacencia del grafo"))
