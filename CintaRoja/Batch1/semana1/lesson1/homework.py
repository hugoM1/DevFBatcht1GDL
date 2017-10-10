from datetime import datetime, date, time, timedelta
import time
import webbrowser

ahora = datetime.now()
minutosnow = ahora.minute

def contador_por_minutos(minutosnow):
    contador = 0
    limite = 2
    url = "https://www.youtube.com/watch?v=0sFvFVkeGVg"
    while limite > contador:
        datetime.time.sleep(60)
        ahoradentro = datetime.now()
        minutoswhile = ahoradentro.minute
        totales = minutoswhile - minutosnow
        if totales != contador:
            contador + 1
        if(totales >= limite):
            webbrowser.open_new(url)
            respuesta = int(input("Deseas volver a iniciar el proceso?"))
            print respuesta
            if respuesta == 1:
                ahoraagain = datetime.now()
                minutosnowagain = ahoraagain.minute
                contador_por_minutos(minutosnowagain)
            else:
                break


contador_por_minutos(minutosnow)