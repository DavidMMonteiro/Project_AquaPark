<?php
	$default_txt = "No data";
	$valor = file_get_contents("../files/nivel_agua/valor.txt");
	$update_date = file_get_contents("../files/nivel_agua/hora.txt");
	$valor = $valor == ""? $default_txt:$valor;
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Nivel de agua em AquaPark</h1>
		<h3>Nivel Atual:</h3>
		<p><?php echo $valor . " cm"?></p>
		<h3>Data atualização do nivel da agua:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
		<h3>Estado de LED</h3>
		<?php
			$state = isset($valor, $update_date) && ($valor != $default_txt && $update_date != $default_txt)? "on" : "off";
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
