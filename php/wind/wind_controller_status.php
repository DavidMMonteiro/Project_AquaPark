<?php
	$default_txt = "No data";
	$valor_vento = file_get_contents("../../files/vento/valor.txt");
	$update_date = file_get_contents("../../files/vento/hora.txt");
	$valor_vento = $valor_vento == ""? $default_txt:$valor_vento;
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Vento de AquaPark</h1>
		<h3>Vento Atual:</h3>
		<p><?php echo $valor_vento >= 1 ? "Detetado" : "Não Detetado" ?></p>
		<h3>Data atualização de vento:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
		<h3>Estado de LED</h3>
		<?php
			$state = isset($valor_vento, $update_date) && ($valor_vento != $default_txt && $update_date != $default_txt)? "on" : "off";
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
	<footer><a href="../../index.html" >Página inicial</a></footer>
</html>
