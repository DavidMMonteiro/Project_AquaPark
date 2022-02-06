
<?php
	$nivel_agua = file_get_contents("../../files/nivel_agua/valor.txt") . 'cm';
	$sprinkler = file_get_contents("../../files/sprinkler/valor.txt");
	$sprinkler_date = file_get_contents("../../files/sprinkler/hora.txt");
	$drain = file_get_contents("../../files/drain/valor.txt");
	$drain_date = file_get_contents("../../files/drain/hora.txt");
	$alarm = file_get_contents("../../files/alarm/valor.txt");
	$alarm_date = file_get_contents("../../files/alarm/hora.txt");
	$LCD = file_get_contents("../../files/lcd_nivel_agua/valor.txt");
	$LCD_date = file_get_contents("../../files/lcd_nivel_agua/hora.txt");
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
			<h1>Estado Atuadores Nivel Agua</h1>
			<a href="../../index.html" >Página inicial</a>
			<div class="row">
				<div class= "col-12">
					<div class="text-center border rounded my-2">
						<h3>Nivel Atual</h3>
						<?php 
							echo "<span class='px-3 bg-dark text-white rounded'>".$nivel_agua."</span>"
						?>
						<br>
						<a href="agua_controller_log.php">Histórico do Nível Agua</a>
					</div>
				</div>
				<div class = "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
					<div class="text-center border rounded">
						<h3>Aspersor</h3>
						<?php
							$state = (isset($sprinkler) && $sprinkler > 0) ? "on" : "off";
							echo "<img class='my-2' src='../../img/led-".$state.".png' title='Cooler State: ".$state."'>";
							echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$sprinkler_date."</span>";
						?>
						<br>
						<a href="logs/sprinkler_logs.php">Histórico da Aspersor</a>
					</div>
				</div>
				<div class = "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
					<div class="text-center border rounded">
						<h3>Esgoto</h3>
						<?php
							$state = (isset($drain) && $drain > 0) ? "on" : "off";
							echo "<img class='my-2' src='../../img/led-".$state.".png' title='Cooler State: ".$state."'>";
							echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$sprinkler_date."</span>";
						?>
						<br>
						<a href="logs/drain_logs.php">Histórico do Esgoto</a>
					</div>
				</div>
				<div class = "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
					<div class="text-center border rounded">
						<h3>Alarma</h3>
						<?php
							$state = (isset($alarm) && $alarm > 0) ? "on" : "off";
							echo "<img class='my-2' src='../../img/led-".$state.".png' title='Cooler State: ".$state."'>";
							echo "<p>Ultima atualização:</p> <span class='px-3 bg-dark text-white rounded'>".$sprinkler_date."</span>";
						?>
						<br>
						<a href="logs/sprinkler_logs.php">Histórico da Alarma</a>
					</div>
				</div>
				<div class = "col-xl-6 col-lg-6 col-md-12 col-sm-12 col-12">
					<div class="text-center border rounded">
					<h3>LCD Nível Agua</h3>
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
