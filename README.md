<h1 align="center"> Dungeon Dice </h1>

<p align="center">
  <br>
  <img src="https://raw.githubusercontent.com/Lioheart/Dungeon-Dice/master/resources/icons/dice.svg" alt="Dungeon Dice" width="400">
  <br>
</p>

Program zawierający w sobie spis wszystkich zaklęć z Podręcznika Gracza D&D ed. 3.5 w wersji polskiej.

## Spis treści
* [Informacje](#informacje)
* [Technologie](#technologie)
* [Instalacja](#instalacja)
* [Użycie](#użycie)
* [Status projektu](#status)
* [Licencja](#licencja)

## Informacje
[![Build Status](https://travis-ci.org/Lioheart/Dungeon-Dice.svg?branch=master)](https://travis-ci.org/Lioheart/Dungeon-Dice)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Lioheart/Dungeon-Dice.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Lioheart/Dungeon-Dice/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Lioheart/Dungeon-Dice.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Lioheart/Dungeon-Dice/context:python)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Lioheart/Dungeon-Dice)
[![Requirements Status](https://requires.io/github/Lioheart/Dungeon-Dice/requirements.svg?branch=master)](https://requires.io/github/Lioheart/Dungeon-Dice/requirements/?branch=master)

Program ten w przyszłości będzie zaiwerał spis zaklęć z Podręcznika Gracza oraz wszystkich dodatków, jakie wyszły w
 wersji polskiej. Dodatkowo, będzie można przyjrzeć się wszystkim magicznym przedmiotom, umiejętnościom, klasom
  postaci, klasom prestiżowym, będzie można wykonać rzuty kośćmi, rzuty na inicjatywę, symulować walkę, losować sprz
  ęt, a nawet tworzyć karty postaci! Poza tym, będzie także wspierał inne systemy RPG.
	
## Technologie
Projekt jest tworzony z wykorzystaniem technologii:
* PySide2
* beautifulsoup4
* SQLAlchemy
* alembic
	
## Setup
Aby uruchomić projekt, wykonaj poniższe polecenia:

```
$ git clone https://github.com/Lioheart/Dungeon-Dice.git
$ cd Dungeon-Dice
# pip install virtualenv
$ python -m venv venv
$ virtualenv venv
$ source venv/bin/activate              - Linux and Mac
# Set-ExecutionPolicy RemoteSigned      - Windows
$ venv\Scripts\activate                 - Windows
# Set-ExecutionPolicy Restricted        - Windows
$ pip install -r requirements.txt
```

## Użycie
Uruchom program za pomocą komendy: `python run.py` 

## Status
Projekt w fazie Alfa.

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Lioheart/Dungeon-Dice?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/Lioheart/Dungeon-Dice)
![GitHub Releases](https://img.shields.io/github/downloads/Lioheart/Dungeon-Dice/latest/total)
<a href="https://paypal.me/lioheart"> ![Donate](https://img.shields.io/badge/%24-Dodate-blue) </a>

![Screenshot](https://raw.githubusercontent.com/Lioheart/Dungeon-Dice/master/resources/screens/O%20mnie.PNG)

## Licencja
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<div>Icons from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>