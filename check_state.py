"""Zawiera funkcje odpowiedzialne za wyświetlanie powiadomień o wpłacie oraz o aktualizacji"""
import json
import queue
import threading
import urllib.request
import webbrowser

from PySide2.QtCore import QTimer

import src
from notifications import NotificationWindow


def _open_browser(url='https://paypal.me/lioheart'):
    """
    Otwiera domyślnie link do paypala w przeglądarce
    """
    webbrowser.open(url, new=2)


def donate():
    """
    Wyświetla dwa powiadomienia o dokonaniu wpłaty. Pierwsze po 10s, drugie po 20 min.
    """
    title = 'Podoba ci się program?'
    text = 'Kliknij tutaj, żeby dokonać wpłaty.'
    QTimer.singleShot(10000, lambda: NotificationWindow.info(title, text, callback=_open_browser))
    QTimer.singleShot(1200000, lambda: NotificationWindow.info(title, text, callback=_open_browser))


def getResponse(q=None, url=None):
    """
    Zwraca plik JSON
    :param q: zmienna, do której przypisane zostanie wynik zwrotny
    :param url: ścieżka do API
    :return: JSON
    """
    operUrl = urllib.request.urlopen(url)
    if operUrl.getcode() == 200:
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
        jsonData = None
    if q:
        q.put(jsonData)
    return jsonData


def update():
    """
    Sprawdza wersję programu i komunikuje, jeśli jest nowsza wersja
    """
    que = queue.Queue()
    x = threading.Thread(target=getResponse,
                         args=(que, 'https://api.github.com/repos/Lioheart/Dungeon-Dice/releases/latest'))
    x.start()
    json_data = que.get()
    version = src.__version__
    if json_data['tag_name'][1:] > version:
        print('Nowa wersja')
        print(json_data['tag_name'][1:])
        title = 'Dostępna nowa wersja!'
        text = 'Kliknij tutaj aby pobrać.'
        url = 'https://github.com/Lioheart/Dungeon-Dice/releases/latest'
        NotificationWindow.success(title, text, callback=lambda: _open_browser(url))
    else:
        print('Aktualna wersja')
        print(json_data['tag_name'][1:])


if __name__ == '__main__':
    update()
