from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=luz&type=valor"
# Equipamente
pinLamp = A0
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
		light = float(data.replace(" ",""))
		# Filtra os dados da API
		if  light >= 60: 
			# Caso os valores for maior ou igual a 60, vai manter as luzes apagadas
			customWrite(pinLamp, 0)
			customWrite(LCD, "Luzes: Off")
		elif light > 20 and light <= 60: 
			# Caso os valores for maior a 20 mas menor do que 60, vai manter as luzes a media potencia
			customWrite(pinLamp, 1)
			customWrite(LCD, "Luzes: Medio")
		elif light <= 20: 
			# Caso os valores for menor ou igual a 20, vai manter as luzes a maxima potencia
			customWrite(pinLamp, 2)
			customWrite(LCD, "Luzes: Full")
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
        # Vai desligar equipamento e mostrar informação ao utilizor
		customWrite(pinLamp, 0)
		customWrite(LCD, "Nao conseguio leer")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(pinLamp,OUT)
	pinMode(LCD,OUT)
    # Vai atribuir a função onHTTPDone a varivel http
	http.onDone(onHTTPDone)
	while True:
        # Vai fazer a chamada a API
		http.get(url)
		sleep(1)
		
if __name__ == "__main__":
	main()