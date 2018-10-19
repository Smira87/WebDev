const http = require('http');
var fs = require('fs');
var express = require('express');
var path = require('path');

var app = express();

app.use(express.static(__dirname + '/public'));
http.createServer(function(req, res) {
    if (req.url === "/"){
        fs.readFile("index.html", "UTF-8", function(err,html){
            res.writeHead(200, {"Condtent-Type": "text/html"});
            res.end(html);
        
        });
          }else if(req.url.match("\.css$")){
              var cssPath = path.join(__dirname, 'public', req.url);
              var fileStream = fs.createReadStream(cssPath, "UTF-8");
              res.writeHead(200, {"Contebt-Type": "text/css"});
              fileStream.pipe(res);
          }else if(req.url.match("\.jpeg$")){
            var imagePath = path.join(__dirname, 'public', req.url);
            var fileStream = fs.createReadStream(imagePath);
            res.writeHead(200, {"Contebt-Type": "image/jpeg"});
            fileStream.pipe(res);
          }

}).listen(3000);

