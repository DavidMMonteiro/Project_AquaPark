from gpio import *
from time import *
from realhttp import *

# Import math library
import math


# Url API para acceder API
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php"
# Equipamente
pinWaterSensor = A0
pinWaterDetector = A1
pinLed = A2
# 
http = RealHTTPClient()

# Função para leer a informação do sensor de agua e procesar a informação
def getWaterSensor(slot):
	qunt = math.floor(calc_watersensor(analogRead(slot),0,255,0,20) + 0.5)
	return round(qunt) 

def calc_watersensor(x, inMin, inMax, outMin, outMax):
    return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

# Função para leer a informação do sensor de humidade e procesar a informação
def getWaterDetector(slot):
	return analogRead(slot) 	

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
	# Caso correr toudo bem ira mostrar a informação devolvida da API
	if status == 200:
		print("OK: POST realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		return status
	# Caso contrario, ira mostrar a informação de erro da API
	else:
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code:" + str(status))
		return status

# Função para leer a informação da temperatura e enviar a API
def save_water():
	qunt_water = getWaterSensor(pinWaterSensor)
	data = getData()
	hora = getHora()
	print('Temperatura:' + str(qunt_water) + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'nivel_agua' , 'valor': qunt_water , 'data': data, 'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função principal
def main():
	# Guardar as portas e tipos movimentos do equipamento
	pinMode(pinWaterSensor, IN)
	pinMode(pinWaterDetector, IN)
	pinMode(pinLed, OUT)
	while True:
		# LED para informar ao utilizador do arduino em funcionamento
		digitalWrite(pinLed, LOW)		
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
        #
		save_water()
        #
		digitalWrite(pinLed, LOW)
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
		sleep(0.5)
		
		
		
if __name__ == '__main__':
	main()