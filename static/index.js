
//first test, let the button click activate the robot to move for a short period. 
async function buttonClick(command) {
    const res = await fetch(`http://0.0.0.0:5000/${command}`, {
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