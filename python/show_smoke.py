from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
urlGet = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=fumo&type=valor"
# Url API para guardar atuadores temperatura
urlPost = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?"
# Equipamente
WINDOW = A0
LCD = A1
#
httpGet = RealHTTPClient()
httpPost = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onGetHTTPDone(status, data):
	window_state = "0"
	lcd_state = "Nao conseguio leer"
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		#
		smoke = float(data.replace(" ",""))
		# Filtra os dados da API
		if  smoke < 50: 
			# Caso os valores forem menores de 50% vai fechar a janela e mostrar informação ao utilizor
			window_state = "0"
			lcd_state = "Fumo:" + data + " % \nWindow: Close"
		else: 
			# Caso os valores forem maiores de 50% vai abrir a janela
			window_state = "1"
			lcd_state = "Fumo:" + data + " % \nWindow: Open"
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))

	customWrite(WINDOW, window_state)
	customWrite(LCD, lcd_state)
	#
	save_actuator('window', window_state)
	save_actuator('lcd_smoke', lcd_state)

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
	pinMode(WINDOW,OUT)
	pinMode(LCD,OUT)
    # Vai atribuir a função onGetHTTPDone a varivel http
	httpGet.onDone(onGetHTTPDone)
	while True:
        # Vai fazer a chamada a API
		httpGet.get(urlGet)
		sleep(1)
		
if __name__ == "__main__":
	main()