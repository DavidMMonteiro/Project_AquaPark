from gpio import *
from time import *
from realhttp import *

# Variaveis

# Url API para leer temperatura
urlCooler = "http://127.0.0.1/prsi/Project_AquaPark/api/api.php?nome=temperatura&type=valor"
# Equipamente
COOLER = A1
LCD_COOLER = A0
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
		if float(data.replace(" ","")) < 30:
			# Caso os valores forem menores de 25 vai desligar equipamento e mostrar informação ao utilizor
			analogWrite(COOLER,LOW)
			analogWrite(COOLER,0)
			customWrite(LCD_COOLER, "TEMP:" + data + " ºC \nCOOLER: OFF")
		else:
			# Caso os valores forem maior de 25 vai ativar o equipamento e mostrar informação ao utilizador
			analogWrite(COOLER,HIGH)
			analogWrite(COOLER,1)
			customWrite(LCD_COOLER, "TEMP:" + data + " ºC \nCOOLER: ON")
    # Caso não seixa bem sucedida
	else:
        # Vai mostrar uma mensagem de erro no pront
		print("ERRO: Nao foi possivel realizar o pedido")
		print("Status Code: " + str(status))
		# Caso os valores forem menores de 25 vai desligar equipamento e mostrar informação ao utilizor
		analogWrite(COOLER,LOW)
		analogWrite(COOLER,0)
		customWrite(LCD_COOLER, "TEMP: --- ºC \nCOOLER: OFF")



def main():
    # Vai guardar as portas de cada equipamento
	pinMode(LCD_COOLER,OUT)
	pinMode(COOLER,OUT)
    # Vai atribuir a função onHTTPDoneFan a varivel http
	http.onDone(onHTTPDoneCooler)
	while True:
        # Vai fazer a chamada a API
		http.get(urlCooler)
		sleep(1)
		
if __name__ == "__main__":
	main()