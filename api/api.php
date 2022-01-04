<?php
	header('Content-Type: text/html; charset=utf-8');
	//header("Location:http://127.0.0.1/prsi/Project_AquaPark/index.html");
	$type = $_SERVER["REQUEST_METHOD"];
	if($type == "POST") {
		 echo "Recebido um POST\n";
		 print_r($_POST);
		 if(isset($_POST["valor"], $_POST["hora"])) {
			 echo "Valores aceites. \nGuardando em ficheiros locais.";
			 $nome = $_POST["nome"];
			 $date = str_replace("-","/",$_POST["data"])." ".$_POST["hora"];
			 echo file_put_contents("../files/".$nome."/valor.txt",$_POST["valor"]);
			 echo file_put_contents("../files/".$nome."/hora.txt", $date);
			 echo file_put_contents("../files/".$nome."/log.txt", "\n".$date.";".$_POST["valor"].($nome == "temperatura" ? "º" : "%"),FILE_APPEND);

		 } else {
			 echo "Falta de dados. \nLocal save cancelada.";
		 }
	} else if ($type == "GET") {
		$data = file_get_contents("../files/".$_GET["nome"]."/".$_GET["type"].".txt");
		echo $data;
	} else {
		 echo "Metodo não permitido";
	}
	exit();
 ?>