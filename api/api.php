<?php
	header('Content-Type: text/html; charset=utf-8');
	$type = $_SERVER["REQUEST_METHOD"];
	if($type == "POST") {
		 echo "Recebido um POST\n";
		 print_r($_POST);
		 if(isset($_POST["valor"], $_POST["hora"], $_POST["nome"])) {
			 $nome = $_POST["nome"];
			 echo "Valores aceites. \nGuardando em ficheiros locais.\n";
			 if (!file_exists("../files/".$nome)) {
				echo "Criando nova diretoria ".$nome."!\n";
				mkdir("../files/".$nome, 0777, true);
			}
			 $date = str_replace("-","/",$_POST["data"])." ".$_POST["hora"];
			 echo file_put_contents("../files/".$nome."/valor.txt",$_POST["valor"]);
			 echo file_put_contents("../files/".$nome."/hora.txt", $date);
			 echo file_put_contents("../files/".$nome."/log.txt", "\n".$date.";".$_POST["valor"],FILE_APPEND);
			 echo "Valores guardados com sucesso";
		 } else {
			 echo "\nFalta de dados. \nLocal save cancelada.";
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