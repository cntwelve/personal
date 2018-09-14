
var http = require('http');
var url = require('url');
var querystring = require('querystring')
const { Pool, Client } = require('pg')

var sqlStr;

const client = new Client({
    user: 'postgres',
    host: '127.0.0.1',
    database: 'postgres',
    password: 'postgres',
    port: 5432,
});

// var queryExcute = async function () {
//     await  client.connect();
//     let sqlStr = await client.query('SELECT NOW() as now');
//     await client.end();
//     console.log(sqlStr.rows[0].now);
//     return sqlStr.rows[0].now;
// };

// 创建服务器
http.createServer(function (request, response) {
    var pathname = url.parse(request.url);
    var query = querystring.parse(pathname.query);

    // HTTP 状态码: 200 : OK
    // Content Type: text/plain
    response.writeHead(200, { 'Content-Type': 'text/html' });

    var dateStr = (new Date()).toLocaleString();

    // 执行PG数据库查询

    console.log('Start query.....');

    // sqlStr = client.query('SELECT NOW() as now', function (err, result) {
    //     if (err) {
    //         return console.error('error running query', err);
    //     }
    //     console.log(result.rows[0].now);
    //     // sqlStr = result.rows[0].now;
    //     client.end();
    //     return result.rows[0].now;
    // });

    // let sqlStr = queryExcute();
    (async () => {
        console.log('starting async query')
        const res = await client.query('SELECT NOW() as now')
        console.log('async query finished')
        sqlStr = res.row[0].now
      })();
              //     await  client.connect();
        //     let sqlStr = await client.query('SELECT NOW() as now');
        //     await client.end();
        //     console.log(sqlStr.rows[0].now);
        //     return sqlStr.rows[0].now;
        // };

    var respStr = request.url + '\n' + dateStr + '\n' + query['id'] + '\n' + query['data'] + '\n' + sqlStr;

    response.write(respStr);
    //  发送响应数据
    response.end();
}).listen(8080);

// 控制台会输出以下信息
console.log('Server running at http://127.0.0.1:8080/');
