
//first test, let the button click activate the robot to move for a short period. 
async function buttonClick(command) {
    
    const res = await fetch(`http://127.0.0.1:5000/${command}`, {
        method: 'GET',
        headers: {
            accept: 'application/json',
            mode: 'no-cors'
        }
    })

    console.log(res.status)

    
    print
    data = await res.json()
}
function up() {
    buttonClick('forward')
    console.log('done')
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