# coding: utf-8

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
# from PyQt5.uic import loadUi
from .ui.Ui_NotesWidget import Ui_Form

from core.NoteModel import NoteModel
from gui.NoteEditDialog import NoteEditDialog


class NotesWidget(QWidget, Ui_Form):
    selection_changed = pyqtSignal(list, name='selectionChanged')

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_model(model)
        self.__init_ui()
        self.__init_signals()

    def __init_ui(self):
        self.setupUi(self)

        self.notesView.setModel(self.__model)
        self.notesView.resizeColumnsToContents()

    def __init_signals(self):
        self.notesView.doubleClicked.connect(self.edit_note)
        self.notesView.selectionModel().selectionChanged.connect(
            self.__on_selection_changed
        )

    def __on_selection_changed(self):
        self.selection_changed.emit(
            self.selected_rows()
        )

    def __init_model(self, model):
        if isinstance(model, NoteModel):
            self.__model = model
            self.__model.select()
        else:
            raise RuntimeError('Переданная модель не NoteModel')

    #закрытый метод
    #d - локальная переменная, уничтожится при закрытии диалога
    def __open_edit_dialog(self, row = None, title = None):
        d = NoteEditDialog(model=self.__model, row = row, parent=self)
        d.ready.connect(self.on_ready)

        if title:
            d.setWindowTitle(title)

        d.exec_()

    def on_ready(self, state, row):
        self.notesView.setCurrentIndex(
            self.__model.index(row, 0)
        )

        if state:
            self.notesView.resizeColumnsToContents()

    def add_new_note(self):
        self.__open_edit_dialog()

    def edit_note(self, index):
        self.__open_edit_dialog(row=index.row(),
                                title=u'Редактирование заметки') #index - это объект, метод row() позволяет получить
                                                                # номер строки, без u будет кракозябра

    def edit_selected_note(self):
        selected = self.selected_rows()

        if len(selected) == 1:
            self.edit_note(selected.pop()) # selected[0]

    def remove_notes(self, indexes):
        indexes.sort(reverse = True)

        for index in indexes:
            self.__model.removeRow(index.row()) #qmodel index - eto ob'ekt s nomerom stroki i stolbca
                                                #есть метод isvalid - проверяет валидность

        self.__model.select()

    def remove_selected_notes(self):
        self.remove_notes(self.selected_rows())

    def selected_rows(self):
        return self.notesView.selectionModel().selectedRows()
