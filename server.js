var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function(request, response) {
	var currentURL = url.parse(request.url, true);

	if(currentURL.pathname == '/analyse' || currentURL.pathname == '/analyse/'){
		if(!currentURL.query.username){
			fs.readFile('./analyse_user.html', function(err, data) {
				if (err) throw err;
				response.writeHead(200, {'Content-Type': 'text/html'});
				response.write(data);
				response.end();
			  });
		}
		else{
			const spawn = require("child_process").spawn;
			const pythonProcess = spawn('python',["./tweets_fetch.py",currentURL.query.username]);
			response.writeHeader(200);
			pythonProcess.stdout.on('data', (data) => {
				console.log(data.toString());
				response.write(data);
				response.end();
			});
		}
	}
	else if(currentURL.pathname == '/dd' || currentURL.pathname == '/dd/'){
		if(!currentURL.query.text){
			fs.readFile('./dd.html', function(err, data) {
				if (err) throw err;
				response.writeHead(200, {'Content-Type': 'text/html'});
				response.write(data);
				response.end();
			  });
		}
		else{
			const spawn = require("child_process").spawn;
			const pythonProcess = spawn('python',["./webVersionDD.py",currentURL.query.text]);
			pythonProcess.stdout.on('data', (data) => {
				console.log(data.toString());
				response.writeHeader(200);
				response.write(data);
				response.end();
			});	
		}
	}
	else{
		fs.readFile('./homepage.html', function(err, data) {
			if (err) throw err;
			response.writeHead(200, {'Content-Type': 'text/html'});
			response.write(data);
			response.end();
		  });
	}
	
}).listen(8080);