slideShow = document.getElementById('wrap')
window.onload = function () {    
let i = 0;
let j = 0;    
setInterval(() => {
    let sStyle = slideShow.style;
    if (sStyle.length == 0) slideShow.style['top']  = -60 + 'vh';
    else {
    current = sStyle['top']
    arr = current.split('v')
    val = arr[0]
    slideShow.style['top']  = val - 60 + 'vh';}
    i++
    if (i >= 3)
    {
        let v = document.getElementsByClassName('slideimg')[j]
        let node = v.cloneNode(deep=true)
        slideShow.appendChild(node)
        if (j >= 3) j = 0;
        else j++
    }
    }, 8000);
}
function scrollV() {
    let anchorlinks = document.querySelectorAll('a[href^="#"]')

    for (let item of anchorlinks) { // relitere 
        item.addEventListener('click', (e)=> {
        let hashval = item.getAttribute('href')
        let target = document.querySelector(hashval)
        target.scrollIntoView({
        behavior: 'smooth'
        })
        history.pushState(null, null, hashval)
        e.preventDefault()
    })
    }
    }