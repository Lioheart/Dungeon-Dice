"""Przekształca pliki .txt oraz .html na gzip"""
import gzip
import io
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Application:
    """
    Klasa TKinter
    """

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.title("Konwersja")
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")
        l1 = ttk.Label(text="Wybierz plik do konwersji", style="BW.TLabel")
        l1.pack(expand=1)
        b = ttk.Button(self.window, text="Otwórz", command=self.open_file)
        b.pack(expand=1)

        self.window.mainloop()

    def open_file(self):
        """
        Otwiera określony plik, po czym zapisuje go w txt.gz
        """
        filename = filedialog.askopenfilename(filetypes=[("Plik HTML", "*.html"), ("Plik tekstowy", "*.txt")])

        if filename:
            name = filename.split("/")[-1].replace(".html", ".txt.gz") if '.html' in filename.split("/")[-1] else \
                filename.split("/")[-1].replace(".txt", ".txt.gz")
            data = open(filename, 'r', encoding='utf-8').read()
            print(data)
            gzip_write(data, name)


def gzip_write(txt='Zażółć gęślą jaźń\n', outfilename='example.txt.gz'):
    """
    Zapisuje tekst w pliku txt.gz
    :param txt: tekst źródłowy
    :param outfilename: nazwa pliku
    """
    with gzip.open(outfilename, 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(txt)

    # print('Plik', outfilename, 'zawiera', os.stat(outfilename).st_size, 'bajtów\n')


def gzip_read(q=None, outfilename='example.txt.gz'):
    """
    Odczytuje wartość z pliku
    :param q: parametr zwrotny z wątku. Można używać wielowątkowości
    :return: tekst źródłowy
    :param outfilename: nazwa pliku
    """
    try:
        with gzip.open(outfilename, 'rb') as input_file:
            with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
                if q:
                    q.put(dec.read())
                return dec.read()
    except FileNotFoundError:
        if q:
            q.put('Nie znaleziono pliku!')
        return 'Nie znaleziono pliku!'


if __name__ == '__main__':
    apl = Application()
