<template>
    <section id="home">
        <img id="logo" alt="LlevamePe" src="../assets/adopt_me.jpeg" height="700">
        <div id="welcome">
            <div class="container">
                <br>
                <h2>¡Bienvenid@ a <strong>LlevamePe!</strong></h2>
            <h3>Somos una organización de ayuda a perros y gatos, facilitando la adopción, donación y ejecución de voluntariados.</h3>
            <br>
                <br>
            </div>
        </div>
  <section id="animales">
    <br><br>
    <h4>¡Últimos animales <strong>adoptados y sus dueños!</strong></h4><br>

    <div class="row">
        <div class="column">
            <img src="../assets/gato1.jpeg" style="width:100%">
            <div class="text">Chino</div>
        </div>
        <div class="column">
            <img src="../assets/harold_pic.jpg" style="width:100%">
            <div class="text">Harold</div>
        </div>
        <div class="column">
            <img src="../assets/gato2.jpeg" style="width:100%">
            <div class="text">Meche</div>
        </div>
        <div class="column">
            <img src="../assets/marvinskynaruto.jpeg" style="width:100%">
            <div class="text">Marvin</div>
          </div>
      </div>
  </section>
</section>
</template>

<style>
    #home section{
    background-color: #758395;
    }
    
    #logo {
    border-radius: 50px;
    border-spacing: 100px;
    cursor: pointer;
    transition: 0.3s;
    }

    #logo:hover {opacity: 0.7;}

    /* The Modal (background) */
    #home .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
    }

    #animales h4 {
        color: white
    }

    #welcome {
    background-image: none;
    }

    .image {
    opacity: 1;
    display: block;
    width: 50%;
    height: auto;
    transition: .5s ease;
    backface-visibility: hidden;
    }

    #home .middle {
    transition: .5s ease;
    opacity: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%)
    }

    .container:hover .image {
    opacity: 0.7;
    }

    .container:hover .middle {
    opacity: 1;
    }

    #home .text {
    background-color: #45445b;
    color: white;
    font-size: 16px;
    padding: 16px 32px;
    }

    #animales .column {
        float: left;
        width: 25%;
        padding: 5px;
      }
      
    #animales .row::after {
        content: "";
        clear: both;
        display: table;
    }
</style>