const Koa = require('koa');
const app = new Koa();
// const { Pool } = require('pg')
const cors = require('koa2-cors');

app.use(cors());

// const pool = new Pool({
//     user: 'postgres',
//     host: '127.0.0.1',
//     database: 'postgres',
//     password: 'postgres',
//     port: 5432,
// });

// app.context.dbpool = pool;

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
  // const client = await ctx.dbpool.connect();
  // try {
  //   const res = await client.query('SELECT now() as now');
  //   ctx.body += res.rows[0].now;
  // } finally {
  //   client.release();
  // }
});

app.listen(8080);