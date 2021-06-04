# -*- coding: utf-8 -*-

import main

from os import stat_result
from PyQt5 import QtCore, QtGui, QtWidgets

import json


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)
        self.game_state = None
        self.reset_game()

        self.depth = 2

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("color: white;""background-color: #222840;")

        ###########################  frames ###########################

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(55, 10, 760, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # self.frame.setStyleSheet("color: white;""background-color: red;")

        self.bts_frame = QtWidgets.QFrame(self.centralwidget)
        self.bts_frame.setGeometry(QtCore.QRect(90, 440, 761, 101))
        self.bts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bts_frame.setObjectName("bts_frame")

        ######################   fonts  #########################
        bt_font = QtGui.QFont()
        bt_font.setPointSize(14)
        bt_font.setBold(True)
        bt_font.setWeight(75)

        lb_font = QtGui.QFont()
        lb_font.setPointSize(14)
        lb_font.setBold(True)
        lb_font.setWeight(75)

        ######################   Buttons  #########################

        self.pocket1 = QtWidgets.QPushButton(self.frame)
        self.pocket1.setGeometry(QtCore.QRect(120, 340, 60, 60))
        self.pocket1.setFont(bt_font)
        self.pocket1.setDefault(False)
        self.pocket1.setFlat(False)
        self.pocket1.setObjectName("pocket1")

        self.pocket1.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        # self.pocket1.setStyleSheet(
        #     "color: white;""background-color: grey;""border-radius : 30px; border : 2px solid white")

        self.pocket2 = QtWidgets.QPushButton(self.frame)
        self.pocket2.setGeometry(QtCore.QRect(220, 340, 60, 60))
        self.pocket2.setFont(bt_font)
        self.pocket2.setObjectName("pocket2")
        self.pocket2.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket3 = QtWidgets.QPushButton(self.frame)
        self.pocket3.setGeometry(QtCore.QRect(300, 340, 60, 60))
        self.pocket3.setObjectName("pocket3")
        self.pocket3.setFont(bt_font)
        self.pocket3.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket4 = QtWidgets.QPushButton(self.frame)
        self.pocket4.setGeometry(QtCore.QRect(380, 340, 60, 60))
        self.pocket4.setObjectName("pocket4")
        self.pocket4.setFont(bt_font)
        self.pocket4.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket5 = QtWidgets.QPushButton(self.frame)
        self.pocket5.setGeometry(QtCore.QRect(470, 340, 60, 60))
        self.pocket5.setObjectName("pocket5")
        self.pocket5.setFont(bt_font)
        self.pocket5.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket6 = QtWidgets.QPushButton(self.frame)
        self.pocket6.setGeometry(QtCore.QRect(570, 340, 60, 60))
        self.pocket6.setObjectName("pocket6")
        self.pocket6.setFont(bt_font)
        self.pocket6.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket7 = QtWidgets.QPushButton(self.frame)
        self.pocket7.setGeometry(QtCore.QRect(570, 50, 60, 60))
        self.pocket7.setObjectName("pocket7")
        self.pocket7.setFont(bt_font)
        self.pocket7.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket8 = QtWidgets.QPushButton(self.frame)
        self.pocket8.setGeometry(QtCore.QRect(470, 50, 60, 60))
        self.pocket8.setObjectName("pocket8")
        self.pocket8.setFont(bt_font)
        self.pocket8.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket9 = QtWidgets.QPushButton(self.frame)
        self.pocket9.setGeometry(QtCore.QRect(380, 50, 60, 60))
        self.pocket9.setObjectName("pocket9")
        self.pocket9.setFont(bt_font)
        self.pocket9.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket10 = QtWidgets.QPushButton(self.frame)
        self.pocket10.setGeometry(QtCore.QRect(300, 50, 60, 60))
        self.pocket10.setObjectName("pocket10")
        self.pocket10.setFont(bt_font)
        self.pocket10.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket11 = QtWidgets.QPushButton(self.frame)
        self.pocket11.setGeometry(QtCore.QRect(220, 50, 60, 60))
        self.pocket11.setObjectName("pocket11")
        self.pocket11.setFont(bt_font)
        self.pocket11.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.pocket12 = QtWidgets.QPushButton(self.frame)
        self.pocket12.setGeometry(QtCore.QRect(120, 50, 60, 60))
        self.pocket12.setObjectName("pocket12")
        self.pocket12.setFont(bt_font)
        self.pocket12.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 3px solid white")

        self.mankla1 = QtWidgets.QPushButton(self.frame)
        self.mankla1.setGeometry(QtCore.QRect(640, 100, 75, 260))
        self.mankla1.setFont(bt_font)
        self.mankla1.setObjectName("mankla1")
        self.mankla1.setStyleSheet(
            "color: white;""background-color: grey;")

        self.mankla2 = QtWidgets.QPushButton(self.frame)
        self.mankla2.setGeometry(QtCore.QRect(20, 100, 75, 260))
        self.mankla2.setFont(bt_font)
        self.mankla2.setObjectName("mankla2")
        self.mankla2.setStyleSheet(
            "color: white;""background-color: grey;")

        ##############  start / save /load  ##########

        self.start_bt = QtWidgets.QPushButton(self.bts_frame)
        self.start_bt.setGeometry(QtCore.QRect(220, 40, 121, 31))
        self.start_bt.setFont(lb_font)
        self.start_bt.setObjectName("start_bt")
        self.start_bt.setStyleSheet("background-color: green;")

        self.load_bt = QtWidgets.QPushButton(self.bts_frame)
        self.load_bt.setGeometry(QtCore.QRect(380, 40, 121, 31))
        self.load_bt.setFont(lb_font)
        self.load_bt.setObjectName("load_bt")
        self.load_bt.setStyleSheet("background-color: grey;")

        self.save_bt = QtWidgets.QPushButton(self.bts_frame)
        self.save_bt.setGeometry(QtCore.QRect(540, 40, 121, 31))
        self.save_bt.setFont(lb_font)
        self.save_bt.setObjectName("save_bt")
        self.save_bt.setStyleSheet("background-color: grey;")

        ######################   labels  #########################
        self.player1_lb = QtWidgets.QLabel(self.frame)
        self.player1_lb.setGeometry(QtCore.QRect(320, 10, 160, 20))
        self.player1_lb.setFont(lb_font)
        self.player1_lb.setObjectName("player1_lb")

        self.player2_lb = QtWidgets.QLabel(self.frame)
        self.player2_lb.setGeometry(QtCore.QRect(320, 400, 160, 20))
        self.player2_lb.setFont(lb_font)
        self.player2_lb.setObjectName("player2_lb")

        self.stealing_lb = QtWidgets.QRadioButton(self.bts_frame)
        self.stealing_lb.setGeometry(QtCore.QRect(30, 5, 111, 31))
        self.stealing_lb.setFont(lb_font)
        self.stealing_lb.setObjectName("stealing_lb")

        # self.player_1st= QtWidgets.QRadioButton(self.bts_frame)

        self.player_1st = QtWidgets.QCheckBox(self.bts_frame)
        self.player_1st.setGeometry(QtCore.QRect(30, 30, 160, 31))
        self.player_1st.setFont(lb_font)
        self.player_1st.setObjectName("player_1st")
        self.player_1st.setText("playing First")

        self.mode = QtWidgets.QComboBox(self.bts_frame)
        self.mode.setGeometry(QtCore.QRect(30, 65, 160, 31))
        self.mode.setFont(lb_font)
        self.mode.setObjectName("mode")
        self.mode.addItems(["Easy", "Medium", "Hard"])


        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Winner Player")

        # self.msg.setText(" Player 1 is Winner    ")
        # x = self.msg.exec_()



        ######################   fonts  #########################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pocket1.clicked.connect(self.pkt1)
        self.pocket2.clicked.connect(self.pkt2)
        self.pocket3.clicked.connect(self.pkt3)
        self.pocket4.clicked.connect(self.pkt4)
        self.pocket5.clicked.connect(self.pkt5)
        self.pocket6.clicked.connect(self.pkt6)
        self.pocket7.clicked.connect(self.pkt7)
        self.pocket8.clicked.connect(self.pkt8)
        self.pocket9.clicked.connect(self.pkt9)
        self.pocket10.clicked.connect(self.pkt10)
        self.pocket11.clicked.connect(self.pkt11)
        self.pocket12.clicked.connect(self.pkt12)
        self.start_bt.clicked.connect(self.start)
        self.load_bt.clicked.connect(self.load)
        self.save_bt.clicked.connect(self.save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################functions ###################

    def pkt1(self):
        self.play(0)

    def pkt2(self):
        self.play(1)

    def pkt3(self):
        self.play(2)

    def pkt4(self):
        self.play(3)

    def pkt5(self):
        self.play(4)

    def pkt6(self):
        self.play(5)

    def pkt7(self):
        pass

    def pkt8(self):
        pass

    def pkt9(self):
        pass

    def pkt10(self):
        pass

    def pkt11(self):
        pass

    def pkt12(self):
        pass

    def save(self):
        # self.save_state_file(self.get_game_state())
        self.get_game_state()
        # print(self.get_game_state())
        pass

    def load(self):
        self.load_state_file()
        self.set_game_state()
        # self.stealing_lb.setCheckable(False)

    def start(self):
        if self.player_1st.isChecked():
            self.game_state['player'] = 1
        else:
            self.game_state['player'] = 0

        if self.stealing_lb.isChecked():
            self.game_state['is_stealing'] = 1

        else:
            self.game_state['is_stealing'] = 0
        print(self.game_state)

        # self.player_1st.setTriState()
        self.player_1st.setCheckable(self.player_1st.isChecked())
        self.start_bt.setStyleSheet("background-color: grey;")

        ########## here take the text and select dipth #############
        if self.mode.currentIndex() == 1:
            self.depth = 5
        elif self.mode.currentIndex() == 2:
            self.depth = 8
        else:
            self.depth = 2

    ######################### help functions #########################

    def play(self, pocket_number=-1):
        if self.game_state['player'] == 1 and pocket_number >= 0:
            self.bt_color()
            new_state = main.do_step(self.game_state, pocket_number)
            if new_state is not None:
                self.game_state = new_state
                self.set_game_state()

        elif self.game_state['player'] == 0:

            self.clear_color()
            # TODO: path depth depending on the game hardness
            self.game_state = main.AI_play(self.game_state, self.depth)
            self.set_game_state()
            self.bt_color()
        # winner = main.winner(self.game_state)
        # if winner is not None:
        #     if self.game_state['player'] == 0:
        #
        #         self.msg.setText("Player 2 is Winner ")
        #     else:
        #         self.msg.setText("Player 1 is Winner ")
        #         self.msg.exec_()
        #     self.reset_game()

    def reset_game(self):
        self.game_state = {
            "player": 1,
            "score": 0,
            "is_stealing": 0,
            "mancala_state": [4, 4, 4, 4, 4, 4, 0,
                              4, 4, 4, 4, 4, 4, 0],
            "steps": []
        }
        self.set_game_state()

    def bt_color(self):

        self.player1_lb.setStyleSheet("color: red;")
        self.player2_lb.setStyleSheet("color: green;")

        self.mankla1.setStyleSheet("color: white;""background-color: grey;" "border : 4px solid green")
        self.mankla2.setStyleSheet("color: white;""background-color: grey;" "border : 4px solid white")

        self.pocket1.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket2.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket3.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket4.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket5.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket6.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")

        self.pocket7.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket8.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket9.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket10.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket11.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket12.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")

        pass

    def clear_color(self):
        self.player1_lb.setStyleSheet("color: green;")
        self.player2_lb.setStyleSheet("color: red;")

        self.mankla2.setStyleSheet("color: white;""background-color: grey;" "border : 4px solid green")
        self.mankla1.setStyleSheet("color: white;""background-color: grey;" "border : 4px solid white")

        self.pocket1.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket2.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket3.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket4.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket5.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")
        self.pocket6.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid white")

        self.pocket7.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket8.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket9.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket10.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket11.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")
        self.pocket12.setStyleSheet(
            "color: white;""background-color: grey;""border-radius : 30px; border : 4px solid green")

        pass

    def is_stealing(self):
        # 1 if stealing   / 0  not stealing
        return self.stealing_lb.isChecked()

    def load_state_file(self):
        try:
            with open('save.json', 'r') as f:
                self.game_state = json.load(f)
        except Exception as e:
            print(f'error while loading save.json, with error: {e}')

    def set_game_state(self):

        self.pocket1.setText(str(self.game_state['mancala_state'][7]))
        self.pocket2.setText(str(self.game_state['mancala_state'][8]))
        self.pocket3.setText(str(self.game_state['mancala_state'][9]))
        self.pocket4.setText(str(self.game_state['mancala_state'][10]))
        self.pocket5.setText(str(self.game_state['mancala_state'][11]))
        self.pocket6.setText(str(self.game_state['mancala_state'][12]))
        self.mankla1.setText(str(self.game_state['mancala_state'][13]))

        self.pocket7.setText(str(self.game_state['mancala_state'][0]))
        self.pocket8.setText(str(self.game_state['mancala_state'][1]))
        self.pocket9.setText(str(self.game_state['mancala_state'][2]))
        self.pocket10.setText(str(self.game_state['mancala_state'][3]))
        self.pocket11.setText(str(self.game_state['mancala_state'][4]))
        self.pocket12.setText(str(self.game_state['mancala_state'][5]))
        self.mankla2.setText(str(self.game_state['mancala_state'][6]))

        if self.game_state['is_stealing'] is True:
            # self.stealing_lb.setChecked(True)
            self.stealing_lb.nextCheckState()
            # self.stealing_lb.setCheckable(False)
        else:
            # self.stealing_lb.setChecked(False)
            self.stealing_lb.nextCheckState()
        QtWidgets.QApplication.processEvents()
        winner = main.winner(self.game_state)
        if winner is None:
            self.play()
        else:
            if winner == 0:

                self.msg.setText("Player 2 is Winner ")
            elif winner == 1:
                self.msg.setText("Player 1 is Winner ")
            else:
                self.msg.setText("It's a tie")
            self.msg.exec_()
            self.reset_game()

    def get_game_state(self):

        import json

        with open('save.json', 'w') as f:
            json.dump(self.game_state, f, indent=4)
        # # file_state= open("save.json",'w+')
        # file_state = open(r"E:\4th computer\2nd_term\AI\project\save.json", 'r')
        #
        # prev_state = file_state.read()
        # print(prev_state)
        #
        # # list to dictionery
        # ps = json.loads(prev_state)
        # print(ps)
        #
        # ps['mancala_state'].clear()
        # print(ps['mancala_state'])
        #
        # ps['mancala_state'].append(self.pocket1.text())
        # ps['mancala_state'].append(self.pocket2.text())
        # ps['mancala_state'].append(self.pocket3.text())
        # ps['mancala_state'].append(self.pocket4.text())
        # ps['mancala_state'].append(self.pocket5.text())
        # ps['mancala_state'].append(self.pocket6.text())
        # ps['mancala_state'].append(self.mankla1.text())
        # ps['mancala_state'].append(self.pocket7.text())
        # ps['mancala_state'].append(self.pocket8.text())
        # ps['mancala_state'].append(self.pocket9.text())
        # ps['mancala_state'].append(self.pocket10.text())
        # ps['mancala_state'].append(self.pocket11.text())
        # ps['mancala_state'].append(self.pocket12.text())
        # ps['mancala_state'].append(self.mankla2.text())
        #
        # print(ps)
        # ps['stealing'] = self.is_stealing()
        # ps2 = json.dumps(ps).replace("'", '"')
        #
        # file_state.close()
        #
        # file_state = open(r"E:\4th computer\2nd_term\AI\project\save.json", 'w')
        #
        # # convert dic to list
        # # list=[]
        # # temp=[]
        #
        # # for key, value in ps.items():
        # #     temp = [key,value]
        # #     list.append(temp)
        #
        # print(ps2)
        # file_state.writelines(ps2)
        # file_state.close()
        #
        # # return mankala_state

        # ##################### not used #############
        # def save_state_file(self, curent_state):
        #     import json
        #
        #     # file_state= open("save.json",'w+')
        #     file_state = open(r"E:\4th computer\2nd_term\AI\project\save.json", 'w+')
        #
        #     prev_state = file_state.readlines()
        #     ps = json.loads(prev_state[0])
        #     file_state.writelines(curent_state)
        #     file_state.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pocket2.setText(_translate("MainWindow", "4"))
        self.pocket4.setText(_translate("MainWindow", "4"))
        self.pocket3.setText(_translate("MainWindow", "4"))
        self.pocket1.setText(_translate("MainWindow", "4"))
        self.pocket5.setText(_translate("MainWindow", "4"))
        self.pocket6.setText(_translate("MainWindow", "4"))
        self.pocket9.setText(_translate("MainWindow", "4"))
        self.pocket8.setText(_translate("MainWindow", "4"))
        self.pocket10.setText(_translate("MainWindow", "4"))
        self.pocket7.setText(_translate("MainWindow", "4"))
        self.pocket11.setText(_translate("MainWindow", "4"))
        self.pocket12.setText(_translate("MainWindow", "4"))
        self.mankla2.setText(_translate("MainWindow", "0"))
        self.mankla1.setText(_translate("MainWindow", "0"))
        self.player2_lb.setText(_translate("MainWindow", "Player 1"))
        self.player1_lb.setText(_translate("MainWindow", "Player 2"))
        self.start_bt.setText(_translate("MainWindow", "start"))
        self.stealing_lb.setText(_translate("MainWindow", "stealing"))
        self.load_bt.setText(_translate("MainWindow", "load"))
        self.save_bt.setText(_translate("MainWindow", "save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())