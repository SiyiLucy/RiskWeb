$(document).ready(function() {
    $.ajax({
        url: '/polls/code_data2/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // 清空表格内容
            $('#codeTableBody').empty();
            var count = 0; // 计数变量
            // 遍历code content
            $.each(data, function(key, value) {
                if (value !== null && value !== '') {
                    count += 1; // 增加计数
                    var row = $('<tr></tr>');
                    var cell = $('<td></td>').text(value);
                    row.append(cell);
                    $('#codeTableBody').append(row);
                }
            });
            $('#countResult').text('不为空的codeContent个数：' + count);
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
});
