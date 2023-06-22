import os.path
import pickle

from PySide6.QtCore import (Slot)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import Qt
import time

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QWidget, QLineEdit, QListWidget, QDateEdit, QTextBrowser, QLabel, QListWidgetItem,
                               QMenuBar, QMenu)
from PySide6.QtUiTools import QUiLoader

from pathlib import Path

import sys
from Game import Game
from Team import Team
from players.AI import AI
from players.Human import Human
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__restart()

    def __restart(self):
        # game logic init
        self.last_field = None
        self.last_move_hints = []
        self.move_counter = 0
        self.move_logs = []

        self.players = {Team.WHITE: Human(Team.WHITE), Team.BLACK: AI(Team.BLACK)}
        self.game = Game(self.players[Team.WHITE], self.players[Team.BLACK])

        # init widgets
        self.window = QWidget()
        self.window.saves = QListWidget()

        # init buttons
        self.window.a1_button = QPushButton()
        self.window.a2_button = QPushButton()
        self.window.a3_button = QPushButton()
        self.window.a4_button = QPushButton()
        self.window.a5_button = QPushButton()
        self.window.a6_button = QPushButton()
        self.window.a7_button = QPushButton()
        self.window.a8_button = QPushButton()

        self.window.b1_button = QPushButton()
        self.window.b2_button = QPushButton()
        self.window.b3_button = QPushButton()
        self.window.b4_button = QPushButton()
        self.window.b5_button = QPushButton()
        self.window.b6_button = QPushButton()
        self.window.b7_button = QPushButton()
        self.window.b8_button = QPushButton()

        self.window.c1_button = QPushButton()
        self.window.c2_button = QPushButton()
        self.window.c3_button = QPushButton()
        self.window.c4_button = QPushButton()
        self.window.c5_button = QPushButton()
        self.window.c6_button = QPushButton()
        self.window.c7_button = QPushButton()
        self.window.c8_button = QPushButton()

        self.window.d1_button = QPushButton()
        self.window.d2_button = QPushButton()
        self.window.d3_button = QPushButton()
        self.window.d4_button = QPushButton()
        self.window.d5_button = QPushButton()
        self.window.d6_button = QPushButton()
        self.window.d7_button = QPushButton()
        self.window.d8_button = QPushButton()

        self.window.e1_button = QPushButton()
        self.window.e2_button = QPushButton()
        self.window.e3_button = QPushButton()
        self.window.e4_button = QPushButton()
        self.window.e5_button = QPushButton()
        self.window.e6_button = QPushButton()
        self.window.e7_button = QPushButton()
        self.window.e8_button = QPushButton()

        self.window.f1_button = QPushButton()
        self.window.f2_button = QPushButton()
        self.window.f3_button = QPushButton()
        self.window.f4_button = QPushButton()
        self.window.f5_button = QPushButton()
        self.window.f6_button = QPushButton()
        self.window.f7_button = QPushButton()
        self.window.f8_button = QPushButton()

        self.window.g1_button = QPushButton()
        self.window.g2_button = QPushButton()
        self.window.g3_button = QPushButton()
        self.window.g4_button = QPushButton()
        self.window.g5_button = QPushButton()
        self.window.g6_button = QPushButton()
        self.window.g7_button = QPushButton()
        self.window.g8_button = QPushButton()

        self.window.h1_button = QPushButton()
        self.window.h2_button = QPushButton()
        self.window.h3_button = QPushButton()
        self.window.h4_button = QPushButton()
        self.window.h5_button = QPushButton()
        self.window.h6_button = QPushButton()
        self.window.h7_button = QPushButton()
        self.window.h8_button = QPushButton()

        # init labels
        self.window.a1 = QLabel()
        self.window.a2 = QLabel()
        self.window.a3 = QLabel()
        self.window.a4 = QLabel()
        self.window.a5 = QLabel()
        self.window.a6 = QLabel()
        self.window.a7 = QLabel()
        self.window.a8 = QLabel()

        self.window.b1 = QLabel()
        self.window.b2 = QLabel()
        self.window.b3 = QLabel()
        self.window.b4 = QLabel()
        self.window.b5 = QLabel()
        self.window.b6 = QLabel()
        self.window.b7 = QLabel()
        self.window.b8 = QLabel()

        self.window.c1 = QLabel()
        self.window.c2 = QLabel()
        self.window.c3 = QLabel()
        self.window.c4 = QLabel()
        self.window.c5 = QLabel()
        self.window.c6 = QLabel()
        self.window.c7 = QLabel()
        self.window.c8 = QLabel()

        self.window.d1 = QLabel()
        self.window.d2 = QLabel()
        self.window.d3 = QLabel()
        self.window.d4 = QLabel()
        self.window.d5 = QLabel()
        self.window.d6 = QLabel()
        self.window.d7 = QLabel()
        self.window.d8 = QLabel()

        self.window.e1 = QLabel()
        self.window.e2 = QLabel()
        self.window.e3 = QLabel()
        self.window.e4 = QLabel()
        self.window.e5 = QLabel()
        self.window.e6 = QLabel()
        self.window.e7 = QLabel()
        self.window.e8 = QLabel()

        self.window.f1 = QLabel()
        self.window.f2 = QLabel()
        self.window.f3 = QLabel()
        self.window.f4 = QLabel()
        self.window.f5 = QLabel()
        self.window.f6 = QLabel()
        self.window.f7 = QLabel()
        self.window.f8 = QLabel()

        self.window.g1 = QLabel()
        self.window.g2 = QLabel()
        self.window.g3 = QLabel()
        self.window.g4 = QLabel()
        self.window.g5 = QLabel()
        self.window.g6 = QLabel()
        self.window.g7 = QLabel()
        self.window.g8 = QLabel()

        self.window.h1 = QLabel()
        self.window.h2 = QLabel()
        self.window.h3 = QLabel()
        self.window.h4 = QLabel()
        self.window.h5 = QLabel()
        self.window.h6 = QLabel()
        self.window.h7 = QLabel()
        self.window.h8 = QLabel()

        self.window.white_points = QLabel()
        self.window.black_points = QLabel()
        self.window.white_pieces = QListWidget()
        self.window.white_pieces = QListWidget()

        self.window.menubar = QMenuBar()
        save_action = QAction('New save', self)
        save_action.triggered.connect(self.save)

        new_game_action = QAction('New game', self)
        new_game_action.triggered.connect(self.__new_game)

        choose_opponent = QAction('Opponent type', self)
        submenu = QMenu(self)
        sub_action_human = QAction('Human', self)
        sub_action_human.triggered.connect(self.__set_human)

        sub_action_ai = QAction('AI', self)
        sub_action_ai.triggered.connect(self.__set_ai)

        submenu.addAction(sub_action_human)
        submenu.addAction(sub_action_ai)
        choose_opponent.setMenu(submenu)

        self.window.load_save_button = QPushButton()
        self.window.delete_save_button = QPushButton()

        # load ui
        loader = QUiLoader()
        self.window = loader.load("mainWindow.ui", self)
        self.window.setFixedSize(870, 941)
        self.window.setWindowTitle("Chess")

        self.window.menubar.addAction(save_action)
        self.window.menubar.addAction(new_game_action)
        self.window.menubar.addAction(choose_opponent)

        # init squares dict
        self.squares = dict()
        self.squares['a1'] = self.window.a1
        self.squares['a2'] = self.window.a2
        self.squares['a3'] = self.window.a3
        self.squares['a4'] = self.window.a4
        self.squares['a5'] = self.window.a5
        self.squares['a6'] = self.window.a6
        self.squares['a7'] = self.window.a7
        self.squares['a8'] = self.window.a8

        self.squares['b1'] = self.window.b1
        self.squares['b2'] = self.window.b2
        self.squares['b3'] = self.window.b3
        self.squares['b4'] = self.window.b4
        self.squares['b5'] = self.window.b5
        self.squares['b6'] = self.window.b6
        self.squares['b7'] = self.window.b7
        self.squares['b8'] = self.window.b8

        self.squares['c1'] = self.window.c1
        self.squares['c2'] = self.window.c2
        self.squares['c3'] = self.window.c3
        self.squares['c4'] = self.window.c4
        self.squares['c5'] = self.window.c5
        self.squares['c6'] = self.window.c6
        self.squares['c7'] = self.window.c7
        self.squares['c8'] = self.window.c8

        self.squares['d1'] = self.window.d1
        self.squares['d2'] = self.window.d2
        self.squares['d3'] = self.window.d3
        self.squares['d4'] = self.window.d4
        self.squares['d5'] = self.window.d5
        self.squares['d6'] = self.window.d6
        self.squares['d7'] = self.window.d7
        self.squares['d8'] = self.window.d8

        self.squares['e1'] = self.window.e1
        self.squares['e2'] = self.window.e2
        self.squares['e3'] = self.window.e3
        self.squares['e4'] = self.window.e4
        self.squares['e5'] = self.window.e5
        self.squares['e6'] = self.window.e6
        self.squares['e7'] = self.window.e7
        self.squares['e8'] = self.window.e8

        self.squares['f1'] = self.window.f1
        self.squares['f2'] = self.window.f2
        self.squares['f3'] = self.window.f3
        self.squares['f4'] = self.window.f4
        self.squares['f5'] = self.window.f5
        self.squares['f6'] = self.window.f6
        self.squares['f7'] = self.window.f7
        self.squares['f8'] = self.window.f8

        self.squares['g1'] = self.window.g1
        self.squares['g2'] = self.window.g2
        self.squares['g3'] = self.window.g3
        self.squares['g4'] = self.window.g4
        self.squares['g5'] = self.window.g5
        self.squares['g6'] = self.window.g6
        self.squares['g7'] = self.window.g7
        self.squares['g8'] = self.window.g8

        self.squares['h1'] = self.window.h1
        self.squares['h2'] = self.window.h2
        self.squares['h3'] = self.window.h3
        self.squares['h4'] = self.window.h4
        self.squares['h5'] = self.window.h5
        self.squares['h6'] = self.window.h6
        self.squares['h7'] = self.window.h7
        self.squares['h8'] = self.window.h8

        # init buttons dict
        self.buttons = dict()
        self.buttons['a1_button'] = self.window.a1_button
        self.squares['a2_button'] = self.window.a2_button
        self.squares['a3_button'] = self.window.a3_button
        self.squares['a4_button'] = self.window.a4_button
        self.squares['a5_button'] = self.window.a5_button
        self.squares['a6_button'] = self.window.a6_button
        self.squares['a7_button'] = self.window.a7_button
        self.squares['a8_button'] = self.window.a8_button

        self.buttons['b1_button'] = self.window.b1_button
        self.squares['b2_button'] = self.window.b2_button
        self.squares['b3_button'] = self.window.b3_button
        self.squares['b4_button'] = self.window.b4_button
        self.squares['b5_button'] = self.window.b5_button
        self.squares['b6_button'] = self.window.b6_button
        self.squares['b7_button'] = self.window.b7_button
        self.squares['b8_button'] = self.window.b8_button

        self.buttons['c1_button'] = self.window.c1_button
        self.squares['c2_button'] = self.window.c2_button
        self.squares['c3_button'] = self.window.c3_button
        self.squares['c4_button'] = self.window.c4_button
        self.squares['c5_button'] = self.window.c5_button
        self.squares['c6_button'] = self.window.c6_button
        self.squares['c7_button'] = self.window.c7_button
        self.squares['c8_button'] = self.window.c8_button

        self.buttons['d1_button'] = self.window.d1_button
        self.squares['d2_button'] = self.window.d2_button
        self.squares['d3_button'] = self.window.d3_button
        self.squares['d4_button'] = self.window.d4_button
        self.squares['d5_button'] = self.window.d5_button
        self.squares['d6_button'] = self.window.d6_button
        self.squares['d7_button'] = self.window.d7_button
        self.squares['d8_button'] = self.window.d8_button

        self.buttons['e1_button'] = self.window.e1_button
        self.squares['e2_button'] = self.window.e2_button
        self.squares['e3_button'] = self.window.e3_button
        self.squares['e4_button'] = self.window.e4_button
        self.squares['e5_button'] = self.window.e5_button
        self.squares['e6_button'] = self.window.e6_button
        self.squares['e7_button'] = self.window.e7_button
        self.squares['e8_button'] = self.window.e8_button

        self.buttons['f1_button'] = self.window.f1_button
        self.squares['f2_button'] = self.window.f2_button
        self.squares['f3_button'] = self.window.f3_button
        self.squares['f4_button'] = self.window.f4_button
        self.squares['f5_button'] = self.window.f5_button
        self.squares['f6_button'] = self.window.f6_button
        self.squares['f7_button'] = self.window.f7_button
        self.squares['f8_button'] = self.window.f8_button

        self.buttons['g1_button'] = self.window.g1_button
        self.squares['g2_button'] = self.window.g2_button
        self.squares['g3_button'] = self.window.g3_button
        self.squares['g4_button'] = self.window.g4_button
        self.squares['g5_button'] = self.window.g5_button
        self.squares['g6_button'] = self.window.g6_button
        self.squares['g7_button'] = self.window.g7_button
        self.squares['g8_button'] = self.window.g8_button

        self.buttons['h1_button'] = self.window.h1_button
        self.squares['h2_button'] = self.window.h2_button
        self.squares['h3_button'] = self.window.h3_button
        self.squares['h4_button'] = self.window.h4_button
        self.squares['h5_button'] = self.window.h5_button
        self.squares['h6_button'] = self.window.h6_button
        self.squares['h7_button'] = self.window.h7_button
        self.squares['h8_button'] = self.window.h8_button

        # signals
        self.window.load_save_button.clicked.connect(self.load_save_mode)
        self.window.delete_save_button.clicked.connect(self.delete_save_mode)
        self.window.a1_button.clicked.connect(self.board_square_action)
        self.window.a2_button.clicked.connect(self.board_square_action)
        self.window.a3_button.clicked.connect(self.board_square_action)
        self.window.a4_button.clicked.connect(self.board_square_action)
        self.window.a5_button.clicked.connect(self.board_square_action)
        self.window.a6_button.clicked.connect(self.board_square_action)
        self.window.a7_button.clicked.connect(self.board_square_action)
        self.window.a8_button.clicked.connect(self.board_square_action)

        self.window.b1_button.clicked.connect(self.board_square_action)
        self.window.b2_button.clicked.connect(self.board_square_action)
        self.window.b3_button.clicked.connect(self.board_square_action)
        self.window.b4_button.clicked.connect(self.board_square_action)
        self.window.b5_button.clicked.connect(self.board_square_action)
        self.window.b6_button.clicked.connect(self.board_square_action)
        self.window.b7_button.clicked.connect(self.board_square_action)
        self.window.b8_button.clicked.connect(self.board_square_action)

        self.window.c1_button.clicked.connect(self.board_square_action)
        self.window.c2_button.clicked.connect(self.board_square_action)
        self.window.c3_button.clicked.connect(self.board_square_action)
        self.window.c4_button.clicked.connect(self.board_square_action)
        self.window.c5_button.clicked.connect(self.board_square_action)
        self.window.c6_button.clicked.connect(self.board_square_action)
        self.window.c7_button.clicked.connect(self.board_square_action)
        self.window.c8_button.clicked.connect(self.board_square_action)

        self.window.d1_button.clicked.connect(self.board_square_action)
        self.window.d2_button.clicked.connect(self.board_square_action)
        self.window.d3_button.clicked.connect(self.board_square_action)
        self.window.d4_button.clicked.connect(self.board_square_action)
        self.window.d5_button.clicked.connect(self.board_square_action)
        self.window.d6_button.clicked.connect(self.board_square_action)
        self.window.d7_button.clicked.connect(self.board_square_action)
        self.window.d8_button.clicked.connect(self.board_square_action)

        self.window.e1_button.clicked.connect(self.board_square_action)
        self.window.e2_button.clicked.connect(self.board_square_action)
        self.window.e3_button.clicked.connect(self.board_square_action)
        self.window.e4_button.clicked.connect(self.board_square_action)
        self.window.e5_button.clicked.connect(self.board_square_action)
        self.window.e6_button.clicked.connect(self.board_square_action)
        self.window.e7_button.clicked.connect(self.board_square_action)
        self.window.e8_button.clicked.connect(self.board_square_action)

        self.window.f1_button.clicked.connect(self.board_square_action)
        self.window.f2_button.clicked.connect(self.board_square_action)
        self.window.f3_button.clicked.connect(self.board_square_action)
        self.window.f4_button.clicked.connect(self.board_square_action)
        self.window.f5_button.clicked.connect(self.board_square_action)
        self.window.f6_button.clicked.connect(self.board_square_action)
        self.window.f7_button.clicked.connect(self.board_square_action)
        self.window.f8_button.clicked.connect(self.board_square_action)

        self.window.g1_button.clicked.connect(self.board_square_action)
        self.window.g2_button.clicked.connect(self.board_square_action)
        self.window.g3_button.clicked.connect(self.board_square_action)
        self.window.g4_button.clicked.connect(self.board_square_action)
        self.window.g5_button.clicked.connect(self.board_square_action)
        self.window.g6_button.clicked.connect(self.board_square_action)
        self.window.g7_button.clicked.connect(self.board_square_action)
        self.window.g8_button.clicked.connect(self.board_square_action)

        self.window.h1_button.clicked.connect(self.board_square_action)
        self.window.h2_button.clicked.connect(self.board_square_action)
        self.window.h3_button.clicked.connect(self.board_square_action)
        self.window.h4_button.clicked.connect(self.board_square_action)
        self.window.h5_button.clicked.connect(self.board_square_action)
        self.window.h6_button.clicked.connect(self.board_square_action)
        self.window.h7_button.clicked.connect(self.board_square_action)
        self.window.h8_button.clicked.connect(self.board_square_action)

        self.window.saves.itemClicked.connect(self.load)

        self.__init_saves()

        # show
        self.window.show()

    def load_save_mode(self):
        self.window.saves.itemClicked.disconnect()
        self.window.saves.itemClicked.connect(self.load)

    def delete_save_mode(self):
        self.window.saves.itemClicked.disconnect()
        self.window.saves.itemClicked.connect(self.delete_save)

    @Slot()
    def delete_save(self, item):
        path = 'saves/' + item.text() + '.pkl'
        if not os.path.exists(path):
            raise RuntimeError(f'Save {path} does not exist!')

        os.remove(path)
        self.__init_saves()

    def __set_ai(self):
        if type(self.players[Team.BLACK]) is AI:
            return

        self.players[Team.BLACK] = AI(Team.BLACK)
        for log in self.move_logs:
            self.players[Team.BLACK].update(log[1:3], log[-2:])

    def __set_human(self):
        self.players[Team.BLACK] = Human(Team.BLACK)

    def __new_game(self):
        self.window.close()
        self.__restart()

    def save(self):
        time: datetime = datetime.now()
        file_name = f"save - {str(time.day)}.{str(time.month)}.{str(time.year)} - {str(time.time().hour)}.{str(time.time().minute)}.{str(time.time().second)}"

        with open('saves/' + file_name + '.pkl', 'wb') as file:
            pickle.dump(self.move_logs, file)

        self.window.saves.addItem(file_name)

    @Slot()
    def load(self, item):
        with open('saves/' + item.text() + '.pkl', 'rb') as file:
            move_logs = pickle.load(file)

        self.window.close()
        self.__restart()
        self.move_logs = move_logs
        self.__perform_moves_from_log()
        self.__show_player_status()
        self.__recolor_turn()

    def __perform_moves_from_log(self):
        game_with_ai = False
        ai = None
        for player in self.players.values():
            if type(player) is AI:
                game_with_ai = True
                ai = player

        for log in self.move_logs:
            source_name = log[1] + log[2]
            destination_name = log[-2:]

            if game_with_ai:
                player.update(source_name, destination_name)

            source_field = self.game.get_field(source_name)
            dest_field = self.game.get_field(destination_name)

            source_square = self.__get_square(source_field)
            destination_square = self.__get_square(dest_field)

            self.game.make_move(self.players[self.move_counter % 2], source_field, dest_field)
            self.move_counter += 1

            destination_square.setPixmap(source_square.pixmap())
            self.__recolor(dest_field)

            source_square.clear()

    @Slot()
    def board_square_action(self):
        game = self.game
        sender = self.sender()
        sender_square_name = sender.objectName()[:2]
        sender_field = game.get_field(sender_square_name)
        current_player = self.players[self.move_counter % 2]

        destinations = game.get_possible_destinations(current_player, sender_field)

        if not self.last_move_hints:

            if destinations is not []:
                self.set_move_hints(destinations, sender_field)

        else:  # perform move
            if sender_field in self.last_move_hints:
                self.move_logs.append(game.make_move(current_player, self.last_field, sender_field))
                if type(ai := self.players[(self.move_counter + 1) % 2]) is AI:
                    ai.update(self.last_field.get_position().get_name(), sender_field.get_position().get_name())

                source_square = self.__get_square(self.last_field)
                destination_square = self.__get_square(sender_field)
                destination_square.setPixmap(source_square.pixmap())
                self.__recolor(sender_field)

                source_square.clear()
                self.move_counter += 1
                self.__recolor_turn()

                self.clear_move_hints(current_player, sender_field)
                self.check(sender_field, current_player)

            else:
                self.clear_move_hints(current_player)
                self.set_move_hints(destinations, sender_field)

        self.__show_player_status()
        self.window.repaint()

        if type(ai := self.players[self.move_counter % 2]) is AI:
            source, dest = ai.get_move()

            source_field = self.game.get_field(source)
            dest_field = self.game.get_field(dest)

            self.move_logs.append(game.make_move(ai, source_field, dest_field))

            source_square = self.__get_square(source_field)
            destination_square = self.__get_square(dest_field)
            destination_square.setPixmap(source_square.pixmap())
            self.__recolor(dest_field)

            source_square.clear()
            self.move_counter += 1
            self.__recolor_turn()

            self.__show_player_status()
            self.window.repaint()
            self.check(dest_field, ai)

    def check(self, sender_field, current_player):
        # is a check
        if (king_field := self.game.check(sender_field, current_player.get_team())) and king_field is not None:
            king_square = self.__get_square(king_field)
            if self.game.mate(king_field):
                king_square.setStyleSheet("background-color: #FF0000;")
                self.window.repaint()
            else:
                # check red blink square
                king_square.setStyleSheet("background-color: #FF0000;")
                self.window.repaint()
                time.sleep(0.6)
                self.__recolor(king_field)

    def __recolor_turn(self):
        self.window.turn_color.setStyleSheet("background-color: #FFFFFF" if self.move_counter % 2 == 0 else
                                             "background-color: #000000")

    def __show_player_status(self):
        white_p = self.players[Team.WHITE]
        white_points = str(white_p.get_points())
        white_pieces = white_p.get_taken_pieces()

        black_p = self.players[Team.BLACK]
        black_points = str(black_p.get_points())
        black_pieces = black_p.get_taken_pieces()

        self.window.white_points.setText(white_points)
        self.window.black_points.setText(black_points)

        white_pieces_ui: QListWidget = self.window.white_pieces
        black_pieces_ui: QListWidget = self.window.black_pieces

        if white_pieces_ui.count() != len(white_pieces):
            for i in range(white_pieces_ui.count(), len(white_pieces)):
                piece = white_pieces[i]

                ui_piece = QListWidgetItem()
                icon = QIcon(QPixmap(piece.get_icon_path()))
                ui_piece.setIcon(icon)

                white_pieces_ui.addItem(ui_piece)

        if black_pieces_ui.count() != len(black_pieces):
            for i in range(black_pieces_ui.count(), len(black_pieces)):
                piece = black_pieces[i]

                ui_piece = QListWidgetItem()
                icon = QIcon(QPixmap(piece.get_icon_path()))
                ui_piece.setIcon(icon)

                black_pieces_ui.addItem(ui_piece)

    def __init_saves(self):
        self.window.saves.clear()
        for save in Path('saves').iterdir():
            # ignore .pkl
            self.window.saves.addItem(save.name[:-4])
        
    def __get_button(self, field) -> QPushButton:
        return self.buttons[field.get_position().get_name()]

    def __get_square(self, field):
        return self.squares[field.get_position().get_name()]

    def clear_move_hints(self, player, move_dest_to_ignore=None):
        for destination in self.last_move_hints:
            square = self.__get_square(destination)
            if destination != move_dest_to_ignore and destination.get_piece() is None:
                square.clear()
            elif destination.get_piece() is not None and player.get_team() != destination.get_piece().get_team():
                self.__recolor(destination)

        self.last_move_hints = []
        self.last_field = None

    def set_move_hints(self, destinations, source_field):
        for destination in destinations:
            if destination.get_piece() is None:
                self.__get_square(destination).setPixmap(
                    QPixmap(r"C:\Users\Asus\PycharmProjects\Szachy\images\sphere75.png"))

            elif source_field.get_piece().get_team() != destination.get_piece().get_team():
                self.__get_square(destination).setStyleSheet("background-color: #FF0000;")

            self.last_move_hints = destinations
            self.last_field = source_field

    def __recolor(self, field):
        if (field.get_position().get_x() + field.get_position().get_y()) % 2 == 1:
            self.__get_square(field).setStyleSheet("background-color: rgb(239, 239, 239);")
        else:
            self.__get_square(field).setStyleSheet("background-color: rgb(170, 0, 255);")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())