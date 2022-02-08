<?php

	function save_file($sourceFile){
		if (!file_exists("../files/img")) {
			mkdir("../files/img", 0777, true);
			echo("<br>Pasta img criada");
		}
		if(move_uploaded_file($sourceFile, "../files/img/camara.jpg")){
			echo("<br>Upload da imagem realizado com sucesso");
		}else{
			echo("<br>Erro no Upload da imagem");
		}
	}
	// Vai ler o tipo de Request feita
	$type = $_SERVER["REQUEST_METHOD"];
	// Caso for um POST
	if($type == "POST") {
		if(isset($_FILES['imagem']))
		{
			echo('Got the image');
			echo('<br>Imagem Nome: '.$_FILES['imagem']['name']);
			echo('<br>Imagem Tipo: '.$_FILES['imagem']['type']);
			echo('<br>Imagem Temporal Name: '.$_FILES['imagem']['tmp_name']);
			save_file($_FILES['imagem']['tmp_name']);
		}else{
			echo ('Erro - não existe imagem');
		}
	// Caso for um GET, verifica que tem a informação necesaria
	} else if ($type == "GET") {
		
	// Caso o Request for um tipo não utilizado
	} else {
		throw new Exception("Metodo não permitido");
	}
	exit();
 ?>