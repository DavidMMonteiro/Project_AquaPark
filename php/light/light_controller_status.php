<?php
	$default_txt = "No data";
	$valor_luz = file_get_contents("../../files/luz/valor.txt");
	$update_date = file_get_contents("../../files/luz/hora.txt");
	if ($valor_luz == "")
		$valor_luz = $default_txt;
	else if ($valor_luz >= 100)
		$valor_luz = "Dia. Luz Apagada";
	else if ($valor_luz < 20)
		$valor_luz = "Noite. Luz Maxima";
	else
		$valor_luz = "Manha/Tarde. Luz Media";
	$update_date = $update_date == ""? $default_txt:$update_date;
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Luz de AquaPark</h1>
		<h3>Luz Atual:</h3>
		<p><?php echo $valor_luz;?></p>
		<h3>Data atualização de luz:</h3>
		<p>
			<?php 
				$data = explode(";", $update_date);
				echo $data[0] ." ".$data[1];
			?>
		</p>
		<h3>Estado de LED</h3>
		<?php
			$state = isset($valor_luz, $update_date) && ($valor_luz != $default_txt && $update_date != $default_txt)? "on" : "off";
			echo "<img src='../../img/led-".$state.".png' title='Led State: ".$state."'>";
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
