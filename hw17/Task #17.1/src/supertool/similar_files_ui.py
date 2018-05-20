from PyQt5 import QtCore, QtWidgets, QtGui
import os

import supertool.similar_files_form as sform
import supertool.table_files_form as tsform
import supertool.similar_files as sf



class SimilarFilesWidget(QtWidgets.QWidget):
    """
    Class of similar files widget
    """

    def __init__(self):
        self.curr_widget = None

        super(SimilarFilesWidget, self).__init__()
        self.ui = sform.Ui_FilesWidget()
        self.ui.setupUi(self)

        self.ui.bottun_folder.clicked.connect(self.button_select_pressed)

        self.clear_data_in_window()

    def button_select_pressed(self):
        """
        Function connected with button_submin_pressed.
        Print weather
        """
        self.ui.bottun_folder.setEnabled(False)
        
        #test_path=os.path.join('C:\\','Users','nosov','PycharmProjects','supertool','src','tests','folder__for_test_1')
        #self.print_similar_files(test_path)

        my_dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            str(os.path.curdir),
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        self.print_similar_files(my_dir)
        self.ui.bottun_folder.setEnabled(True)
    
    def print_similar_files(self,dir):
        self.clear_data_in_window()
        
        self.ui.label_folder.setVisible(True)
        self.ui.line_edit_selected_folder.setVisible(True)
        self.ui.line_edit_selected_folder.setText(dir)
        
        res = sf.work(dir)

        if len(res) == 0:
            self.ui.files_not_found.setVisible(True)
        else:
            for files in res:
                relative_paths=list(map(lambda x:os.path.relpath(x,dir),files))
                table=TableFile(relative_paths)
                current_height = self.ui.scrollAreaWidgetContents.height()
                self.ui.scrollAreaWidgetContents.setFixedHeight(current_height + table.height() + 6)
                self.ui.verticalLayout.addWidget(table)

    def clear_data_in_window(self):
        """
        Clear window to initial state

        :return:
        """
        self.ui.label_folder.setVisible(False)
        self.ui.line_edit_selected_folder.setVisible(False)
        self.ui.files_not_found.setVisible(False)
        self.ui.line.setVisible(False)



        while self.ui.verticalLayout.itemAt(0):
            a = self.ui.verticalLayout.itemAt(0)
            a.widget().close()
            self.ui.verticalLayout.removeItem(a)

        self.ui.scrollArea.setWidgetResizable(False)
        self.ui.scrollAreaWidgetContents.setFixedHeight(20)


class TableFile(QtWidgets.QFrame):
    """
    Class of weather widget for a one date.
    """

    def __init__(self,files_path):
        super(TableFile, self).__init__()
        self.ui = tsform.Ui_Frame_file()
        self.ui.setupUi(self)
        
        for file in files_path:



            line_edit_files=QtWidgets.QLineEdit(self.ui.verticalLayoutWidget)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(line_edit_files.sizePolicy().hasHeightForWidth())

            font = QtGui.QFont()
            font.setPointSize(10)
            font.setWeight(50)
            line_edit_files.setFont(font)

            line_edit_files.setSizePolicy(sizePolicy)
            line_edit_files.setFixedHeight(40)
            line_edit_files.setFixedWidth(680)
            line_edit_files.setReadOnly(True)

            line_edit_files.setText(file)


            self.ui.verticalLayout.addWidget(line_edit_files)

        self.setFixedHeight(40*len(files_path)+20)

