var dom = document.getElementById('chart-container');
var myChart = echarts.init(dom, 'dark');

var option = {
  visualMap: {
    show: false,
    min: 2,
    max: 6,
    inRange: {
      color: [
        '#313695',
      ]
    }
  },
  xAxis3D: {
    type: 'value'
  },
  yAxis3D: {
    type: 'value'
  },
  zAxis3D: {
    type: 'value',
    max: 200,
    min: 0
  },
  grid3D: {
    axisLine: {
      lineStyle: { color: '#fff' }
    },
    axisPointer: {
      lineStyle: { color: '#fff' }
    },
    viewControl: {
      // autoRotate: true
    },
    light: {
      main: {
        shadow: true,
        quality: 'ultra',
        intensity: 1.5
      }
    }
  },
  series: [
    {
      type: 'bar3D',
      shading: 'lambert',
      label: {
        formatter: function (param) {
          return param.value[2].toFixed(1);
        }
      }
    }
  ]
};

myChart.setOption(option);

var websocket = new WebSocket('ws://localhost:3000'); // 请根据实际情况更改 WebSocket 的地址
websocket.onmessage = function (event) {
  var message = event.data;
  console.log('接收到消息:', message); // 打印接收到的消息内容
  // 处理接收的消息
  if (message === 'WebSocket 连接已建立') {
    console.log('WebSocket 连接已建立');
  } else {
    try {
      var data = JSON.parse(message);
      myChart.setOption({
        series: [{
          data: data
        }]
      });
    } catch (error) {
      console.error('解析消息时发生错误:', error);
    }
  }
};



// 断开 WebSocket 连接成功触发事件
websocket.onclose = function() {
  console.log('WebSocket connection closed.');
};

// 关闭 WebSocket 连接
function closeWebSocket() {
  websocket.close();
}
