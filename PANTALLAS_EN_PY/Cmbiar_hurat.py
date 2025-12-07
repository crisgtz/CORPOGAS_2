from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import time
import sys
import os

# Agregar carpeta del proyecto al PATH para que encuentre CD
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from CD.Registro_empleados import cargar_horarios, guardar_horarios


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 855)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 741, 851))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("background-image: url(:/newPrefix/interfaz.jpeg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/interfaz.jpeg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextEditable |
            QtCore.Qt.TextEditorInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(210, 40, 251, 51))
        self.textBrowser.setObjectName("textBrowser")


        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(460, 170, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("color: white; font: 87 10pt 'Arial Black';")

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 170, 95, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(True)
        self.radioButton_2.setAutoRepeatDelay(324)
        self.radioButton_2.setAutoRepeatInterval(111)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("color: white; font: 87 10pt 'Arial Black';")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(160, 170, 95, 20))
        self.radioButton.setChecked(False)
        self.radioButton.setAutoRepeat(True)
        self.radioButton.setAutoRepeatDelay(296)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("color: white; font: 87 10pt 'Arial Black';")

        # Texto de "Ingresar Nueva Hora"
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 260, 361, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")

        # Campo HH:MM:SS
        self.leUsuario_3 = QtWidgets.QLineEdit(Dialog)
        self.leUsuario_3.setGeometry(QtCore.QRect(260, 330, 101, 31))
        self.leUsuario_3.setObjectName("leUsuario_3")

        # BOTÓN GUARDAR
        self.btnIngresar = QtWidgets.QPushButton(Dialog)
        self.btnIngresar.setGeometry(QtCore.QRect(420, 440, 121, 31))
        self.btnIngresar.setStyleSheet(
            "background-color: qlineargradient("
            "spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(180,180,180,255), stop:1 rgba(255,255,255,255));"
            "font: 87 10pt 'Arial Black';"
        )
        self.btnIngresar.setObjectName("btnIngresar")

        # BOTÓN VOLVER
        self.btnIngresar_2 = QtWidgets.QPushButton(Dialog)
        self.btnIngresar_2.setGeometry(QtCore.QRect(120, 440, 121, 31))
        self.btnIngresar_2.setStyleSheet(
            "background-color: qlineargradient("
            "spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(180,180,180,255), stop:1 rgba(255,255,255,255));"
            "font: 87 10pt 'Arial Black';"
        )
        self.btnIngresar_2.setObjectName("btnIngresar_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cambiar horario de turno"))
        self.textBrowser.setHtml(_translate("Dialog",
            "<p style='font-size:12pt;'>TURNO A MODIFICAR</p>"
        ))
        self.radioButton_3.setText(_translate("Dialog", "Turno 3"))
        self.radioButton_2.setText(_translate("Dialog", "Turno 2"))
        self.radioButton.setText(_translate("Dialog", "Turno 1"))
        self.textBrowser_3.setHtml(_translate("Dialog",
            "<p style='font-size:12pt;'>Ingresar Nueva Hora de Entrada</p>"
        ))
        self.leUsuario_3.setText(_translate("Dialog", "HH:MM:SS"))
        self.btnIngresar.setText(_translate("Dialog", "GUARDAR"))
        self.btnIngresar_2.setText(_translate("Dialog", "volver"))




class CambiarHoraController(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar botones
        self.ui.btnIngresar.clicked.connect(self.guardar_cambio)
        self.ui.btnIngresar_2.clicked.connect(self.close)

    def obtener_turno(self):
        if self.ui.radioButton.isChecked():
            return 1
        elif self.ui.radioButton_2.isChecked():
            return 2
        elif self.ui.radioButton_3.isChecked():
            return 3
        return None

    def guardar_cambio(self):
        turno = self.obtener_turno()
        nueva_hora = self.ui.leUsuario_3.text().strip()

        if turno is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un turno.")
            return

        try:
            h, m, s = map(int, nueva_hora.split(":"))
        except:
            QtWidgets.QMessageBox.warning(self, "Error", "Formato inválido. Usa HH:MM:SS")
            return

        horarios = cargar_horarios()
        horarios[turno] = time(h, m)     # Actualizar hora
        guardar_horarios(horarios)

        QtWidgets.QMessageBox.information(self, "Guardado", "Horario actualizado correctamente.")
        self.close()


import prueba_rc


#if __name__ == "__main__":
 #   import sys
  #  app = QtWidgets.QApplication(sys.argv)
   # ventana = CambiarHoraController()
    #ventana.show()
    #sys.exit(app.exec_())