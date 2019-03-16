var path = require('path');
var express = require('express');
var app = express();

app.get('/', function(req, res){
	res.sendFile(path.join(__dirname, '.', './index.html'));
});

app.post('/',function(req, res){
	res.send('have some patience. haven\'t written the post handler yet');
});

var server = app.listen(3500, function(){
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at port "+port+" in the host "+host);
});
