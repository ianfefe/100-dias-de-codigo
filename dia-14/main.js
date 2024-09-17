function changeMode(sheet) {
    document.querySelector('link').setAttribute('href', `${sheet}.css`)
}

function dayMode() {
    let light = 'lightStyle'

    document.querySelector('link').removeAttribute('href')
    changeMode(light)
}

function nightMode() {
    let dark = 'darkStyle'

    document.querySelector('link').removeAttribute('href')
    changeMode(dark)
}