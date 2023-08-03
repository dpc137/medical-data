const Redis = require('ioredis');

const client = new Redis({
  host: '127.0.0.1', // Redis服务器的IP地址
  port: 6379, // Redis服务器的端口
});

client.on('connect', () => {
  console.log('Redis连接成功');
});

client.on('error', (err) => {
  console.error('Redis连接错误:', err);
});
