let box = document.querySelector('.box')
let input = document.querySelector('input')

input.addEventListener('input', () => {
    box.style.background = input.value
    box.style.borderRadius = input.value
});
