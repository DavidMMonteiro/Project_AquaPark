<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
<?php
	$log_temp = file_get_contents("../files/temperatura/log.txt");
?>

	<body>
		<h1>Histórico da Entrada - AquaPark</h1>
		<h3>Estado(Data de Abertura - Data de Fecho)</h3>
		<p><?php echo str_replace("\n", "<br>", $log_temp)?></p>
	</body>
	<footer><a href="../index.html" >Página inicial</a></li></footer>
</html>
