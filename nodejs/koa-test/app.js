const Koa = require('koa');
const app = new Koa();
const { Pool } = require('pg')
const cors = require('koa2-cors');
const bodyParser = require('koa-bodyparser');

app.use(cors());
app.use(bodyParser());

const pool = new Pool({
  user: 'z',
  host: '127.0.0.1',
  database: 'test',
  password: 'z',
  port: 5432,
});

app.context.dbpool = pool;

// app.use(async ctx => {
//   ctx.body = 'Hello World';
//   const client = await ctx.dbpool.connect();
//   try {
//     const res = await client.query('SELECT now() as now');
//     ctx.body += res.rows[0].now;
//   } finally {
//   client.release();
//   }
// });

app.use(async ctx => {
  // ctx.set("Access-Control-Allow-Origin", "*");
  ctx.body = 'Hello World';
  // console.log('ID: ' + ctx.query.id);
  // console.log('温度: ' + ctx.query.temp);
  // console.log('时间戳： ' + ctx.query.datetime);
  const client = await ctx.dbpool.connect();
  try {
    const res = await client.query('insert into sensor(sensor_id, data, gen_time) values(' + ctx.query.id + ', ' + ctx.query.temp + ', to_timestamp(' + ctx.query.datetime + ' / 1000.0));');
    // ctx.body += res.rows[0].now;
  } finally {
    client.release();
  }
});

app.listen(8080);