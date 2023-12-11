
 // 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));
myChart.resize({ width: '800px', height: '400px' });

// 指定图表的配置项和数据
var option = {
    title: {
        text: '股票数据'
    },
    tooltip: {},
    legend: {
        data:['mkv', 'amount', 'stk_mkv_ratio']
    },
    xAxis: {
        data: []
    },
    yAxis: {},
    series: [
        {
            name: 'mkv',
            type: 'bar',
            data: []
        },
        {
            name: 'amount',
            type: 'bar',
            data: []
        },
        {
            name: 'stk_mkv_ratio',
            type: 'bar',
            data: []
        }
    ]
};
fetch('/polls/code_data/')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      const tsCodeSelect = document.getElementById('ts_code');
      // 遍历 data 对象的属性
      for (let i = 1; i <= 10; i++) {
        const codeContent = data[`code${i}Content`];
        // 如果属性存在，则创建对应的选项并添加到 select 元素中
        if (codeContent) {
          const codeOption = document.createElement('option');
          codeOption.value = codeContent;
          codeOption.innerText = codeContent;
          tsCodeSelect.appendChild(codeOption);
        }
      }
    });
$('#search-form').submit(function(event) {
    event.preventDefault(); // 阻止默认提交行为
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
var ts_code = $('#ts_code').val();
var start_date = $('#start_date').val();
var end_date = $('#end_date').val();
console.log(ts_code, start_date, end_date); // 打印表单参数

// 通过ajax获取数据
$.ajax({
    url: '/polls/stock_data/',
    data: {
        'ts_code': ts_code,
        'start_date': start_date,
        'end_date': end_date
    },
    success: function(data) {
        console.log(document.getElementById('chart'));
        console.log(responseData);
        var data = JSON.parse(responseData);
        var xData = data.map(function(item) {
            return item.ann_date;
        });
        var mkvData = data.map(function(item) {
            return item.mkv;
        });
        var amountData = data.map(function(item) {
            return item.amount;
        });
        var stkMkvRatioData = data.map(function(item) {
            return item.stk_mkv_ratio;
        });
            for (var i = 0; i < data.length; i++) {
                xData.push(data[i].ann_date);
                mkvData.push(data[i].mkv);
                amountData.push(data[i].amount);
                stkMkvRatioData.push(data[i].stk_mkv_ratio);
            }
            myChart.setOption({
                xAxis: {
                    data: xData
                },
                series: [
                    {
                        name: 'mkv',
                        data: mkvData
                    },
                    {
                        name: 'amount',
                        data: amountData
                    },
                    {
                        name: 'stk_mkv_ratio',
                        data: stkMkvRatioData
                    }
                ]
            });
        }
});
});