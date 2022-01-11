<?php
	$logs_hum = file_get_contents("../files/humidade/log.txt");
	$list_logs = preg_split("/\\r\\n|\\r|\\n/",$logs_hum);	
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Histórico de humidade de AquaPark</h1>
		<h3>Estado(Data de atualização)</h3>
		<?php 
			foreach($list_logs as $log){
				if($log <> "")echo "<p>".$log."%</p>";
			}
		?>		
	</body>
	<footer><a href="../index.html" >Página inicial</a></li></footer>
</html>
