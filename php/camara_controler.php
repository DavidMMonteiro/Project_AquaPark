<?php
	$default_txt = "No data";
	$update_date = file_get_contents("../../files/img/hora.txt");
?>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="15">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
	</head>
	<body>
		<h1>Camara em AquaPark</h1>
        <div><a href="../../index.html" >Página inicial</a></div>
		<div>
            <p>
                <?php echo "Ultima atualização: " . $update_date ?>
            </p>
            <?php
                echo "<img src='../../files/img/camara.png?id=".time()."' style='width: 250px;'>"
            ?>
        </div>
	</body>
</html>
