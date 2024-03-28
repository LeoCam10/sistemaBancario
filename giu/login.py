import sys
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic

sys.path.append('/Users/camus/Desktop/banco/data')
from usuario import UsuarioData
from model.usuario import Usuario
from giu.main import MainWindow



class Login():
    def __init__(self):
        self.login = uic.loadUi("giu/login.ui")
        self.initGui()
        self.login.lblmensaje.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.txtusuario.text()) < 2:
            self.login.lblmensaje.setText("ingrese un usuario valido")
            self.login.txtusuario.setFocus()
        elif len(self.login.txtclave.text()) < 3:
            self.login.lblmensaje.setText("ingrese una contrasena valida")
            self.login.txtclave.setFocus()
        else:
            self.login.lblmensaje.setText("")
            usu = Usuario(usuario=self.login.txtusuario.text(),clave=self.login.txtclave.text())
            usuDate= UsuarioData()
            res = usuDate.login(usu)
            if res:
               self.main = MainWindow()
               #self.main.showMaximized()
               self.login.hide()
            else: 
                 self.login.lblmensaje.setText("DATOS DE ACCESO INCORRECTOS")
            
    def initGui(self):
        self.login.btnacceder.clicked.connect(self.ingresar)