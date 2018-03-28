# -*- coding: utf-8 -*-

import os
from scipy.io.wavfile import read
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from phrases import randomPhrase
from recorder import Recorder
from speech_features import features
from users import fileToDict


def standartize(X):
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    return (X - m) / s, m, s


# форма голосовой идентификации
class IdentifyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.buttonsBox = QHBoxLayout()
        self.readyBox = QHBoxLayout()
        self.setLayout(self.vBox)
        self.setWindowTitle('Идентифицировать себя')

        # создание компонентов
        self.textToSpeech = QLabel('Текст для произнесения')
        self.startButton = QPushButton('Старт')
        self.stopButton = QPushButton('Стоп')
        self.userName = QLabel('Вы - <неизвестный пользователь>')
        self.readyButton = QPushButton('Готово')

        # добавление компонентов на форму
        self.vBox.addWidget(QLabel('Произнесите фразу'))
        self.vBox.addWidget(self.textToSpeech)

        self.buttonsBox.addStretch(1)
        self.buttonsBox.addWidget(self.startButton)
        self.buttonsBox.addWidget(self.stopButton)
        self.buttonsBox.addStretch(1)
        self.vBox.addLayout(self.buttonsBox)

        self.vBox.addWidget(self.userName)

        self.readyBox.addStretch(1)
        self.readyBox.addWidget(self.readyButton)
        self.vBox.addLayout(self.readyBox)

        # connect
        self.startButton.clicked.connect(lambda: self.startButtonClicked())
        self.stopButton.clicked.connect(lambda: self.stopButtonClicked())

    def startButtonClicked(self):
        self.stopButton.setEnabled(True)
        self.startButton.setEnabled(False)

        self.recorder = Recorder()
        self.recorder.start()

    def stopButtonClicked(self):
        self.stopButton.setEnabled(False)
        self.startButton.setEnabled(True)

        # запись речевого фрагмента в файл
        testDirectory = 'test_files'
        if not os.path.exists(testDirectory):
            os.makedirs(testDirectory)
        path = testDirectory + '/test.wav'
        self.recorder.stop(path)

        # вычисление признаков по файлу и запись в их в файл data.txt
        feats = self.processFile(path)

        # классификация
        data = np.loadtxt('data.txt', delimiter=';')
        X = data[:, :-1]
        y = np.array(data[:, -1], dtype=int)

        # стандартизация обучающей выборки и классифицируемого объекта
        X_train, m, s = standartize(X)
        feats = (feats - m) / s

        clf = KNeighborsClassifier(n_neighbors=3, p=1)
        clf.fit(X_train, y.ravel())
        id = int(clf.predict(feats))

        # вывод на экран имени распознанного пользователя
        users = fileToDict()
        self.userName.setText('Вы - %s' % users[id])


    def processFile(self, path):
        sampleRate, samples = read(path)
        return features(samples, sampleRate)

    def showEvent(self, event):
        self.textToSpeech.setText(randomPhrase())
