import sys
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QMainWindow
sys.path.append('/Users/camus/Desktop/banco/model')
from movimiento import Transferencia
sys.path.append('/Users/camus/Desktop/banco/data')
from transferencia import TransferenciaData
sys.path.append('/Users/camus/Desktop/banco/data')
from deposito import DepositoData
sys.path.append('/Users/camus/Desktop/banco/model')
from movimiento import DepositoInternacional
sys.path.append('/Users/camus/Desktop/banco/data')
from historial import HistorialData
import datetime
from PyQt6.QtWidgets import QTableWidgetItem



from ciudad import CiudadData
from PyQt6 import uic
from PyQt6.QtCore import QDate


class MainWindow():
    def __init__(self):
       
        self.main = uic.loadUi("giu/main.ui")
        self.initGui()
        self.main.showMaximized()
   
    def initGui(self):
        self.main.btnRealizarTransferencias.triggered.connect(lambda : self.abrir_registro())
        self.main.btnReportarTransferencia.triggered.connect(lambda : self.abrir_deposito())
        self.main.btnHistorialTransferencias.triggered.connect(lambda : self.abrir_historial())
        self.registro = uic.loadUi("giu/registro.ui")
        self.deposito = uic.loadUi("giu/deposito.ui")
        self.historial = uic.loadUi("giu/historial.ui")
   
    def abrir_registro(self):
        self.registro.btnregistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()

    def abrir_deposito(self):
       
        self.deposito.btnregistrarDeposito.clicked.connect(self.registrarDeposito)
        self.deposito.show()
        self.llenarComboCiudades()

    def abrir_historial(self):
       
        self.historial.btnbuscar.clicked.connect(self.buscar)
        self.historial.tblhistorial.setColumnWidth(0,50)
        self.historial.tblhistorial.setColumnWidth(1,250)
        self.historial.tblhistorial.setColumnWidth(2,100)
        self.historial.tblhistorial.setColumnWidth(3,250)
        self.historial.tblhistorial.setColumnWidth(4,150)
        self.historial.tblhistorial.setColumnWidth(5,60)
        self.historial.show()
        self.llenarTablaHistorial()
##################TRANSFERENCIA#######################################
    def registrarTransferencia(self):
        if  self.registro.cbtipo.currentText() == "-- Seleccione una opcion":
            mbox = QMessageBox()
            mbox.setText("debe seleccionar el tipo de documento")
            mbox.exec()
            self.registro.cbtipo.setFocus()
        elif len(self.registro.txtdocumento.text())<4:
            mbox = QMessageBox()
            mbox.setText("debe ingresar un documento valido")
            mbox.exec()
            self.registro.txtdocumento.setFocus()
        elif self.registro.cbmotivo.currentText() == "-- Seleccione una opcion":
            mbox = QMessageBox()
            mbox.setText("debe seleccionar un motivo valido")
            mbox.exec()
            self.registro.cbmotivo.setFocus()
        elif not (self.registro.txtmonto.text()).isnumeric():
            mbox = QMessageBox()
            mbox.setText("ddebe ingresar un monto valida")
            mbox.exec()
            self.registro.txtmonto.setText("0")
            self.registro.txtmonto.setFocus()
        else:
             transferencia=Transferencia(tipo = self.registro.cbtipo.currentText(),documento = self.registro.txtdocumento.text(),
                             monto = float(self.registro.txtmonto.text()), dolares = self.registro.checkinternacional.isChecked(), internacional=self.registro.checkinternacional.isChecked(),motivo= self.registro.cbmotivo.currentText())
        print('tran :', str(self.registro.checkinternacional.isChecked()))
        print('dolar :', str(self.registro.checkdolares.isChecked()))

        objdata = TransferenciaData()
        mbox = QMessageBox()
        if objdata.registrar(transferencia):
            mbox.setText("Transferencia registrada")
            self.limpiarCamposTransferencias()
        else:
             mbox.setText("Transferencia NO registrada")
        mbox.exec()

    def limpiarCamposTransferencias(self):
        self.registro.cbtipo.setCurrentIndex(0)
        self.registro.cbmotivo.setCurrentIndex(0)
        self.registro.txtdocumento.setText("")
        self.registro.txtmonto.setText("0")
        self.registro.checkdolares.setChecked(False)
        self.registro.checkinternacional.setChecked(False)

