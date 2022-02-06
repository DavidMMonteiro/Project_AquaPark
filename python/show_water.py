from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer temperatura
urlGet = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=nivel_agua&type=valor"
# Url API para guardar atuadores temperatura
urlPost = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?"
# Equipamente
pinDrain = A3
pinSprinler = A2
pinAlarm = A1
pinLCD = A0
#
httpGet = RealHTTPClient()
httpPost = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onGetHTTPDone(status, data):
	sprinkler_state = LOW
	drain_state = 0
	alarm_state = LOW
	LCD_state = "Nao conseguio leer"
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		# Valor em cm
		minValue = 10 
		maxValue = 40
		# Filtra os dados da API
		qunt = float(data.replace(" ",""))
		if  qunt < minValue: # Caso valor for inferior ao minimo, ativa o aspersor, fechar o esgoto e desativa a alarma
			sprinkler_state = HIGH
			drain_state = 0
			alarm_state = LOW
			LCD_state = "H2O Level:" + data + "cm \nSprinler: ON"
		# Caso a valor for comprendi entre o minimo e o maximo, 
		# ativa a alarma para avisar aos utilizadores	
		elif qunt >= minValue and qunt < maxValue: 
			sprinkler_state = HIGH
			drain_state = 0
			alarm_state = HIGH
			LCD_state = "H2O Level:" + data + "cm \nWARNING!"
		# Caso a valor for maior o maximo, 
		# ativa a alarma e desativa o aspersor e abrir o esgoto
		elif qunt >= maxValue:
			sprinkler_state = LOW
			drain_state = 1
			alarm_state = HIGH
			LCD_state = "H2O Level:" + data + "cm \nDrain: OPEN"

    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))

	digitalWrite(pinSprinler, sprinkler_state)
	digitalWrite(pinAlarm, alarm_state)
	customWrite(pinDrain, drain_state)
	customWrite(pinLCD, LCD_state)
	#
	save_actuator('sprinkler', sprinkler_state)
	save_actuator('alarm', alarm_state)
	save_actuator('drain', drain_state)
	save_actuator('lcd_nivel_agua', LCD_state)


# Função chamada quando acabar a chamada a API
def onPostHTTPDone(status, data, replyHeader):
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
	
# Função para leer da data no sistema
def getData():
	return strftime('%d-%m-%Y',gmtime())

# Função para leer a hora no sistema
def getHora():
	return strftime('%H:%M:%S',gmtime())

# Função para guardar o estado dos atuadores no Servidor
def save_actuator(name, state):
	data = getData()
	hora = getHora()
	state_text = state if not (type(state)==bool) else 'True' if state else 'False'
	state_text = str(state_text) if (type(state_text)==int) else state_text.replace('\n','')
	print(name + ':' + state_text + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': name , 'valor': state_text , 'data': data, 'hora': hora}
	httpPost.post(urlPost, array_dados)
	httpPost.onDone(onPostHTTPDone)


def main():
    # Vai guardar as portas de cada equipamento
	pinMode(pinLCD,OUT)
	pinMode(pinAlarm,OUT)
	pinMode(pinSprinler,OUT)
	pinMode(pinDrain, OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	httpGet.onDone(onGetHTTPDone)
	while True:
        # Vai fazer a chamada a API
		httpGet.get(urlGet)
		sleep(1)
		
if __name__ == "__main__":
	main()