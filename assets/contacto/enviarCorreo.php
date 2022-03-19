<?php
session_start();
if(isset($_POST['url']) && $_POST['url'] == '' && isset($_POST['url2']) && $_POST['url2'] == "antispam")
{
    if(!($_POST["message"] == "" || $_POST["name"] == "" || $_POST["email"] == "")){
      $to = 'adlopez@itesm.mx'; // Replace with your email 
  
      $subject = 'Contacto desde el sitio de Conexion Tec'; // Replace with your $subject
      $headers = 'From: ' . $_POST['email'] . "\r\n" . 'Reply-To: ' . $_POST['email'];    

      $message = "Contacto desde el sitio de Conexion Tec" . "\n" .
                 'Nombre: ' . $_POST['name'] . "\n" .
                 'Correo: ' . $_POST['email'] . "\n" .
                 'Mensaje: ' . $_POST['message'];
      
      mail($to, $subject, $message, $headers);   
    }
     

}
?>