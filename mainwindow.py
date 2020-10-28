from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.finalcap.clicked.connect(self.click_agregarfinal)
        self.ui.Iniciocap.clicked.connect(self.click_agregarinicio)      
        self.ui.Mostrar.clicked.connect(self.click_mostrar)

    

    @Slot()
    def click_agregarfinal(self):
        IDD = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()
        Blue = self.ui.Azul.value()
        Green = self.ui.Verde.value()   

        particula = Particula(IDD,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        self.particulas.agregar_final(particula)
        
        #print(particula)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_agregarinicio(self):
        IDD = self.ui.ID.value()
        Ox = self.ui.OrigenX.value()   
        Oy = self.ui.OrigenY.value() 
        Dx = self.ui.DestinoX.value()
        Dy = self.ui.DestinoY.value()
        Vel = self.ui.Velocidad.value()
        Red = self.ui.Rojo.value()
        Blue = self.ui.Azul.value()
        Green = self.ui.Verde.value()

        particula = Particula(IDD,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        self.particulas.agregar_inicio(particula)

        #print(IDD,Ox,Oy,Dx,Dy,Vel,Red,Blue,Green)
        #self.ui.salida.insertPlainText(str(IDD)+str(Ox)+str(Oy)+str(Dx)+str(Dy)+str(Vel)+str(Red)+str(Blue)+str(Green))

    @Slot()
    def click_mostrar(self):
       # self.particulas.mostrar()
       self.ui.salida.clear()
       self.ui.salida.insertPlainText(str(self.particulas))
