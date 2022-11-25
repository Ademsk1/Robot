
//first test, let the button click activate the robot to move for a short period. 
async function buttonClick(command) {
    const res = await fetch(`http://127.0.0.1:5000/${command}`, {
        method: 'GET'
    })
    data = await res.json()
}
const up = () => {
    buttonClick('forward')
}
const reverse = () => {
    buttonClick('reverse')
}
const left = () => {
    buttonClick('left')
}
const right  = () => {
    buttonClick('right')
}