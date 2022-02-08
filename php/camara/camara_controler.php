<?php
	$default_txt = "No data";
	$camara_value = file_get_contents("../../files/img/valor.txt");
	$update_date = file_get_contents("../../files/img/hora.txt");
	$camara_state =  $camara_value> 0 ? "Ligada" : "Desliga";
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Webcam AquaPark</h1>
        <div><a href="../../index.html" >Página inicial</a> | <a href="logs.php" >Página Logs WebCamara</a></div>
		<!--form action="../../api/upload.php" method="post" enctype = "multipart/form-data">
			<p>Selecione uma imagem para fazer upload:</p>
			<input type='file' name='imagem' id='fileToUpload'>
			<br>
			<input type='submit' value='Upload Imagem' name='submit'>
		</form-->
		<div>
			<p>
				<?php
					echo "Camara estado: ".$camara_state;
					echo "<br>Ultima atualização: ".$update_date;	
				?>
			</p>
            <?php
                echo "<img src='../../files/img/camara.jpg?id=".time()."' style='width: 50%;'>";
            ?>
        </div>
	</body>
</html>
