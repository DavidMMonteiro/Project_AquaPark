from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer temperatura
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=nivel_agua&type=valor"
# Equipamente
pinSprinler = A2
pinAlarm = A1
pinLCD = A0
#
http = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onHTTPDoneCooler(status, data):
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		# Filtra os dados da API
		minValue = 10
		maxValue = 40
		qunt = float(data.replace(" ",""))
		if  qunt < minValue:
			digitalWrite(pinSprinler, 1)
			digitalWrite(pinAlarm, 0)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nSprinler: ON")
		elif qunt >= minValue and qunt < maxValue:
			digitalWrite(pinAlarm, 1)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nWARNING! ")
		elif qunt >= maxValue:
			digitalWrite(pinSprinler, 0)
			digitalWrite(pinAlarm, 1)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nSprinler: OFF")

    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
		digitalWrite(pinSprinler, 0)
		digitalWrite(pinAlarm, 0)
		customWrite(pinLCD, "H2O Level: --- cm\nSprinler: OFF")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(pinLCD,OUT)
	pinMode(pinAlarm,OUT)
	pinMode(pinSprinler,OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	http.onDone(onHTTPDoneCooler)
	while True:
        # Vai fazer a chamada a API
		http.get(url)
		sleep(1)
		
if __name__ == "__main__":
	main()