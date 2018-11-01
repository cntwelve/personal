const router = require('koa-router')()

router.prefix('/api')

router.get('/currentUser', async (ctx, next) => {
  ctx.body = {
    name: 'Serati Ma',
    avatar: '/images/icon-ma.png',
    userid: '00000001',
    email: 'antdesign@alipay.com',
    signature: '海纳百川，有容乃大',
    title: '监控专家',
    group: '技术部',
    tags: [
      {
        key: '0',
        label: '很有想法的',
      },
      {
        key: '1',
        label: '专注设计',
      },
      {
        key: '2',
        label: '辣~',
      },
      {
        key: '3',
        label: '大长腿',
      },
      {
        key: '4',
        label: '川妹子',
      },
      {
        key: '5',
        label: '海纳百川',
      },
    ],
    notifyCount: 12,
    country: 'China',
    geographic: {
      province: {
        label: '北京市',
        key: '330000',
      },
      city: {
        label: '北京市',
        key: '330100',
      },
    },
    address: '北京市前门大街1号',
    phone: '010-888888888',
  }
})

module.exports = router
