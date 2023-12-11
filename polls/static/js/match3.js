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
        value2 = 'fund scale';
    }
    if (value == 'x3') {
        value2 = 'Accumulated unit net value';
    }
    if (value == 'x4') {
        value2 = 'The average number of products managed per fund manager';
    }
    if (value == 'x5') {
        value2 = 'Jensen';
    }
    if (value == 'x6') {
        value2 = 'Investment style';
    }
    if (value == 'x7') {
        value2 = 'Education level';
    }
    if (value == 'x8') {
        value2 = 'Treynor';
    }
    if (value == 'x9') {
        value2 = 'Sharpe';
    }
    if (value == 'x10') {
        value2 = 'Shareholders equity at the beginning of the period';
    }
    if (value == 'x11') {
        value2 = 'Shareholders equity at the end of the period';
    }
    if (value == 'x12') {
        value2 = 'Fund shares';
    }
    if (value == 'x13') {
        value2 = 'The average tenure of fund managers';
    }
    if (value == 'x14') {
        value2 = 'Team stability';
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
        console.log('111选择的值是：' + selectedValue);
        // 在这里可以根据选择的值做出相应的改变
        addLevelSelect(newIndicator, num, selectedValue);
        selectedValues.push(selectedValue);
        console.log('已经添加了：' + selectedValues);
    });


    document.querySelector('form').appendChild(newIndicator);

    // 在newIndicator元素的后面添加levelLabel和levelSelect
}

function addLevelSelect(newIndicator, num, selectedValue) {
    var levelLabel = document.createElement('label');
    levelLabel.textContent = 'level :';
    newIndicator.appendChild(levelLabel);

    var classContent;
    if (selectedValue == 'fund scale' || selectedValue == 'Accumulated unit net value') {
        classContent = 5;
    } else if (selectedValue == 'The average number of products managed per fund manager' || selectedValue == 'The average tenure of fund managers' || selectedValue == 'Team stability'){
        classContent = 4;
    } else if (selectedValue == 'Jensen' || selectedValue == 'Investment style' || selectedValue == 'Treynor' || selectedValue == 'Sharpe') {
        classContent = 2;
    } else if (selectedValue == 'Education level' || selectedValue == 'Shareholders equity at the beginning of the period' || selectedValue == 'Shareholders equity at the end of the period') {
        classContent = 3;
    } else if (selectedValue == 'Fund shares') {
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