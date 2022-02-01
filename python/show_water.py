from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer temperatura
url = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=nivel_agua&type=valor"
# Equipamente
pinDrain = A3
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
		# Valor em cm
		minValue = 10 
		maxValue = 40
		# Filtra os dados da API
		qunt = float(data.replace(" ",""))
		if  qunt < minValue: # Caso valor for inferior ao minimo, ativa o aspersor, fechar o esgoto e desativa a alarma
			digitalWrite(pinSprinler, HIGH)
			customWrite(pinDrain, 0)
			digitalWrite(pinAlarm,LOW)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nSprinler: ON")
		# Caso a valor for comprendi entre o minimo e o maximo, 
		# ativa a alarma para avisar aos utilizadores	
		elif qunt >= minValue and qunt < maxValue: 
			digitalWrite(pinAlarm, HIGH)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nWARNING! ")
		# Caso a valor for maior o maximo, 
		# ativa a alarma e desativa o aspersor e abrir o esgoto
		elif qunt >= maxValue:
			digitalWrite(pinSprinler, LOW)
			digitalWrite(pinAlarm, HIGH)
			customWrite(pinDrain, 1)
			customWrite(pinLCD, "H2O Level:" + data + "cm\nDrain: ON")

    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
		digitalWrite(pinSprinler, LOW)
		digitalWrite(pinAlarm, LOW)
		customWrite(pinDrain, 0)
		customWrite(pinLCD, "Nao conseguio leer")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(pinLCD,OUT)
	pinMode(pinAlarm,OUT)
	pinMode(pinSprinler,OUT)
	pinMode(pinDrain, OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	http.onDone(onHTTPDoneCooler)
	while True:
        # Vai fazer a chamada a API
		http.get(url)
		sleep(1)
		
if __name__ == "__main__":
	main()