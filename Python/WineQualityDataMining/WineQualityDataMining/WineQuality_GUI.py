##

## B8IT108 Data and Web Mining -  Machine Learning Workflow Program

## February 2020 

## Ciaran Finnegan - Student No. 10524150
## Dermot Madsen   - Student No. 10522567

## GUI Libraries

##

import PySimpleGUI as sg


def GetDatasetDescription():

    sg.theme('DarkAmber')	# Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Dataset Description')],
                [sg.Text('Enter a description tag for the dataset'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks 'Cancel' button
            break
        if event in ('Ok'):	    # if user clicks 'Ok' button
            sDataDescriptionText = values[0]
            print('You entered ', sDataDescriptionText)
            break

    window.close()

    return sDataDescriptionText

