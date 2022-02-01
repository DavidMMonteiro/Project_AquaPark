from gpio import *
from time import *
from realhttp import *

# Import math library
import math


# Url API para acceder API
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php"
# Equipamente
pinLightSensor = A0
pinLed = A1
# 
http = RealHTTPClient()

# Função para leer a informação do sensor de agua e procesar a informação
def getLightSensor(slot):
	return round(analogRead(slot)) 

# Função para leer da data no sistema
def getData():
	return strftime('%d-%m-%Y',gmtime())

# Função para leer a hora no sistema
def getHora():
	return strftime('%H:%M:%S',gmtime())

# Função chamada quando acabar a chamada a API
def onHTTPDone(status, data, replyHeader):
	# Informação da chamada
	print(replyHeader)
	if status == 200: # Caso correr toudo bem ira mostrar a informação devolvida da API
		print("OK: POST realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		return status
	else: # Caso contrario, ira mostrar a informação de erro da API
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code:" + str(status))
		return status

# Função para leer a informação da temperatura e enviar a API
def save_light():
	qunt_light = getLightSensor(pinLightSensor)
	data = getData()
	hora = getHora()
	print('Luz:' + str(qunt_light) + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'luz' , 'valor': qunt_light , 'data': data, 'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função principal
def main():
	# Guardar as portas e tipos movimentos do equipamento
	pinMode(pinLightSensor, IN)
	pinMode(pinLed, OUT)
	while True:
		# LED para informar ao utilizador do arduino em funcionamento
		digitalWrite(pinLed, LOW)		
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
        #
		save_light()
        #
		digitalWrite(pinLed, LOW)
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
		sleep(0.5)
		
		
		
if __name__ == '__main__':
	main()