function toggleHeader() {
    if (document.getElementById('header').style['top'] === '0em')
    {
        document.getElementById('header').style['top'] = '-3.5em';
        document.getElementById('body-container').style['top'] = '-3.5em';
        document.getElementById('body-container').style['margin-bottom'] = '-3.5em';
    }
    else
    {
      document.getElementById('header').style['top'] = '0em';
      document.getElementById('body-container').style['top'] = '0em';
      document.getElementById('body-container').style['margin-bottom'] = '0em';
    }
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