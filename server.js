var path = require('path');
var express = require('express');
var app = express();
const cors = require('cors');
app.use(cors({ "https://bhargavhegde.com/utils.html": true,
		"http://192.168.0.21:8081/utils.html": true}));


app.get('/', function(req, res){
	console.log("request incoming . . .");
	res.sendFile(path.join(__dirname, '.', './index.html'));
});

app.post('/',function(req, res){
	console.log("request incoming");
	res.send('have some patience. haven\'t written the post handler yet');
});

var server = app.listen(8080, function(){
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at port "+port+" in the host "+host);
});
