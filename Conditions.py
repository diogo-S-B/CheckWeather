
def condition(cidade):

    import requests
    erro = ''
    try:
        API_KEY = ""
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        req = requests.get(link)
        req_desc = req.json()
        temp = int(req_desc["main"]["temp"]-273.15)
        desc = req_desc["weather"][0]["description"]
        humi = req_desc["main"]["humidity"]
        wind_speed = int(req_desc["wind"]["speed"])
        print(humi)
        
        return temp, desc, humi, wind_speed
    except KeyError:
        erro = 'cidade não encontrada'
        return erro
