
<?php
	$logs = (file_get_contents("../../../files/fan/log.txt"));
	$list_logs = preg_split("/\\r\\n|\\r|\\n/",$logs);
	rsort($list_logs);
	
	function fan_state($fan_data) {
		if (!strcmp($fan_data,"0"))
			return "Desativada";
		elseif (!strcmp($fan_data,"1"))
			return "Media Velocidade";
		elseif (!strcmp($fan_data,"2"))
			return "Maxima Velocidade";
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
	</head>

	<body>
		<div class="container-fluid">
			<h1>Histórico de Estado da Ventoilha</h1>
			<a href="../hum_actores.php" >Página Atuadores</a>
			<div>
				<table class="table table-striped">
					<thead class="thead-dark text-center">
						<tr>
							<th scope="col">Data</th>
							<th scope="col">Hora</th>
							<th scope="col">Estado</th>
						</tr>
					</thead>
					<tbody>
						<?php 
							foreach($list_logs as $log){
								if($log <> "") {
									$data = explode(";",$log);
									echo "<tr>";
									echo "<td style='text-align:center'><p>".$data[0]."</p></td>";
									echo "<td style='text-align:center'><p>".$data[1]."</p></td>";
									echo "<td style='text-align:center'><p>".fan_state($data[2])."</p></td>";
									echo "</tr>";
								}
							}
						?>
					</tbody>
				</table>
			</div>
		</div>
	</body>
</html>
