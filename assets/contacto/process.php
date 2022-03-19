<?php
session_start();
if( isset($_POST['name']) && strtoupper($_POST['captcha']) == $_SESSION['captcha_id'] )
{
	$to = 'concurso.mty@itesm.mx'; // Replace with your email	
	$subject = 'Contacto desde el sitio del Concurso de Ciencias'; // Replace with your $subject
	$headers = 'From: ' . $_POST['email'] . "\r\n" . 'Reply-To: ' . $_POST['email'];	
	
	if($_POST['telefono'] == '') $_POST['telefono'] = 'No disponible';

	$message = "Contacto desde el sitio del Concurso de Ciencias" . "\n" .
			   'Nombre: ' . $_POST['name'] . "\n" .
	           'Correo: ' . $_POST['email'] . "\n" .
	           'Teléfono: ' . $_POST['telefono'] . "\n" .
	           'Mensaje: ' . $_POST['message'];
	
	mail($to, $subject, $message, $headers);	
	if( $_POST['copy'] == 'on' )
	{
		mail($_POST['email'], $subject, $message, $headers);
	}

}
?>