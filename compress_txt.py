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


# TODO dodać testy
def gzip_write(txt='Zażółć gęślą jaźń\n', outfilename='example.txt.gz'):
    """
    Zapisuje tekst w pliku txt.gz
    :param txt: tekst źródłowy
    :param outfilename: nazwa pliku
    """
    with gzip.open(outfilename, 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(txt)

    print('Plik', outfilename, 'zawiera', os.stat(outfilename).st_size, 'bajtów\n')


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
    # original_data = '[32] Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?    [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.'
    # gzip_write(original_data)
    # print(gzip_read())
    # os.remove("example.txt.gz")
    apl = Application()
