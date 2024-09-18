function changeMode(mode) {

    getTema = document.querySelector('.container')
    getTema.removeAttribute("data-theme")

    if(mode == 0)
        getTema.setAttribute("data-theme", "light")
    else
        getTema.setAttribute("data-theme", "dark")
}