<?php
	header('Content-Type: text/html; charset=utf-8');
	//

	function save_file($sourcefile){
		if (move_uploaded_file($sourcefile, "../files/img/webcam.png")) {
			echo (' Image save succefully! ');
		} else {
			echo (' Image save went wrong! ');
		}
	}

	//
	$type = $_SERVER["REQUEST_METHOD"];
	if($type == "POST") {
		if(isset($_FILES['imagem'])) {
			save_file($_FILES['imagem'][tmp_name]);
		} else if(isset($_POST["valor"], $_POST["hora"], $_POST["nome"])) {
			 $nome = $_POST["nome"];
			 if (!file_exists("../files/".$nome)) {
				mkdir("../files/".$nome, 0777, true);
			}
			 $date = str_replace("-","/",$_POST["data"]).";".$_POST["hora"];
			 echo file_put_contents("../files/".$nome."/valor.txt",$_POST["valor"]);
			 echo file_put_contents("../files/".$nome."/hora.txt", $date);
			 echo file_put_contents("../files/".$nome."/log.txt", "\n".$date.";".$_POST["valor"],FILE_APPEND);
		 } else {
			 echo "<br<Falta de dados.<br>Local save cancelada.";
		 }
	} else if ($type == "GET" && isset($_GET["nome"], $_GET["type"])) {
		if (file_exists("../files/".$_GET["nome"])) {
			$data = file_get_contents("../files/".$_GET["nome"]."/".$_GET["type"].".txt");
			echo $data;
		} else {
			echo "Diretoria não encontrada";
		}
	} else {
		 echo "Metodo não permitido";
	}
	exit();
 ?>