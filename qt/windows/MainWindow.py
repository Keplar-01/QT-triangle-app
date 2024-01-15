from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from qt.generated.ui_mainwindow import Ui_MainWindow
from model.builder import TriangleBuilder
from utils.data_sources.FIleDS import FileDS
from qt.windows.DataBasePage import DataBasePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.calculateBtn.clicked.connect(self.calculate)
        self.ui.fileBtn.clicked.connect(self.readFromFile)
        self.ui.databaseBtn.clicked.connect(self.openDatabasePage)
        # code
        self.show()

    def calculate(self):
        builder = TriangleBuilder()
        triangle = builder.set_first_side(self.ui.firstSideNum.value()).set_second_side(self.ui.secondSideNum.value())\
            .get_triangle()
        self.ui.Hyp.setText(f'{triangle.hypotenuse}')
        self.ui.perimetr.setText(f'{triangle.perimeter}')
        self.ui.area.setText(f'{triangle.area}')

    def readFromFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовые файлы (*.txt);;Все файлы (*)",
                                                   options=options)
        all_triangles = FileDS(file_name).get_list()
        try:
            self.ui.firstSideNum.setValue(all_triangles[0].first_side)
            self.ui.secondSideNum.setValue(all_triangles[0].first_side)
        except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при чтении файла, убедитесь, что в строке лежат два "
                                                     f"числа разделенных пробелом")


    def openDatabasePage(self):
        self.setDisabled(True)
        a = DataBasePage(self)
        a.show()

