
var http = require('http');

function randomFrom(lowerValue, upperValue) {
    return Math.floor(Math.random() * (upperValue - lowerValue + 1) + lowerValue);
}

// 用于请求的选项
var options = {
    host: 'localhost',
    port: '8080',
    path: '/index.html'
};

// 处理响应的回调函数
var callback = function (response) {
    // 不断更新数据
    var body = '';
    response.on('data', function (data) {
        body += data;
    });

    response.on('end', function () {
        // 数据接收完成
        console.log(body);
    });
}

// 设置请求参数
var id = randomFrom(0, 9);
var data = randomFrom(330, 349) / 10;
options.path = '/send?id=' + id + '&data=' + data;

// 向服务端发送请求
var req = http.request(options, callback);
req.end();
