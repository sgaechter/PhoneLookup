#! /usr/bin/env python3

######################################################
# PhoneLookup GUI                                    #
#                                                    #
# v 0.1                                              #
######################################################

import urllib.request
import webbrowser
from tkinter import *
import sys


def func(*args):
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zuerst eine Nummer ein.")
    else:
        url='https://tel.local.ch/'+entry_text
        webbrowser.open_new(url)
        eingabefeld.delete(0, END)
        
fenster = Tk()
fenster.title("Telefonnummern Lookup")
fenster.bind('<Return>',func)

# Anweisungs-Label
my_label = Label(fenster, text="Telefonnummer / Name: ")

welcome_label = Label(fenster)

# Hier kann der Benutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=5, width=40)
eingabefeld.focus_set()
exit_button = Button(fenster, text="Beenden", command=fenster.destroy)


# Nun fügen wir die Komponenten unserem Fenster hinzu
my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
exit_button.grid(row = 1, column = 1)
welcome_label.grid(row = 2, column = 0, columnspan = 2)


mainloop()

