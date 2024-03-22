import PySimpleGUI as sg

layout = [
            [sg.Text('Convertisseur de température')],
            [sg.InputText(size=5, key='nombre'), sg.Combo(['°C', '°K', '°F'], key='type1'), sg.Text('à'), sg.Combo(['°C', '°K', '°F'], key='type2')],
            [sg.Button('Ok'), sg.Button('Annuler')] 
        ]


window = sg.Window('', layout, size=(500,500), default_element_size=600)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Annuler':
        break
    elif event == 'Ok':
        nombre = int(values['nombre'])
        type1 = values['type1'].split('°')[1]
        type2 = values['type2'].split('°')[1]
        if type1 == "C" and type2 == "F":
            tempfinal = (nombre * (9/5)) + 32
            window = sg.Window("°C à °F", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])
        elif type1 == "C" and type2 == "K":
            tempfinal = nombre + 273.15
            window = sg.Window("°C à °K", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])
        elif type1 == "F" and type2 == "C":
            tempfinal = (nombre - 32) * (5/9)
            window = sg.Window("°F à °C", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])
        elif type1 == "F" and type2 == "K":
            tempfinal = (nombre - 32) * (5/9) + 273.15
            window = sg.Window("°F à °K", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])
        elif type1 == "K" and type2 == "C":
            tempfinal = nombre - 273.15
            window = sg.Window("°K à °C", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])  
        if type1 == "K" and type2 == "F":
            tempfinal = (nombre - 273.15) * (9/5) + 32
            window = sg.Window("°K à °F", [[sg.Text((str(tempfinal) + "°" + str(type2)))]])              
        

window.close()