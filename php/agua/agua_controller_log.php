<?php
	$logs = file_get_contents("../../files/nivel_agua/log.txt");
	$list_logs = preg_split("/\\r\\n|\\r|\\n/",$logs);	
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Histórico de humidade de AquaPark</h1>
		<a href="../../index.html" >Página inicial</a>
		<div>
		<table>
				<thead>
					<tr>
						<th width = "100px">Data</th>
						<th width = "100px">Hora</th>
						<th width = "100px">Nivel agua</th>
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
								echo "<td style='text-align:center'><p>".$data[2]." cm</p></td>";
								echo "</tr>";
							}
						}
					?>
				</tbody>
			</table>
		</div>	
	</body>
</html>
