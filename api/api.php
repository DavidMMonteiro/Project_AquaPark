<?php
	header('Content-Type: text/html; charset=utf-8');

	// Vai ler o tipo de Request feita
	$type = $_SERVER["REQUEST_METHOD"];
	// Caso for um POST
	if($type == "POST") {
		// Verifica se vai procesar informação de arduino
		// e se tem a informação necesaria para poder procesar a informação
		if(isset($_POST["valor"], $_POST["hora"], $_POST["nome"])) {
			 $nome = $_POST["nome"]; // Guarda o nove do dato a ser procesado
			 // Caso não encontrar a pasta para guarda a informação fornecida
			 // vai criar o correspondente pasta
			 if (!file_exists("../files/".$nome)) {
				mkdir("../files/".$nome, 0777, true);
			}
			// Guarda a informação da data e hora
			 $date = str_replace("-","/",$_POST["data"]).";".$_POST["hora"];
			 // Guarda num ficheiro o valor procesado
			 echo file_put_contents("../files/".$nome."/valor.txt",$_POST["valor"]);
			 // Guarda num ficheiro a data procesada
			 echo file_put_contents("../files/".$nome."/hora.txt", $date);
			 // Guarda um novo log no ficheiro 
			 echo file_put_contents("../files/".$nome."/log.txt", "\n".$date.";".$_POST["valor"],FILE_APPEND);
		 } else {
			 // Caso faltar informação para poder procesar, irá mostrar uma mensagem au utilizador
			 echo "<br<Falta de dados.<br>Local save cancelada.";
			 echo "<br>Campu Nome: ". $_POST["nome"];
			 echo "<br>Campu Valor: ". $_POST["valor"];
			 echo "<br>Campu Data: ". $_POST["data"];
			 echo "<br>Campu Hora: ". $_POST["hora"];
		 }
	// Caso for um GET, verifica que tem a informação necesaria
	} else if ($type == "GET" && isset($_GET["nome"], $_GET["type"])) {
		// Vai verificar se existe o ficheiro dos dados a serem pedidos
		if (file_exists("../files/".$_GET["nome"])) {
			// Vai returnar o ficheiro a ser pedido
			echo file_get_contents("../files/".$_GET["nome"]."/".$_GET["type"].".txt");
		// Caso não encontrar o ficheiro
		} else {
			throw new Exception("Diretoria não encontrada");
		}
	// Caso o Request for um tipo não utilizado
	} else {
		throw new Exception("Metodo não permitido");
	}
	exit();
 ?>