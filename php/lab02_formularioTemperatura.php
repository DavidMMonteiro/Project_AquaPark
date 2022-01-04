<?php
	$default_txt = "No data";
	$valor_temperatura = file_get_contents("../files/temperatura/valor.txt");
	$update_date = file_get_contents("../files/temperatura/hora.txt");
	$valor_temperatura = $valor_temperatura == ""? $default_txt:$valor_temperatura;
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Lab02 - Formulario de Temperatura</h1>
		<form action="../api/api.php" method="post">
		  <label for="valor">Temperatura:</label>
		  <input type="number" id="valor" name="valor"><br><br>
		  <label for="data">Data:</label>
		  <input type="date" id="data" name="data"><br><br>
		  <label for="data">Hora:</label>
		  <input type="time" id="hora" name="hora"><br><br>
		  <input type="submit" value="Submit">
		</form>
	</body>
	<footer><a href="../index.html" >Página inicial</a></footer>
</html>
