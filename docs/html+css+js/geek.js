
const ques = document.querySelectorAll('.ques'); 
// 获取所有类名为answer的元素，也就是所有答案盒子的DOM节点，返回一个NodeList对象
const answers = document.querySelectorAll('.answer'); 

// 遍历所有问题元素
ques.forEach((ques, index) => { 
  // 为每个问题元素添加点击事件监听器
  ques.addEventListener('click', function () { 
    // 根据当前问题元素的索引，获取对应的答案元素
    const answer = answers[index]; 
    // 将对应的答案元素的display属性设置为block，使其显示出来
    answer.style.display = 'block'; 
  });

  // 为每个问题元素添加鼠标离开事件监听器
  ques.addEventListener('mouseleave', function () { 
    // 根据当前问题元素的索引，获取对应的答案元素
    const answer = answers[index]; 
    // 将对应的答案元素的display属性设置为none，使其隐藏起来
    answer.style.display = 'none'; 
  });
});
// 获取类名为 button3 的元素并赋值给 button 变量
const button = document.querySelector('.button3');
// 为 button 元素添加点击事件监听器
button.addEventListener('click', function () {
    // 当按钮被点击时，将窗口的地址重定向到指定的 B 站视频链接
    window.location.href = 'http://www.bilibili.com/video/BV1GJ411x7h7/';
});

// 当 DOM 内容加载完成后执行回调函数
document.addEventListener("DOMContentLoaded",() => {
    // 获取 id 为 emailButton 的元素并赋值给 emailButton 变量
    const emailButton = document.getElementById('emailButton');
    // 获取类名为 tan 的元素并赋值给 emailPopup 变量，该元素可能是一个弹出框
    const emailPopup = document.querySelector('.tan');
    // 获取类名为 queding 的元素并赋值给 closePopupButton 变量，该元素可能是关闭弹出框的按钮
    const closePopupButton = document.querySelector('.queding');

    // 为 emailButton 元素添加点击事件监听器
    emailButton.addEventListener("click", (event) => {
        // 阻止按钮的默认行为
        event.preventDefault();
        // 将 emailPopup 元素的显示样式设置为 block，即显示弹出框
        emailPopup.style.display='block';
        // 使用 Clipboard API 将指定的邮箱地址复制到剪贴板
        navigator.clipboard.writeText("newthread_geek@outlook.com").then(() => {
            console.log("邮箱地址已复制到剪贴板");
        });
    });

    // 为 closePopupButton 元素添加点击事件监听器
    closePopupButton.addEventListener("click",() =>{
        // 将 emailPopup 元素的显示样式设置为 none，即隐藏弹出框
        emailPopup.style.display='none';
    });
});

// 当 DOM 内容加载完成后执行回调函数
document.addEventListener("DOMContentLoaded", () => {
    // 获取类名为 point 的元素并赋值给 pointer 变量
    const pointer = document.querySelector('.point');

    // 如果 pointer 元素存在
    if (pointer) {
        // 为窗口添加滚动事件监听器
        window.addEventListener("scroll", () => {
            // 获取当前窗口的垂直滚动位置
            const scrollPosition = window.scrollY;
            // 根据滚动位置决定是否显示 pointer 元素
            pointer.style.display = scrollPosition >= 800? "block" : "none";
        });

        // 为 pointer 元素添加点击事件监听器
        pointer.addEventListener("click", () => {
            // 将窗口滚动到顶部，滚动行为设置为平滑滚动
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }
});

// 定义一个函数，用于滚动到指定类名的元素位置
function scrollToSection(sectionClass) {
    // 根据传入的类名获取对应的元素
    const targetSection = document.querySelector('.'+sectionClass);
    // 将窗口滚动到目标元素的顶部位置，滚动行为设置为平滑滚动
    window.scrollTo({
        top: targetSection.offsetTop,
        behavior: 'smooth'  
    });
}
