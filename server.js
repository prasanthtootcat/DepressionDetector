var http = require('http');
var url = require('url');
var fs = require('fs');
var csv = require('fast-csv');

http.createServer(function(request, response) {
	var q = url.parse(request.url, true);
	var suicidalDataLoad = new Promise(function(resolve, reject) {
		var s = []
		fs.createReadStream('./suicidalWords.csv')
		.pipe(csv())
		.on('data',function(data){
			s.push(data[0]);
		})
		.on('end',function(data){
			resolve(s);
		})
	});

	if(!q.query.text){
		fs.readFile('./index.html', function(err, data) {
			if (err) throw err;
    		response.writeHead(200, {'Content-Type': 'text/html'});
    		response.write(data);
    		response.end();
  		});
	}
	else{

		suicidalDataLoad.then(function(data){
			for(var i=0; i<data.length; i++){
				 if(data[i] == q.query.text){
					response.writeHeader(200);
					response.write('Extreme depression');
					console.log('Extreme Depression');
					response.end();
					return(1);
				 }
			}
			return 0;
		}).then(function(data){
			if(data == 0){
				const spawn = require("child_process").spawn;
				const pythonProcess = spawn('python',["./webVersionDD.py",q.query.text]);
				pythonProcess.stdout.on('data', (data) => {
					console.log(data.toString());
					response.writeHeader(200);
					response.write(data);
					response.end();
				});	
			}
		})
	}
	
}).listen(8080);