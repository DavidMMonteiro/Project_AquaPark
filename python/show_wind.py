from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=vento&type=valor"
# Equipamente
LCD = A0
#
http = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onHTTPDone(status, data):
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		#
		wind = data.replace(" ","")
		# Filtra os dados da API
		if  wind: 
			# Caso for detetado vento
			customWrite(LCD, "Vento: Detect")
		else: 
			# Caso não for detetado vento
			customWrite(LCD, "Vento: No Detect")
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
        # Vai desligar equipamento e mostrar informação ao utilizor
		customWrite(LCD, "Nao conseguio leer")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(LCD,OUT)
    # Vai atribuir a função onHTTPDone a varivel http
	http.onDone(onHTTPDone)
	while True:
        # Vai fazer a chamada a API
		http.get(url)
		sleep(1)
		
if __name__ == "__main__":
	main()