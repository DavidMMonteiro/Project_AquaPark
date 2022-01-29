from gpio import *
from time import *
from realhttp import *


# Url API para acceder API
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php"
# Equipamente
pinTemp = A0
pinHum = A1
pinLed = A2
# 
http = RealHTTPClient()

# Função para leer a informação do sensor de temperatura e procesar a informação
def lerTemperatura(slot):
	temp = analogRead(slot)
	return round(temp * 200.0 / 1023.0 - 100,2) 

# Função para leer a informação do sensor de humidade e procesar a informação
def lerHumidade(slot):
	humid = analogRead(slot)
	return round(humid * 100.0 / 1024.0 + 0.5,2) 	

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
def save_temp():
	temperatura = lerTemperatura(pinTemp)
	data = getData()
	hora = getHora()
	print('Temperatura:'+str(temperatura)+' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'temperatura' , 'valor': temperatura , 'data': data,'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função para leer a informação da humidade e enviar a API
def save_hum():
	humidade =  lerHumidade(pinHum)
	data = getData()
	hora = getHora()
	print('Humidade:'+str(humidade)+' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': 'humidade' , 'valor': humidade , 'data':data, 'hora': hora}
	http.post(url, array_dados)
	http.onDone(onHTTPDone)

# Função principal
def main():
	# Guardar as portas e tipos movimentos do equipamento
	pinMode(pinTemp, IN)
	pinMode(pinHum, IN)
	pinMode(pinLed, OUT)
	while True:
		# LED para informar ao utilizador do arduino em funcionamento
		digitalWrite(pinLed, LOW)		
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
		# Chamada das correspondentes funções de dados
		save_temp()
		save_hum()
		#
		digitalWrite(pinLed, LOW)
		sleep(0.5)
		digitalWrite(pinLed, HIGH)
		sleep(0.5)
		
		
		
if __name__ == '__main__':
	main()