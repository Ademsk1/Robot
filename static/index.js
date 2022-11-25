
//first test, let the button click activate the robot to move for a short period. 
async function buttonClick(command) {
    try {
        const res = await fetch(`http://127.0.0.1:5000/${command}`, {
            method: 'GET',
            headers: {
                accept: 'application/json'
            }
        })
    } catch {
        console.log(res.status)
    }
        
        print
    data = await res.json()
}
function up() {
    buttonClick('forward')
}
function reverse() {
    buttonClick('reverse')
}
function left() {
    buttonClick('left')
}
function right() {
    buttonClick('right')
}