<template>
    <section id="hero">
    <div class="principal">
    <img id="logo" alt="LlevamePe logo" src="../assets/adoptme.jpeg" height="400">
    </div>
    <div id = "welcome">
      <h3>¡Bienvenidos a <strong>LlevamePe!</strong></h3>
      <h1>Somos una organización de ayuda a perros y gatos, facilitando la adopción, donación y ejecución de voluntariados.</h1>
      <h2>Somos un equipo de estudiantes de UTEC comprometidos con los animales.</h2>
    </div>
  </section>
  <section id = "animales">
    <h4>¡Últimos animales <strong>adoptados!</strong></h4>
    <body>
    <div class="container">
        <img src="i../assets/gato1.jpeg" class="image" style="width:100%">
        <div class="middle">
            <div class="text">Chino</div>
        </div>
    </div>
    <div class="container">
        <img src="i../assets/gato2.jpeg" class="image" style="width:100%">
        <div class="middle">
            <div class="text">Meche</div>
    </div>
    </div>
    </body>
  </section>
  <section id = "donadores">
    <h4>¡Nuestro más fieles <strong>donadores!</strong></h4>
    <body>
    <div class="container">
        <img src="i../assets/harold.jpeg" class="image" style="width:100%">
        <div class="middle">
            <div class="text">Harold Colchado</div>
        </div>
    </div>
    <div class="container">
        <img src="i../assets/marvinskynaruto.png" class="image" style="width:100%">
        <div class="middle">
            <div class="text">Marvinsky</div>
    </div>
    </div>
    </body>
  </section>
</template>

<style>
    section {
    background-color: #000000;
    }
    section .body {
        display:table-row;
    }
    h3 {
        font-family: 'Asap', sans-serif;
        color: #f8f9ff;
        font-size: 50px;
        margin-top: 20px;
    }
    h1,h2 {
        font-family: "Courier New", monospace;
        color: #f8f9ff;
        font-size: 24px;
        margin-top: 20px;
    }
    h4 {
        font-family: 'Asap', sans-serif;
        color: #f8f9ff;
        font-size: 40px;
        margin-top: 20px;
    }
    #logo {
    border-radius: 100px;
    border-spacing: 200px;
    cursor: pointer;
    transition: 0.3s;
    margin-top: 100px;
    }

    #logo:hover {opacity: 0.7;}

    /* The Modal (background) */
    .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
    }

    #welcome {
    background-image: none;
    margin-top: 100px;
    }
    .container {
    position: relative;
    width: 30%;
    }

    .image {
    opacity: 1;
    display: block;
    width: 100%;
    height: auto;
    transition: .5s ease;
    backface-visibility: hidden;
    }

    .middle {
    transition: .5s ease;
    opacity: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%)
    }

    .container:hover .image {
    opacity: 0.3;
    }

    .container:hover .middle {
    opacity: 1;
    }

    .text {
    background-color: #ff0000;
    color: white;
    font-size: 16px;
    padding: 16px 32px;
    }

    #animales {
        margin-top: 100px;
    }
</style>