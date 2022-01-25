<?php
	$default_txt = "No data";
	$valor_Humidade = file_get_contents("../files/humidade/valor.txt");
	$update_date = file_get_contents("../files/humidade/hora.txt");
	$valor_Humidade = $valor_Humidade == ""? $default_txt:$valor_Humidade;
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Humidade em AquaPark</h1>
		<h3>Humidade Atual:</h3>
		<p><?php echo $valor_Humidade . "%"?></p>
		<h3>Data atualização de Humidade:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
		<h3>Estado de LED</h3>
		<?php
			$state = isset($valor_Humidade, $update_date) && ($valor_Humidade != $default_txt && $update_date != $default_txt)? "on" : "off";
			echo "<img src='../img/led-".$state.".png' title='Led State: ".$state."'>"
		?>
		<h3>Data atualização do LED:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
	</body>
	<footer><a href="../index.html" >Página inicial</a></footer>
</html>
