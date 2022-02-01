from gpio import *
from time import *
from realhttp import *

# Import math library
import math


# Url API para acceder API
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php"
# Equipamente
pinSmokeSensor = A0
pinWindSendor = A1
pinLed = A2
# 
http = RealHTTPClient()

# Função para leer a informação do sensor de fumo e procesar a informação
def getSmokeSensor(slot):
	smoke = analogRead(slot)
	smoke = (smoke * 100)/255
	return round(smoke) 	

# Função para leer a informação do sensor de vento e procesar a informação
def getWindSensor(slot):
	if analogRead(slot) >= 1:
		wind = 1
	else:
		wind = 0
	return wind

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

# Função para leer a informação da fumo e enviar a API
def save_smoke():
	qunt_smoke = getSmokeSensor(pinSmokeSensor)
	data = getData()
	hora = getHora()
	print('Fumo:' + str(qunt_smoke) + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'fumo' , 'valor': qunt_smoke , 'data': data, 'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função para leer a informação da vento e enviar a API
def save_wind():
	qunt_wind = getWindSensor(pinWindSendor)
	data = getData()
	hora = getHora()
	print('Vento:' + str(qunt_wind) + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'vento' , 'valor': qunt_wind , 'data': data, 'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função principal
def main():
	# Guardar as portas e tipos movimentos do equipamento
	pinMode(pinSmokeSensor, IN)
	pinMode(pinWindSendor, IN)
	pinMode(pinLed, OUT)
	while True:
		# LED para informar ao utilizador do arduino em funcionamento
		digitalWrite(pinLed, LOW)		
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
        #
		save_smoke()
		save_wind()
        #
		digitalWrite(pinLed, LOW)
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
		sleep(0.5)
		
		
		
if __name__ == '__main__':
	main()