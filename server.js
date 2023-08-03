const express = require('express');
const Redis = require('ioredis');
const WebSocket = require('ws');

const app = express();
const port = 3000;



//连接redis
const client = new Redis({
  host: '127.0.0.1', 
  port: 6379, 
});
client.on('connect', function(){
  console.log('Redis连接成功');
});
client.on('error', function(err){
  console.error('Redis连接错误:', err);
});



//创建静态文件目录
app.use(express.static('public'));
//创建服务器并且指定监听端口
const server = app.listen(port, () => {
  console.log(`服务器正在运行，访问地址：http://localhost:${port}`);
});



// 创建 WebSocket 服务器
const wss = new WebSocket.Server({ server }); 
// WebSocket 连接建立后，可以向客户端发送消息
wss.on('connection', (ws) => {
  // 取消订阅 Redis 的数据更新事件
  ws.on('close', () => {
    client.unsubscribe('latest_data');
    console.log('客户端和服务端的连接未建立');
  });
  ws.send('WebSocket 连接已建立');
  console.log('客户端和服务端的连接已经建立');
  ws.on('error', (error) => {
    console.error('WebSocket发生错误:', error);
  });
});



// 每当 Redis 有数据更新时，将最新的数据发送给所有连接的客户端
client.on('message', (channel, message) => {
  if (channel === 'latest_data') {
    console.log('有新数据');
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
        console.log('传输新的数据');
      }
    });
  }
});

// ws订阅redis
client.subscribe('latest_data');
console.log('Redis订阅已完成：latest_data');
//确保成功连接到Redis
client.on('connect', function(){
  console.log('Redis连接成功');
});




