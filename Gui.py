import tkinter
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar, simpledialog,filedialog
import pandas as pd
import PySimpleGUI as sg
pd.set_option('display.max_rows', None)
from NaiveBaise import classify
from Build import build

###Building Window
def Gui():
    sg.theme("DarkTeal2")
    layout = [[sg.T("")],
                      [sg.Text("Directory Path: "), sg.Input(key="-IN-", change_submits=True), sg.FolderBrowse(key="-IN-")],
                       [sg.Text("Discretization Bins: "), sg.Input(key="-IN2-", change_submits=True)] ,
                      [sg.Button("Classify"), sg.Button("Build"), sg.Button("Exit")]]

    ###Building Window
    window= sg.Window('Naive Baise Classifier', layout, size=(600, 150))

    while True:
        event, values = window.read()


        #exit the platform
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        #classify should come after bulid!
        elif event == "Classify":

            classify(train,test, path)

        if event == "Build":
            try:
                data = []
                with open(values["-IN-"] + "/Structure.txt", "r") as file:
                    for line in file:
                        row = line.split()
                        row = [str(x) for x in row]
                        data.append(row)
                path = values["-IN-"]
                attributes={}
                structure_features = list(map(lambda x: x[1], data))
                att=list(map(lambda x: x[2], data))
                i=0
                for x in structure_features:
                    attributes[x]= att[i]
                    i+=1


                test= pd.read_csv(values["-IN-"] + "/test.csv")
                #print(test)
                test= test.fillna(test.mode().iloc[0]) #clean data from NA's-> replace with most common in  each culomn
                train = pd.read_csv(values["-IN-"] + "/train.csv")
                #print(train)
                bins = values["-IN2-"]

                if bins is None or int(bins) <= 0 or not bins.isdigit():
                    print("Bins number isn't valid")
                    return False


                if build(train, test, structure_features,bins, attributes):
                    continue
                else:
                    break

            except IOError:
                print("File not found or path is incorrect")

Gui()







