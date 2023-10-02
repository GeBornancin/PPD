// Importa as bibliotecas necessárias
var express = require('express'),

    app = express(),
    server = require('http').createServer(app).listen(4555), // Cria um servidor HTTP e o faz escutar na porta 4555
    io = require('socket.io').listen(server), // Cria uma instância do Socket.io e a conecta ao servidor
    bodyParser = require('body-parser'); // Biblioteca para análise do corpo das requisições


// Configura o uso do bodyParser para analisar os corpos das requisições
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

var port = process.env.PORT || 8080; // Define a porta padrão como 8080 caso não seja fornecida via variável de ambiente
var router = express.Router(); // Criação do roteador

// Middleware para emitir notificações via Socket.io
var emitir = function (req, res, next) {
    var notificar = req.query.notificacao || '';
    if (notificar != '') {
        io.emit('notificacao', notificar); // Emite uma notificação via Socket.io
        next(); // Passa para o próximo middleware
    } else {
        next(); // Passa para o próximo middleware
    }
}

app.use(emitir); // Utiliza o middleware de emissão de notificações
app.use('/api', router); // Define a rota base '/api' para o roteador

// Rota para receber notificações
router.route('/notificar')
    .get(function (req, res) {
        // Responde com uma mensagem JSON
        res.json({
            message: "testando essa rota"
        });
    });

// Inicia o servidor na porta definida
app.listen(port);
console.log('Conectado à porta ' + port);