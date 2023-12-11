var myChart=echarts.init(document.getElementById('m1'));
var option={
    title:{
    text:'ECharts 入门案例'
    },
    tooltip:{},
    legend:{
    data:['销量']
    },
    xAxis:{
    data:['衬衫','羊毛衫','袜子','高根结','蝴蝶结']
    },
    yAxis:{},
    series:[
        {
        name:'销量',
        type:'bar',
        data:[5,20,36,10,25]
        }
    ]
};
myChart.setOption(option);

$.ajax({
    url: '/polls/get_data/',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
       console.log('AJAX yes yes : ');
  var chartData = [];
  for (var i = 0; i < data.length; i++) {
    var name = data[i].goodsA + ' ' + data[i].goodsB;
    var value = [data[i].goods1, data[i].goods2];
    chartData.push({
      name: name,
      type: 'bar',
      data: value
    });
  }
        var chart = echarts.init(document.getElementById('m2'));
    chart.setOption({
         xAxis: {
            type: 'category',
            data: ['goodsA', 'goodsB']
            },
            yAxis: {
      type: 'value'},
    series: chartData
        });
    },
    error: function(xhr, status, error) {
        console.log('AJAX request failed: ');
    }
});