import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Comic_Sans 20",button_element_size = (3,3))
    button_size = (6,3)

    layout = [
        [sg.Text("",font= "Comic_Sans 40", justification="right" ,expand_x=True,pad =(10,20), right_click_menu = theme_menu, key = "Output")],
        [sg.Button("Löschen", expand_x = True ),sg.Button("berechne", expand_x = True, key = "=") ],
        [sg.Button(7, size = button_size ), sg.Button(8,size = button_size ), sg.Button(9,size = button_size ), sg.Button("/", size = button_size )],
        [sg.Button(4, size = button_size ),sg.Button(5, size = button_size ),sg.Button(6,size = button_size ),sg.Button("*", size = button_size )],
        [sg.Button(1, size = button_size ),sg.Button(2, size = button_size ),sg.Button(3, size = button_size ),sg.Button("-", size = button_size )],
        [sg.Button(0,expand_x = True ),sg.Button(",", size = button_size,),sg.Button("+", size = button_size )]
        ]

    return sg.Window("Taschenrechner", layout)

themes = sg.theme_list()
themes.sort()
theme_menu = ["menu", themes]
window = create_window("dark")
current_number = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["0","1","2","3","4","5","6","7","8","9",","]:
        current_number.append(event)
        number_string = "".join(current_number)
        window["Output"].update(number_string)

    if event in ["+","-","/","*"]:
        full_operation.append("".join(current_number))
        current_number = []
        full_operation.append(event)
        window["Output"].update("")

    if event == "=":
        full_operation.append("".join(current_number))
        result = eval("".join(full_operation).replace(",","."))
        window["Output"].update(result)
        current_number = [str(result)]
        full_operation = []

    if event == "Löschen":
        current_number = []
        full_operation = []
        window["Output"].update("")