####################DEPOSITO###########################################

    def llenarComboCiudades(self):
        objData = CiudadData()
        datos = objData.listarCiudades()
        for item in datos:
             print(item)
             self.deposito.cblugarnacimiento.addItem(item[1])

    def validarCamposObligatorios(self):
    
        if  not self.deposito.txtdocumento.text() or not self.deposito.txtprimernombre.text() or not self.deposito.txtprimerapellido.text() or not self.deposito.txtmonto.text()or self.deposito.cbtipo.currentText() == "-- Seleccione una opcion"  or  self.deposito.cblugarnacimiento.currentText() == "-- Seleccione una opcion" or self.deposito.cbsexo.currentText() == "-- Seleccione una opcion" or self.deposito.cbmotivogiro.currentText() == "-- Seleccione una opcion":       
             return False
            
        else:
             return True

    
    def registrarDeposito(self):
        mbox = QMessageBox()
        if not self.validarCamposObligatorios():
            
            mbox.setText("debe completar los campos obligatorios (*)")
          
        elif self.deposito.checkterminos.isChecked() == False:
             mbox.setText("debe aceptar los terminos")
        elif  not self.deposito.txtmonto.text().isnumeric() or float(self.deposito.txtmonto.text()) < 1:
            mbox = QMessageBox()
            mbox.setText("El monto debe ser mayor a 0")
            self.deposito.txtmonto.setText("0")
            mbox.exec()
            
            self.deposito.txtmonto.setFocus()
             
        else:
             fechaN = self.deposito.datefechanacimiento.date().toPyDate()
             deposito = DepositoInternacional(monto = float(self.deposito.txtmonto.text()),tipo = self.deposito.cbtipo.currentText(),documento = self.deposito.txtdocumento.text(),
                             nombre1 = self.deposito.txtprimernombre.text(),nombre2 = self.deposito.txtsegundonombre.text(), apellido1 = self.deposito.txtprimerapellido.text(),
                             apellido2 = self.deposito.txtsegundoapellido.text(), sexo = self.deposito.cbsexo.currentText(),internacional = True, dolares = True,
                             fechanacimiento = fechaN  ,lugarnacimiento = self.deposito.cblugarnacimiento.currentText(), 
                             terminos = self.deposito.checkterminos.isChecked(), motivo=self.deposito.cbmotivogiro.currentText())  
                            
        

             objdata = DepositoData()
             
             if objdata.registrar(deposito):
                mbox.setText("Deposito registrado")
                self.limpiarCamposDepositos()
            
             else:
                 mbox.setText("Deposito NO registrado")
        mbox.exec()

    def limpiarCamposDepositos(self):
        fecha = QDate(2000, 1, 1)
        self.deposito.cbtipo.setCurrentIndex(0)
        self.deposito.cbmotivogiro.setCurrentIndex(0)
        self.deposito.cbsexo.setCurrentIndex(0)
        self.deposito.cblugarnacimiento.setCurrentIndex(0)
        self.deposito.txtdocumento.setText("")
        self.deposito.txtprimernombre.setText("")
        self.deposito.txtsegundonombre.setText("")
        self.deposito.txtprimerapellido.setText("")
        self.deposito.txtsegundoapellido.setText("")
        self.deposito.datefechanacimiento.setDate(fecha)
        self.deposito.txtmonto.setText("0")
        self.deposito.checkterminos.setChecked(False)
        
##########################HISTORIAL##############################
        
    def buscar(self):
        his = HistorialData()
        desde = self.historial.datefechadesde.dateTime().toString("yyyy-MM-dd")
        hasta = self.historial.datefechahasta.dateTime().toString("yyyy-MM-dd")
        #data = his.buscarPorFecha(self.historial.cbtipo.currentText(), self.historial.txtdocumento.text())
        data = his.buscarPorFecha(desde,hasta, self.historial.cbtipo.currentText(), self.historial.txtdocumento.text())    
        print(data)
        fila = 0
        
        canti= self.historial.tblhistorial.setRowCount(len(data))
        print(canti)
        for item in data:
            self.historial.tblhistorial.setItem(fila,0,QTableWidgetItem(str(item[0])))
            #self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem(str(item[14])))
            self.historial.tblhistorial.setItem(fila,4,QTableWidgetItem(str(item[11])))
            self.historial.tblhistorial.setItem(fila,5,QTableWidgetItem(" SI "))

            self.historial.tblhistorial.setItem(fila, 1, QTableWidgetItem("{} {} {} {}".format(str(item[4]), str(item[5]), str(item[6]), str(item[7]))))
            
            if str(item[10]) == 'True':
               self.historial.tblhistorial.setItem(fila,2,QTableWidgetItem("USD " + str(item[1])))
            else: 
                 self.historial.tblhistorial.setItem(fila,2,QTableWidgetItem("$ " + str(item[1])))

            if str(item[9]) == 'True':
               self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Internacional : " + str(item[15])))
            else: 
                 self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Nacional : " + str(item[15])))
                
            if str(item[9]) == 'True':
               self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Internacional : " + str(item[15])))
            else: 
                 self.historial.tblhistorial.setItem(fila,3,QTableWidgetItem("Transferencia Nacional : " + str(item[15])))
            
            fila = fila +1

    def llenarTablaHistorial(self):
        
        pass