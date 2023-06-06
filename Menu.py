from PySimpleGUI import PySimpleGUI as sg
from Conditions import condition


def Images():
    broken_clouds = 'images\Broken_Clouds.png'
    clear_sky = 'images\Clear_Sky.png'
    raining = 'images\Raining.png'
    snow = 'images\Snow.png'
    return broken_clouds, clear_sky, raining, snow


sao = ''

def SearchScreen():
    root1 = [
        [sg.Image('', key="logo")],
        [sg.Text("Localização"),sg.Input(key="Cidade", justification='c')],
        [sg.Button("Buscar")],
        [sg.Text("", key='erro')]
    ]

    return sg.Window('Project',layout=root1, finalize=True, element_justification="c")

def ShowResults():
    screen2 = [
        [sg.Button("Voltar"),sg.Image("", key="Logo")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Image(sao, key="Desc_icon")],
        [sg.Image("", key="Temp_icon"), sg.Text("", key="Temp_Text", font=('Arial Bold',40))],
        [sg.Text("", key="Desc_text", )],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Image("images\Humidade.png", key="Humidity_icon"), sg.Text("", key="humi_text", justification='t'), sg.Image("images\wind_speed_icon.png", key="Wind_Speed"), sg.Text("", key="Wind_Text")]
        
    ]
    return sg.Window("InfWeather",size=(450,500), layout= screen2, finalize= True, element_justification='c', text_justification='c')

window1, window2 = SearchScreen(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event == sg.WIN_CLOSED:
        break
    elif window == window2 and event == sg.WIN_CLOSED:
        break

    if window == window1 and event == 'Buscar':

        
        temp = condition(values["Cidade"])[0]
        desc = condition(values["Cidade"])[1]
        humi = condition(values["Cidade"])[2]
        wind = condition(values["Cidade"])[3]

        if condition(values["Cidade"])[0] == 'cidade não encontrada':
            window1['erro'].update('ERRO 404, Cidade não encontrada digite novamente')

        else:
            if desc == 'nublado' or desc == 'névoa':
                sao = "images\Broken_Clouds.png"

            elif desc == 'chuva leve':
                sao = 'images\Raining.png'

            elif desc == 'céu limpo':
                sao = "images\Clear_Sky.png"
            
            elif desc == 'algumas nuvens':
                sao = "images\Some_Clouds.png"


            window2 = ShowResults()
            window1.hide()

            
            window2["Temp_Text"].update(f'{temp}C°')
            window2["Desc_text"].update(f'{desc}')
            window2["humi_text"].update(f'{humi}%')
            window2["Wind_Text"].update(f'{wind}km/h')

    elif window == window2 and event == "Voltar":
        window2.hide()
        window1.un_hide()

        
