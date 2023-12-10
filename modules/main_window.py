import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt
from division_data import division_by_year, division_by_week, division_date_and_data
from search_functions import search


class Window(QMainWindow):
    def __init__(self):

        self.folderpath = None
        self.destination_folder = None
        self.menu = None
        self.path_orig_data = None

        super(Window, self).__init__()

        self.setWindowTitle("Курс доллара") 
        self.setGeometry(300, 250, 300, 250)
        self.setWindowIcon(QtGui.QIcon('dollar.png'))        

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label1.setObjectName("label1")
        self.label1.setText("Выберете путь к файлу с исходным датасетом:")

        self.path_orig_data = QtWidgets.QLineEdit(self)
        self.path_orig_data.setGeometry(QtCore.QRect(10, 30, 220, 25))
        self.path_orig_data.setObjectName("pathOrigData")

        self.btn_view1 = QtWidgets.QPushButton(self)
        self.btn_view1.setGeometry(QtCore.QRect(237, 30, 45, 25))
        self.btn_view1.setObjectName("btnView1")
        self.btn_view1.setText("Обзор")
        self.btn_view1.clicked.connect(self.select_folder)    

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(10, 60, 271, 41))
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(False)
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")
        self.label2.setText("Выберите папку, в которую хотите записать новый датасет:")

        self.path_write = QtWidgets.QLineEdit(self)
        self.path_write.setGeometry(QtCore.QRect(10, 100, 220, 25))
        self.path_write.setObjectName("pathToWrite")

        self.btn_view2 = QtWidgets.QPushButton(self)
        self.btn_view2.setGeometry(QtCore.QRect(237, 100, 45, 25))
        self.btn_view2.setObjectName("btnView2")
        self.btn_view2.setText("Обзор")
        self.btn_view2.clicked.connect(self.create_dataset)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(20, 140, 251, 20))
        self.label3.setObjectName("label3")
        self.label3.setText("Выберите дату, по которой хотите узнать курс")

        self.date_input = QtWidgets.QDateEdit(self)
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())
        self.date_input.setGeometry(QtCore.QRect(20, 170, 110, 25))
        self.date_input.setObjectName("dateInput")                 

        self.btn_get_data = QtWidgets.QPushButton(self)
        self.btn_get_data.setGeometry(QtCore.QRect(167, 170, 115, 23))
        self.btn_get_data.setObjectName("btnGetData")
        self.btn_get_data.setText("Получить данные")
        self.btn_get_data.clicked.connect(self.get_data)

        self.result = QtWidgets.QTextBrowser(self)
        self.result.setGeometry(QtCore.QRect(20, 210, 260, 30))
        self.result.setObjectName("result")     

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if self.folderpath != "C:/Users/Admin/Desktop/University/2 cours/3 semester/PP/LabAppProg/LabApplicationProgramming/datasets":
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'В этой папке нет нужных данных')
            self.folderpath = None
            self.path_orig_data.clear()
            return
        if self.folderpath:
            QtWidgets.QMessageBox.information(self, 'Папка выбрана', f'Выбрана папка: {self.folderpath}')
        self.folderpath += "/dataset.csv"
        self.path_orig_data.setText(self.folderpath)

    def create_dataset(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        self.destination_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для нового датасета')        
        if self.destination_folder:
            self.menu = SubWindow(self)
            self.menu.show()
        
        self.path_write.setText(self.destination_folder)

    def get_data(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return
        selected_date = self.date_input.date().toString(QtCore.Qt.ISODate)
        self.find_data(selected_date)

    def find_data(self, selected_date):
        course = search(selected_date, self.folderpath)
        if course == None:
            
            self.result.setText(f'Курса доллара на {selected_date} нет')
        else:
            self.result.setText(f'На {selected_date} --> 1$ = {" ".join(course)} ₽')
            

class SubWindow(QDialog):
    def __init__(self, Main: Window = None):
        super(SubWindow, self).__init__(Main)

        self.setWindowTitle("Деление на файлы")
        self.setGeometry(300, 300, 290, 200)

        if Main is not None:
            self.Main = Main

        self.btn_div_xy = QtWidgets.QPushButton(self)
        self.btn_div_xy.setText("Разделить на X и Y")
        self.btn_div_xy.setGeometry(QtCore.QRect(10, 20, 270, 50))
        self.btn_div_xy.clicked.connect(self.btn_xy)

        self.btn_div_year = QtWidgets.QPushButton(self)
        self.btn_div_year.setText("Разделить по годам")
        self.btn_div_year.setGeometry(QtCore.QRect(10, 80, 270, 50))
        self.btn_div_year.clicked.connect(self.btn_year)        

        self.btn_div_week = QtWidgets.QPushButton(self)
        self.btn_div_week.setText("Разделить по неделям")        
        self.btn_div_week.setGeometry(QtCore.QRect(10, 140, 270, 50))
        self.btn_div_week.clicked.connect(self.btn_week)
        

    def btn_xy(self):
        division_date_and_data(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                          f'Датасет "date_and_data" создан и сохранен в {self.Main.destination_folder}')
        self.close()

    def btn_year(self):
        division_by_year(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                          f'Датасет "data_by_year" создан и сохранен в {self.Main.destination_folder}')
        self.close()

    def btn_week(self):
        division_by_week(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                          f'Датасет "data_by_week" создан и сохранен в {self.Main.destination_folder}')
        self.close()

def application():
    app = QApplication(sys.argv)
    window = Window()    

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()