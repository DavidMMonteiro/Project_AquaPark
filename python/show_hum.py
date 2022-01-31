from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer humidade
urlFan = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=humidade&type=valor"
# Equipamente
FAN = A1
LCD_FAN = A0
#
http = RealHTTPClient()

# Quando a chamada a API estiver comcluida
def onHTTPDoneFan(status, data):
    # Se a chamada for bem sucedida
	if status == 200:
        # Mostra informação no pront
		print("OK: GET realizado com sucesso")
		print("Status code: " + str(status))
		print("Resposta: " + str(data))
		#
		hum = float(data.replace(" ",""))
		# Filtra os dados da API
		if  hum < 20.0: 
			# Caso os valores forem menores de 30 vai desligar a ventoinha e mostrar informação ao utilizor
			customWrite(FAN,"0")
			customWrite(LCD_FAN, "HUMI:" + data + " % \nFAN: OFF")
		elif hum >= 20.0 and hum < 60.0: 
			# Caso os valores forem maiores de 20 e menores de 60 vai ativar
			# a ventoinha a meia velocidade e mostrar informação ao utilizador
			customWrite(FAN,"1")
			customWrite(LCD_FAN, "HUMI:" + data + " % \nFAN: ON")
		elif hum >= 60.0: 
			# Caso os valores forem maior de 60 vai ativar 
			# a ventoinham ao maximo e mostrar informação ao utilizador
			customWrite(FAN,"2")
			customWrite(LCD_FAN, "HUMI:" + data + " % \nFAN: ON")
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
        # Vai desligar equipamento e mostrar informação ao utilizor
		customWrite(FAN,"0")
		customWrite(LCD_FAN, "HUMI: --- % \nFAN: OFF")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(FAN,OUT)
	pinMode(LCD_FAN,OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	http.onDone(onHTTPDoneFan)
	while True:
        # Vai fazer a chamada a API
		http.get(urlFan)
		sleep(1)
		
if __name__ == "__main__":
	main()