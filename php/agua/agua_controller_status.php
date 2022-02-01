<?php
	include('/Project_Aquapark');
	$default_txt = "No data";
	$valor = file_get_contents("../../files/nivel_agua/valor.txt");
	$update_date = file_get_contents("../../files/nivel_agua/hora.txt");
	$valor = $valor == ""? $default_txt:$valor." cm";
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Nível de agua em AquaPark</h1>
		<p><a href="../../index.html" >Página inicial</a></p>
		<h3>Nível Água Atual:</h3>
		<p><?php echo $valor?></p>
		<h3>Data atualização do Nível da agua:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
		<h3>Estado de LED</h3>
		<?php
			$state = isset($valor, $update_date) && ($valor != $default_txt && $update_date != $default_txt)? "on" : "off";
			echo "<img src='../../img/led-".$state.".png' title='Led State: ".$state."'>"
		?>
		<h3>Data atualização do LED:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
	</body>
</html>
