function changeMode(mode) {

    getBotao = document.querySelector('.switcher')
    getTema = document.body
    getTema.removeAttribute("data-theme")
    
    if(mode == 0){
        getTema.setAttribute("data-theme", "light")
        getBotao.setAttribute('onclick', "changeMode(1)")
    }else{
        getTema.setAttribute("data-theme", "dark")
        getBotao.setAttribute('onclick', "changeMode(0)")
    }
}