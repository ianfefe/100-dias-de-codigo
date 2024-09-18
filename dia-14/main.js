function changeMode() {

    getBotao = document.querySelector('.switcher')
    getTema = document.body
    
    if(getTema.getAttribute('data-theme') != "light")
        getTema.setAttribute("data-theme", "light")
    else
        getTema.setAttribute("data-theme", "dark")
}