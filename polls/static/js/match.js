var selectedValues = [];
function addIndicator() {
    var num = document.querySelectorAll('.indicator').length;
    var newIndicator = document.createElement('div');
    newIndicator.className = 'indicator';

    var indicatorLabel = document.createElement('h2');
    indicatorLabel.textContent = 'index' + num;
    newIndicator.appendChild(indicatorLabel);

    var indicatorSelect = document.createElement('select');
    indicatorSelect.name = 'x' + num;

    for (var i = 1; i <= 14; i++) {
        var value = 'x' + i;
            if (value == 'x1') {
        value2 = '';
    }
    if (value == 'x2') {
        value2 = '基金规模';
    }
    var option = document.createElement('option');
    option.value = value2;
    option.textContent = value2;
         if (selectedValues.includes(value2)) {
        continue;
        }
    indicatorSelect.appendChild(option);

    }
    newIndicator.appendChild(indicatorSelect);
    indicatorSelect.addEventListener('change', function() {
        var selectedValue = indicatorSelect.value;
        addLevelSelect(newIndicator, num, selectedValue);
        selectedValues.push(selectedValue);
    });
    document.querySelector('form').appendChild(newIndicator);
}

function addLevelSelect(newIndicator, num, selectedValue) {
    var levelLabel = document.createElement('label');
    levelLabel.textContent = '等级:';
    newIndicator.appendChild(levelLabel);

    var classContent;
    if (selectedValue == '基金规模' || selectedValue == '累计单位净值') {
        classContent = 5;
    } else if (selectedValue == '基金经理人均管理产品数' || selectedValue == '基金经理平均年限' || selectedValue == '团队稳定性') {
        classContent = 4;
    } else if (selectedValue == 'Jensen' || selectedValue == '投资风格' || selectedValue == 'Treynor' || selectedValue == 'Sharpe') {
        classContent = 2;
    } else if (selectedValue == '学历' || selectedValue == '期初所有者权益' || selectedValue == '期末所有者权益') {
        classContent = 3;
    } else if (selectedValue == '基金份额') {
        classContent = 5;
    } else {
        classContent = null;
    }

    var levelSelect = document.createElement('select');
    levelSelect.name = 'level' + num;
    for (var i = 1; i <= classContent; i++) {
        var option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        levelSelect.appendChild(option);
    }
    newIndicator.appendChild(levelSelect);
}


function submitForm(event) {
event.preventDefault();
var selectedIndicators = [];
var selectedLevels = [];

// 获取选中的指标和等级数据
var indicatorSelects = document.querySelectorAll('select[name^="x"]');
indicatorSelects.forEach(function(select) {
  selectedIndicators.push(select.value);
});

var levelSelects = document.querySelectorAll('select[name^="level"]');
levelSelects.forEach(function(select) {
  selectedLevels.push(select.value);
});

// 创建一个对象，将选中的数据添加到其中
var data = {
  indicators: selectedIndicators,
  levels: selectedLevels,
};
console.log(data.indicators);
var matchContentInputs = [
  document.getElementById('match1ContentInput'),
  document.getElementById('match2ContentInput'),
  document.getElementById('match3ContentInput'),
  document.getElementById('match4ContentInput'),
  document.getElementById('match5ContentInput'),
  document.getElementById('match6ContentInput'),
  document.getElementById('match7ContentInput'),
  document.getElementById('match8ContentInput'),
  document.getElementById('match9ContentInput'),
  document.getElementById('match10ContentInput')
];

var levelContentInputs = [
    document.getElementById('level1ContentInput'),
    document.getElementById('level2ContentInput'),
    document.getElementById('level3ContentInput'),
    document.getElementById('level4ContentInput'),
    document.getElementById('level5ContentInput'),
    document.getElementById('level6ContentInput'),
    document.getElementById('level7ContentInput'),
    document.getElementById('level8ContentInput'),
    document.getElementById('level9ContentInput'),
    document.getElementById('level10ContentInput')
];
for (var i = 0; i < 10; i++) {
  if (data.indicators.length > i) {
    matchContentInputs[i].value = data.indicators[i];
  } else {
    matchContentInputs[i].value = '';
  }

  if (data.levels.length > i) {
    levelContentInputs[i].value = data.levels[i];
  } else {
    levelContentInputs[i].value = '';
  }
}
    console.log(levelContentInputs.map(input => input.value));
    console.log(matchContentInputs.map(input => input.value));
}