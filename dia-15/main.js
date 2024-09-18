let contador = document.querySelector('.contador')
let input = document.querySelector('input')

input.addEventListener('input', () => {
    contador.textContent = input.value.replace(/\s/g, "").length
});
