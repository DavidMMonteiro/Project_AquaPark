<?php
	$log_temp = file_get_contents("../files/temperatura/log.txt");
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Lab02 - Histórico de Temperatura</h1>
		<h3>Estado(Data de atualização)</h3>
		<p><?php echo str_replace("\n", "<br>", $log_temp)?></p>
	</body>
	<footer><a href="../index.html" >Página inicial</a></li></footer>
</html>
