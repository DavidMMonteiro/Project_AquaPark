from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
urlGet = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=luz&type=valor"
# Url API para guardar atuadores
urlPost = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?"
# Equipamente
pinLamp = A0
LCD = A1
#
httpGet = RealHTTPClient()
httpPost = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onGetHTTPDone(status, data):
	lamp_state = 0
	lcd_state = "Nao conseguio leer"
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		#
		light = float(data.replace(" ",""))
		# Filtra os dados da API
		if  light >= 60: 
			# Caso os valores for maior ou igual a 60, vai manter as luzes apagadas
			lamp_state = 0
			lcd_state = "Luzes: Off"
		elif light > 20 and light <= 60: 
			# Caso os valores for maior a 20 mas menor do que 60, vai manter as luzes a media potencia
			lamp_state = 1
			lcd_state = "Luzes: Medio"
		elif light <= 20: 
			# Caso os valores for menor ou igual a 20, vai manter as luzes a maxima potencia
			lamp_state = 2
			lcd_state = "Luzes: Full"
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
	customWrite(pinLamp, lamp_state)
	customWrite(LCD, lcd_state)
	#
	save_actuator('lamp',lamp_state)
	save_actuator('lcd_light', lcd_state)

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
	state_text = str(state_text) if (type(state_text)==int) else state_text
	state_text = state_text.replace('\n','')
	print(name + ':' + state_text + ' Date:' + data + ' Hora:' + hora)
	array_dados = {'nome': name , 'valor': state_text , 'data': data, 'hora': hora}
	httpPost.post(urlPost, array_dados)
	httpPost.onDone(onPostHTTPDone)


def main():
    # Vai guardar as portas de cada equipamento
	pinMode(pinLamp,OUT)
	pinMode(LCD,OUT)
    # Vai atribuir a função onGetHTTPDone a varivel http
	httpGet.onDone(onGetHTTPDone)
	while True:
        # Vai fazer a chamada a API
		httpGet.get(urlGet)
		sleep(1)
		
if __name__ == "__main__":
	main()