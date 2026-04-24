from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("./dev/screen/activeScreen/menu/chatMenu/chatWidget.ui", self)

        self.NEW_CHAT_INDEXES = []

        # some default settings
        if True:
            # if no chats were saved, start with new chat else load chats
            self.start_newChat()
            self.chatsStackedWidget.setCurrentIndex(0)  

        # setting up connections
        self.btn_new_chat.clicked.connect(self.start_newChat)
        self.btn_send_querry.clicked.connect(self.btn_sendquerry)
        self.comboBox.currentIndexChanged.connect(self.change_current_chat)
    
    def start_newChat(self):
        self.chatsStackedWidget.setCurrentIndex(0)
        self.comboBox.addItem("new chat")
        self.comboBox.setCurrentIndex(self.comboBox.count()-1)
        self.NEW_CHAT_INDEXES.append(self.comboBox.currentIndex())
        # print(f"list - {self.NEW_CHAT_INDEXES}")

    def btn_sendquerry(self):
        text = self.TextEdit.toPlainText()
        self.TextEdit.setPlainText("")

        self.comboBox.setItemText(self.comboBox.currentIndex(), text[:11])

        newactivechat = self.chat_0
        newactivechat.setObjectName("chat_1")
        # newactivechat.TEMP_TEXT_SEND_3.setText(text)
        self.chatsStackedWidget.addWidget(newactivechat)

        self.NEW_CHAT_INDEXES.remove(self.comboBox.currentIndex())
        self.change_current_chat()
        # print(f"list - {self.NEW_CHAT_INDEXES}")

    def change_current_chat(self):
        if self.comboBox.currentIndex() not in self.NEW_CHAT_INDEXES:
            self.chatsStackedWidget.setCurrentIndex(self.comboBox.currentIndex() + 1)
        else:
            self.chatsStackedWidget.setCurrentIndex(0)
            # print(f"list - {self.NEW_CHAT_INDEXES}")

        for i in self.chatsStackedWidget.children():
            pass
            # print(i.objectName())

        

