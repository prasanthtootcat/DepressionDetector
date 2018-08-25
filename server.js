var http = require('http');
var url = require('url');

http.createServer(function(request, response) {
	var queryData = url.parse(request.url, true).query;
	const spawn = require("child_process").spawn;
	const pythonProcess = spawn('python',["./webVersionDD.py",queryData.text]);
	pythonProcess.stdout.on('data', (data) => {
        response.writeHeader(200);
        response.write(data);
        response.end();
	});
}).listen(8080);