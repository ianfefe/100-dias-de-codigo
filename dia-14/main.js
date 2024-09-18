function changeMode() {

    getBotao = document.querySelector('.switcher')
    getTema = document.body
    
    if(getTema.getAttribute('data-theme') != "light"){
        getTema.setAttribute("data-theme", "light")
        getBotao.setAttribute('onclick', "changeMode()")
    }else{
        getTema.setAttribute("data-theme", "dark")
        getBotao.setAttribute('onclick', "changeMode()")
    }
}