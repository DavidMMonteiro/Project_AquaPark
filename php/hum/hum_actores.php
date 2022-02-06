
<?php
	$actual_date = date("Y/m/d;h:i:sa"); 
	$temp = file_get_contents("../../files/temperatura/valor.txt") . 'ºC';
	$cooler = file_get_contents("../../files/cooler/valor.txt");
	$cooler_date = file_get_contents("../../files/cooler/hora.txt");
	$heater = file_get_contents("../../files/heater/valor.txt");
	$heater_date = file_get_contents("../../files/heater/hora.txt");
	$LCD = file_get_contents("../../files/lcd_temp/valor.txt");
	$LCD_date = file_get_contents("../../files/lcd_temp/hora.txt");
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
			<h1>Estado Atuadores Temperatura</h1>
			<a href="../../index.html" >Página inicial</a>
			<div class="row">
				<div class= "col-12">
					<div class="text-center border rounded my-2">
						<h3>Temperatura Atual</h3>
						<?php 
							echo "<span class='px-3 bg-dark text-white rounded'>".$temp."</span>"
						?>
						<br>
						<a href="temp_controller_log.php">Histórico da Temperatura</a>
					</div>
				</div>
				<div class = "col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
					<div class="text-center border rounded">
						<h3>Cooler</h3>
						<?php
							$state = isset($cooler) && !strcmp($cooler,'True') ? "on" : "off";
							echo "<img class='my-2' src='../../img/led-".$state.".png' title='Cooler State: ".$state."'>";
							echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$cooler_date."</span>";
						?>
						<br>
						<a href="logs/cooler_logs.php">Histórico do Cooler</a>
					</div>
				</div>
				<div class = "col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
					<div class="text-center border rounded">
					<h3>Aquecedor</h3>
					<?php
						$state = isset($heater) && !strcmp($heater,'True') ? "on" : "off";
						echo "<img class='my-2' src='../../img/led-".$state.".png' title='Heater State: ".$state."'>";
						echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$heater_date."</span>";
					?>
					<br>
					<a href="logs/heater_logs.php">Histórico do Aquecedor</a>
					</div>
				</div>
				<div class = "col-xl-4 col-lg-4 col-md-12 col-sm-12 col-12">
					<div class="text-center border rounded">
					<h3>LCD</h3>
					<?php
						echo "<p>Texto LCD: <br>" .$LCD. "</p>";
						echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$LCD_date."</span>";
					?>
					<br>
					<a href="logs/lcd_logs.php">Histórico do LCD</a>
					</div>
				</div>			
			</div>
		</div>
	</body>
</html>
