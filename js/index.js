var leftBand = document.querySelector('.left-band');
var search = document.querySelector('.search');
var chevronLeft = document.querySelector('.left-band').querySelector('.chevron-left');
var mainPage = document.querySelector('#main-page');

chevronLeft.addEventListener('click', showMain)


var scrollFunc = function (e) {
    var direct = 0;
    e = e || window.event;
    if (e.wheelDelta) {  //判断浏览器IE，谷歌滑轮事件             
        if (e.wheelDelta > 0) { //当滑轮向上滚动时
            mouseUpScroll();
        }
        if (e.wheelDelta < 0) { //当滑轮向下滚动时
            mouseDownScroll();
        }
    } else if (e.detail) {  //Firefox滑轮事件
        if (e.detail < 0) { //当滑轮向上滚动时
            mouseUpScroll();
        }
        if (e.detail > 0) { //当滑轮向下滚动时
            mouseDownScroll();
        }
    }
    // ScrollText(direct);
}
//给页面绑定滑轮滚动事件
document.addEventListener('DOMMouseScroll', scrollFunc, false);
//滚动滑轮触发scrollFunc方法
window.onmousewheel = document.onmousewheel = scrollFunc;  

var mouseUpScroll = function(){
    
}
var mouseDownScroll = function(){
    showMain();
    document.removeEventListener('DOMMouseScroll', scrollFunc);
    window.onmousewheel = document.onmousewheel = null;  
}

function showMain() {
    animate(leftBand, -leftBand.offsetWidth);
    animate(search, search.parentNode.offsetWidth, fadeIn(mainPage, 15));
}

function fadeIn(element, speed) {
    element.style.display = 'block';
    var speed = speed || 30;
    var num = 0;
    var st = setInterval(function () {
        num++;
        element.style.opacity = num / 100;
        if (num == 100) { clearInterval(st); }
    }, speed);
}

function animate(obj, target, callback) {
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        // var step = Math.ceil((target - obj.offsetLeft) / 10);
        var step = (target - obj.offsetLeft) / 10;
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        if (obj.offsetLeft == target) {
            clearInterval(obj.timer);
            if (callback) {
                callback();
            }
        }
        obj.style.left = obj.offsetLeft + step + 'px';
    }, 15);
}