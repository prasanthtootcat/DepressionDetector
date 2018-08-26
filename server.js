var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function(request, response) {
	var q = url.parse(request.url, true);
	if(!q.query.text){
		fs.readFile('./index.html', function(err, data) {
			if (err) throw err;
    		response.writeHead(200, {'Content-Type': 'text/html'});
    		response.write(data);
    		response.end();
  		});
	}
	else{
		const spawn = require("child_process").spawn;
		const pythonProcess = spawn('python',["./webVersionDD.py",q.query.text]);
		pythonProcess.stdout.on('data', (data) => {
        	response.writeHeader(200);
        	response.write(data);
        	response.end();
		});	
	}
	
}).listen(process.env.PORT);