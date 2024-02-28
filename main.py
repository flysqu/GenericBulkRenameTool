import functions
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import sys
from os import rename, path
import random

class MyWidget(QtWidgets.QWidget):

    def load_files_button_clicked(self):
        print("Load Files button clicked")

        path = window.directory_input.text()
        files = functions.list_files(path)
        files.sort()

        files_after = window.files_after
        files_before = window.files_before

        files_after.clear()
        files_before.clear()

        files_after.insertItems(0, files)
        files_before.insertItems(0, files)


    def refresh_button_clicked(self):
        print("Refresh button clicked")
        # Initializing Variables

            # Buttons
        load_files_button = window.load_files_button
        refresh_button = window.refresh_button
        save_to_files_button = window.save_to_files_button

            # Insert Text
        it_position_spinbox = window.it_position_spinbox
        it_text_input = window.it_text_input

            # Remove Characters
        rc_from_spinbox = window.rc_from_spinbox
        rc_to_spinbox = window.rc_to_spinbox

            # Search And Replace
        sr_search_input = window.sr_search_input
        sr_replace_input = window.sr_replace_input

            # Misc
        directory_input = window.directory_input
        files_after = window.files_after
        files_before = window.files_before

        

        # GET ITEMS IN FILES_BEFORE TO LIST
        items = []
        for x in range(files_before.count()):
            items.append(files_before.item(x).text())

        items_after = []
        # RUN LIST THROUGH ALL* FUNCTIONS IN FUNCTIONS.PY AND GET NEW LIST FROM RESULT
        for item in items:
            item = functions.search_and_replace(sr_search_input.text(), sr_replace_input.text(), item)
            item = functions.insert_text(it_text_input.text(), it_position_spinbox.value(), item)
            item = functions.remove_characters(rc_from_spinbox.value(), rc_to_spinbox.value(), item)

            items_after.append(item)

        # PUT THAT NEW LIST INTO FILES_AFTER
        files_after.clear()
        files_after.insertItems(0, items_after)


    def save_to_files_button_clicked(self):
        print("Save to Files button clicked")
        
        directory_input = window.directory_input
        directory = directory_input.text()

        files_after = window.files_after
        files_before = window.files_before

        old_filenames = []
        for x in range(files_before.count()):
            old_filenames.append(files_before.item(x).text())

        new_filenames = []
        for x in range(files_after.count()):
            new_filenames.append(files_after.item(x).text())

        for x in range(len(old_filenames)):
            oldnamepath = path.join(directory,old_filenames[x])
            newnamepath = path.join(directory,new_filenames[x])

            rename(oldnamepath,newnamepath)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "forms/genericbulkrenametool.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    
    # Connect button signals to functions
    widget = MyWidget()
    window.load_files_button.clicked.connect(widget.load_files_button_clicked)
    window.refresh_button.clicked.connect(widget.refresh_button_clicked)
    window.save_to_files_button.clicked.connect(widget.save_to_files_button_clicked)

    window.show()

    sys.exit(app.exec())
