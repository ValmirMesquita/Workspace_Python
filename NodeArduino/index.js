var http =  require('http');
var express = require('express');
var app = express();
var server = http.createServer(app);

// Cria uma rota para a raiz da aplicação 
app.get('/', function(reg, res){
    res.render(index.ejs);
})
// Cria uma 2ª rota (/about) para a raiz da aplicação
app.get('/about', function(reg, res){
    res.send("Isso é sobre a página");
})

// Adiciona uma engenharia de tamplet
app.set('view engine', 'ejs');
var title = "Some Arduino componentes Starting With p"
var componentArray = ['potentiometer', 'piezo', 'phototransistor','pushbutton'];

app.get('/', function(reg, res){
    res.render('index',{
        title: title, 
        Components:componentArray
    });
});

// Fica monitorando a porta 3000
server.listen(3000, function() {
    console.log('Ouvindo no por 3000...')
}
);