<?php 
include 'include/navbar.php'; 
require("html/db_config.php");
session_start();

if (!isset($_SESSION["email"])) {
echo('
<html>


<div id="carouselExampleIndicators w-75" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active ">
      <img src="img/img-slide/img-1.jpg" class="d-block mx-auto w-75"  height="500" >
    </div>
    <div class="carousel-item">
      <img src="img/img-slide/img-2.jpg" class="d-block mx-auto w-75"  height="500">
    </div>
    <div class="carousel-item ">
      <img src="img/img-slide/img-3.jpg" class="d-block mx-auto w-75"  height="500">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>


<div class="container mt-5">
<div class="row justify-content-center">
<div class="col-6 ml-3">
  <h1 id="title" class="ml-5 mr-2 p-3 ms-4 display-1 text-light bg-dark ">INNOVA MUSIC</h1>
</div>
</div>
</div>

<div class="row">
  <div class="text-light text-center">Servicios de mantención y registros de TÚ música. También puedes visualizar el material de tu futuro colaborador o competencia </div>
</div> 

</body>
</html>');}


else{
  $sql_statement = "SELECT suscripcion_activa,nombre FROM personas WHERE email = $1;";
  $result = pg_query_params($dbconn, $sql_statement, array($_SESSION["email"]));

  $row = pg_fetch_row($result);
  $Tipo_persona = $row[0];
  if($Tipo_persona==null){echo("<div class='position-absolute top-50 start-50 translate-middle  btn bg-secondary bg-gradient'>
    <h1>Bienvenido $row[1]</h1> <h5>¿Que deseas hacer?</h5><form action='html/crud_canciones.php'>
      <button class='btn-danger' type='submit'>Modificar canciones</button>
  </form>
  <form action='html/crud_albumes.php'>
      <button class='btn-danger' type='submit'>Modificar Album</button>
  </form>
  </div>"
);}
  else {
      echo('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand btn btn-outline-success  text-success" href="html/informacion_usuario.php">Información Perfil</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="html/lista_canciones.php">Lista de Canciones</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">INNOVA</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <a class="link-dark" href="../html/UsuarioCantante.php" >Vuelvete Cantante</a>
    ');

  }
}

?>