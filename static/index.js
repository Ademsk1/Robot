
//first test, let the button click activate the robot to move for a short period. 
async function buttonClick(command) {
    const res = await fetch(`${window.location.href}/${command}`, {
        method: 'GET'
    })
    data = await res.json()
}
async function up() {
    buttonClick('forward')
}
async function reverse() {
    buttonClick('reverse')
}
async function left() {
    buttonClick('left')
}
async function right() {
    buttonClick('right')
}