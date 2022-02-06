
<?php
	$log_temp = file_get_contents("../../files/temperatura/log.txt");
	$list_logs = preg_split("/\\r\\n|\\r|\\n/",$log_temp);
	rsort($list_logs);
	$icon = "ºC"
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
			<h1>Histórico de Temperatura de AquaPark</h1>
			<a href="../../index.html" >Página inicial</a>
			<div>
				<table class="table table-striped">
					<thead class="thead-dark text-center">
						<tr>
							<th scope="col">Data</th>
							<th scope="col">Hora</th>
							<th scope="col">Temperatura</th>
						</tr>
					</thead>
					<tbody>
						<?php 
							foreach($list_logs as $log){
								if($log <> "") {
									$data = explode(";",$log);
									echo "<tr>";
									echo "<td scope='row' class='text-center'><p>".$data[0]."</p></td>";
									echo "<td scope='row' class='text-center'><p>".$data[1]."</p></td>";
									echo "<td scope='row' class='text-center'><p>".$data[2].$icon."</p></td>";
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
