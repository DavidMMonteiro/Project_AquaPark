<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Formulario de Temperatura - AquaPark</h1>
		<form action="../api/api.php" method="post">
		  <label for="nome">Nome:</label>
		  <input type="text" id="nome" name="nome"><br><br>
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
