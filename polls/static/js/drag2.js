var draggableElements = document.querySelectorAll('.draggable');
var droppableElements = document.querySelectorAll('.droppable');
var draggableElement = null;

// 添加拖拽事件监听器
draggableElements.forEach(function(element) {
  element.addEventListener('dragstart', dragStart);
  element.addEventListener('dragend', dragEnd);
});

// 添加放置事件监听器
droppableElements.forEach(function(element) {
  element.addEventListener('dragenter', dragEnter);
  element.addEventListener('dragover', dragOver);
  element.addEventListener('dragleave', dragLeave);
  element.addEventListener('drop', drop);
});

// 拖拽开始事件
function dragStart(e) {
  draggableElement = this;
  setTimeout(function() {
    draggableElement.classList.add('hide');
  }, 0);
}

// 拖拽结束事件
function dragEnd(e) {
  draggableElement.classList.remove('hide');
  draggableElement = null;
}

// 放置进入事件
function dragEnter(e) {
  e.preventDefault();
  this.classList.add('highlight');
}

// 放置悬停事件
function dragOver(e) {
  e.preventDefault();
}

// 放置离开事件
function dragLeave(e) {
  this.classList.remove('highlight');
}

var droppable1Content = null;
var droppable2Content = null;
var droppable3Content = null;
var droppable4Content = null;
var droppable5Content = null;
var droppable6Content = null;
var droppable7Content = null;
var droppable8Content = null;
var droppable9Content = null;
var droppable10Content = null;
var draggableContentArray = [];

function drop(e) {
   e.preventDefault();
  this.classList.remove('highlight');
  this.appendChild(draggableElement);
  var content = draggableElement.textContent;
  this.setAttribute('data-value', content);
  console.log("fuzhi6:" + content);
  // 根据放置区域的id保存拖拽的内容
  var index = parseInt(this.id.replace('droppable', ''));
  console.log("fuzhi4:" + index);
  if (draggableContentArray[index]) {
  // 如果指定索引位置已经有值，则将新值与原有值合并成一个字符串
  var mergedContent = draggableContentArray[index] + ',' + content;
  draggableContentArray[index] = mergedContent;
  } else {
  // 如果指定索引位置没有值，则直接将新值赋给该位置
  draggableContentArray[index] = content;
   }
   content=draggableContentArray[index];
   console.log("fuzhi7:" + content);
   console.log("draggableContentArray: " + draggableContentArray);
  if (this.id === 'droppable1') {
    document.getElementById('droppable1ContentInput').value = content;
  }
  else if (this.id === 'droppable2') {
    document.getElementById('droppable2ContentInput').value = content;
  }
  else if (this.id === 'droppable3') {
    document.getElementById('droppable3ContentInput').value = content;
  }
  else if (this.id === 'droppable4') {
    document.getElementById('droppable4ContentInput').value = content;
  }
    else if (this.id === 'droppable5') {
    document.getElementById('droppable5ContentInput').value = content;
  }
    else if (this.id === 'droppable6') {
    document.getElementById('droppable6ContentInput').value = content;
}
else if (this.id === 'droppable7') {
    document.getElementById('droppable7ContentInput').value = content;
}
else if (this.id === 'droppable8') {
    document.getElementById('droppable8ContentInput').value = content;
}
else if (this.id === 'droppable9') {
    document.getElementById('droppable9ContentInput').value = content;
}
 else if (this.id === 'droppable10') {
    document.getElementById('droppable10ContentInput').value = content;
}
}
