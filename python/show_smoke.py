from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=fumo&type=valor"
# Equipamente
WINDOW = A0
LCD = A1
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
		smoke = float(data.replace(" ",""))
		# Filtra os dados da API
		if  smoke < 50: 
			# Caso os valores forem menores de 50% vai fechar a janela e mostrar informação ao utilizor
			customWrite(WINDOW,"0")
			customWrite(LCD, "Fumo:" + data + " % \nWindow: Close")
		else: 
			# Caso os valores forem maiores de 50% vai abrir a janela
			customWrite(WINDOW,"1")
			customWrite(LCD, "Fumo:" + data + " % \nWindow: Open")
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
        # Vai desligar equipamento e mostrar informação ao utilizor
		customWrite(WINDOW,"0")
		customWrite(LCD, "Nao conseguio leer")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(WINDOW,OUT)
	pinMode(LCD,OUT)
    # Vai atribuir a função onHTTPDone a varivel http
	http.onDone(onHTTPDone)
	while True:
        # Vai fazer a chamada a API
		http.get(url)
		sleep(1)
		
if __name__ == "__main__":
	main()