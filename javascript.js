// fazer apenas um nivel com um botao "jogar de novo"
// ou fazer varios niveis (5-6) que aumentem a dificuldade com o tempo
// e fique trocando os background para dar uma impressao de avanço
// nessa troca de background posso ir fazendo os muros deixarem de serem
// urbanos para serem floresta
// na lista de rankings deixar o usuario falar quantos ele quer ver
// tentar deixar tudo responsivo
// mas assim, só tentar mesmo
// se eu quiser um labirinto horizontal é só eu mudar as regras
// Vou fazer o labirinto horizontal se tiver saco porque vou ter que criar regras
// pro movimento pra cima
// tela de inicio
// tela de jogo ganho
// tela de game over
// talvez tela de ranking
// O ranking pode ser feito com apenas tres letras indentificando o jogador
// tipo arcade antigo
// criar funcao para substituir os anterior_moves
/*   */

$(document).ready(() => {
   setTimeout(function() {
     terminaLore();
   }, 32000);


  $("#topo").css("height", (window.innerHeight / 6) + "px");
  $("#tela").css("height", (window.innerHeight / 1.5) + "px");
  var nivel = 50;

  $("#tela").load("nivelSelect.jsp");


});

function setLabirinto(nivel){
  $("#tela").addClass("background-game");
  $("#tela").empty();
  $("#tela").append("<div id=\"caminho\"></div>");
  inicia(nivel);

  setLabRoad(nivel);
  // reseta o delay para caso o jogador jogue varios jogos sem atualizar a pagina
  delay = 1500;

  var alturaTela = $("#tela").css("height");
  alturaTela = alturaTela.split("px")[0];
  alturaTela = parseInt(alturaTela);

  $("#caminho > div:last-child").removeClass("muro");
  $("#caminho > div:last-child").css("background-color", "red");
  $("#caminho > div:last-child").addClass("vencer");
  $(".vencer").css("border-color", "red");
  var vertical = getVertical();
  $("#caminho > div:last-child").css("height", alturaTela - vertical + "px");
  setLoseAndWin(nivel);
}

function inicia(nivel){
  var horizontal = Math.floor((Math.random() * 15) + 1);
  horizontal *= 50;
  $("#caminho").append("<div id=\"inicio\" style=\" background-color: green !important; position: absolute; left: 0px; top: 0px; height:" + nivel + "px; width: " + nivel + "px;\"></div>");
  $("#caminho > div:last-child").animate({left: horizontal + "px"}, 1500);
  $("#caminho > div:last-child").css("left", horizontal + "px");
}

var delay = 1500;
function move(direcao, nivel){
  var vertical = getVertical();
  var horizontal = getHorizontal();
  if(direcao == "baixo"){
    vertical += nivel;
  }else if (direcao == "esquerda"){
    horizontal -= nivel;
  }else if (direcao == "direita"){
    horizontal += nivel;
  }

  $("#caminho").append("<div class=\"muro\" style=\"position: absolute; top:" + vertical + "px; left: 0px; height:" + nivel + "px; width: " + nivel + "px;\"></div>");
  $("#caminho > div:last-child").animate({left: horizontal + "px"}, delay);
  $("#caminho > div:last-child").css("left", horizontal + "px");
  delay += nivel * 2;
}

function getHorizontal(){
  var horizontal = $("#caminho > div:last-child").css("left");
  horizontal = horizontal.split("px")[0];
  horizontal = parseInt(horizontal);
  return horizontal;
}

function getVertical(){
  var vertical = $("#caminho > div:last-child").css("top");
  vertical = vertical.split("px")[0];
  vertical = parseInt(vertical);
  return vertical;
}

function calcPontos(tempoInicial) {
  var muros = $("#caminho > div").length
  var tempoFinal = new Date().getTime()
  var tempo = tempoFinal - tempoInicial
  var pontuacao = 50000 - Math.floor((tempo / muros) * 42);
  return pontuacao;
}

function setLoseAndWin(nivel) {
  var str_nivel = "";
  if(nivel == 50){
    str_nivel = "facil";
  }else if (nivel == 25){
    str_nivel = "medio";
  }else if (nivel == 13){
    str_nivel = "dificil";
  }

  $("#inicio").mouseenter(function() {
    var tempoInicial = new Date().getTime();
    $("#caminho").mouseleave(function() {
      $("#tela").removeClass("background-game");
      $("#tela").empty();
      $("#tela").load("gameOver.jsp");
    });
    $(".vencer").mouseover(function() {
      $("#tela").removeClass("background-game");
      var pontuacao = calcPontos(tempoInicial);

      $("#tela").empty();
      $("#tela").load("winGame.jsp", {
        nivel: str_nivel,
        pontuacao: pontuacao
      });
    })
  })
}

function setLabRoad(nivel) {
  var vertical = getVertical();
  var horizontal = getHorizontal();
  var rand = 0;
  var anterior_move1 = 0;
  var anterior_move2 = 0;
  var descidas;
  var verticalMax = nivel == 13 ? 450 : 440;

  while(vertical <= verticalMax){
    rand = Math.floor(Math.random() * 3 + 1);

    if(rand == 1){
      if(canMoveLeft(anterior_move1, anterior_move2, horizontal)){
        descidas = 0;
        move("esquerda", nivel);
        anterior_move2 = anterior_move1;
        anterior_move1 = rand;
      }
    }else if(rand == 2){
      if(canMoveDown(descidas)){
        move("baixo", nivel);
        descidas += 1;
        anterior_move2 = anterior_move1;
        anterior_move1 = rand;
      }
    }else if (rand == 3){
      if(canMoveRight(anterior_move1, anterior_move2, horizontal)){
        descidas = 0;
        move("direita", nivel);
        anterior_move2 = anterior_move1;
        anterior_move1 = rand;
      }
    }
    vertical = getVertical();
    horizontal = getHorizontal();
    anterior_move(1);
  }
}

function canMoveLeft(anterior_move1, anterior_move2, horizontal) {
  return (anterior_move1 != 3 && horizontal > 0 && anterior_move2 != 3);
}

function canMoveDown(descidas) {
  return (descidas <= 2);
}

function canMoveRight(anterior_move1, anterior_move2, horizontal) {
  return (anterior_move1 != 1 && horizontal < 750 && anterior_move2 != 1);
}

function anterior_move(past_move) {
  var teste = $("#caminho > div:nth-last-child(" + past_move + ")");
  // console.log(teste);
}

function terminaLore(){
  $("#lore").animate({"opacity" : "0"}, 2000);
  setTimeout(function() {
    $("#lore").attr('hidden', 'true');
    $("#topo").removeAttr('hidden');
    $("#jogo-conteudo").removeAttr('hidden');
  }, 2000);
}


var objeto = {
  "nome": "carro",
  "rodas" : 4
}

var funcao = function() {
  console.log("something");
}

var objetoDentroObjeto = {
  url: "someSite.jsp",
  data: {
    nome: "someone",
    objeto1: {
      nome: "something"
    },
    objeto2 : {
      nome: "something2"
    }
  }
}