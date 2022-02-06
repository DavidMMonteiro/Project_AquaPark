from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer temperatura
urlGet = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=temperatura&type=valor"
# Url API para guardar atuadores temperatura
urlPost = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?"
# Equipamente
HEATER = A2
COOLER = A1
LCD_COOLER = A0
#
httpGet = RealHTTPClient()
httpPost = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onGetHTTPDone(status, data):
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		temp = 30
		cooler = False
		heater = False
		LCD_text = ""
		# Filtra os dados da API
		if float(data.replace(" ","")) < temp:
			# Caso os valores forem menores de temp vai desligar equipamento e mostrar informação ao utilizor
			cooler = False
			heater = True
			LCD_text = "TEMP:" + data + " ºC \nHEATER: ON"
			digitalWrite(HEATER, HIGH)
			digitalWrite(COOLER, LOW)
			customWrite(LCD_COOLER, LCD_text)
		else:
			# Caso os valores forem maior de temp vai ativar o equipamento e mostrar informação ao utilizador
			cooler = True
			heater = False
			LCD_text = "TEMP:" + data + " ºC \nCOOLER: ON"
			digitalWrite(HEATER,LOW)
			digitalWrite(COOLER, HIGH)
			customWrite(LCD_COOLER, LCD_text)
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
		# Caso os valores forem menores de 25 vai desligar equipamento e mostrar informação ao utilizor
		cooler = False
		heater = False
		LCD_text = "Nao conseguio leer"
		digitalWrite(HEATER,LOW)
		digitalWrite(COOLER,LOW)
		customWrite(LCD_COOLER, LCD_text)
	
	save_actuator('cooler', cooler)
	save_actuator('heater', heater)
	save_actuator('lcd_temp', LCD_text)

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
	state_text = state_text.replace('\n','')
	print(name + ':' + state_text + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': name , 'valor': state_text , 'data': data, 'hora': hora}
	httpPost.post(urlPost, array_dados)
	httpPost.onDone(onPostHTTPDone)

def main():
    # Vai guardar as portas de cada equipamento
	pinMode(LCD_COOLER,OUT)
	pinMode(COOLER,OUT)
	pinMode(HEATER, OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	httpGet.onDone(onGetHTTPDone)
	while True:
        # Vai fazer a chamada a API
		httpGet.get(urlGet)
		sleep(1)
		
if __name__ == "__main__":
	main()