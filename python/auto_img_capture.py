
import sys
from time import *
import cv2 as cv
#
from requests import (post, get)

camera = cv.VideoCapture(0)
delay = 5000
#
url = "http://127.0.0.1/prsi/Project_AquaPark/api/upload.php"
urlAPI = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php"
#


def send_file(file):
    print("A enviar ficheiro para API...")
    r = post(url, files = file)
    print(r.status_code, " --- ", r.text)

def send_info(array):
    print("Enviar informação imagem...")
    r = post(urlAPI, array)
    print(r.status_code, " --- ", r.text)

# Função para leer da data no sistema
def getData():
	return strftime('%d-%m-%Y',gmtime())

# Função para leer a hora no sistema
def getHora():
	return strftime('%H:%M:%S',gmtime())

try:
    print("Prima CTRL+C para terminar")
    while True:
        print("---------------")
        print("Capturar imagem")
        ret, image = camera.read()
        print("A grabar imagem em disco")
        cv.imwrite('webcam.jpg', image)
        file = {'imagem': open('webcam.jpg', 'rb')}
        send_file(file)
        array_dados = {'nome': 'img' , 'valor': '1' , 'data': getData(), 'hora': getHora()}
        send_info(array_dados)
        print("Próximo captura da imagem dentro de " + str(delay/1000) + "segundos...")
        cv.waitKey(delay)

except KeyboardInterrupt:
    print("Programa terminado pelo utilizador")

except:
    print("Ocorreu um erro", sys.exc_info())

finally:
    array_dados = {'nome': 'img' , 'valor': '0' , 'data': getData(), 'hora': getHora()}
    send_info(array_dados)
    print("Fim do programa")
    camera.release()
    cv.destroyAllWindows()