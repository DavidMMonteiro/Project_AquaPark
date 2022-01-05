<?php
	header('Content-Type: text/html; charset=utf-8');
	$type = $_SERVER["REQUEST_METHOD"];
	if($type == "POST") {
		 echo "Recebido um POST<br>";
		 print_r($_POST);
		 if(isset($_POST["valor"], $_POST["hora"], $_POST["nome"])) {
			 $nome = $_POST["nome"];
			 echo "<br>Valores aceites. <br>Guardando em ficheiros locais.";
			 if (!file_exists("../files/".$nome)) {
				echo "<br>Criando nova diretoria <b>".$nome."</b>! ";
				mkdir("../files/".$nome, 0777, true);
			}
			 $date = str_replace("-","/",$_POST["data"])." ".$_POST["hora"];
			 echo file_put_contents("../files/".$nome."/valor.txt",$_POST["valor"]);
			 echo file_put_contents("../files/".$nome."/hora.txt", $date);
			 echo file_put_contents("../files/".$nome."/log.txt", "\n".$date.";".$_POST["valor"],FILE_APPEND);
			 echo "<br>Valores guardados com sucesso";
		 } else {
			 echo "<br<Falta de dados.<br>Local save cancelada.";
		 }
	} else if ($type == "GET") {
		if (file_exists("../files/".$nome)) {
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