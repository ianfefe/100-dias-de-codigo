function formata(param){
    if(param < 10)
        return `0${param}` 
    return param
}

function display(){
    let time = document.querySelector('#clock')
    let data = new Date()
    let hora = data.getHours()
    let min = data.getMinutes()
    let seg = data.getSeconds()

    texto =  `${formata(hora)}:${formata(min)}:${formata(seg)}`
    time.textContent = texto
}

setInterval(display, 1000);