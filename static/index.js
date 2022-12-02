
//first test, let the button click activate the robot to move for a short period. 



async function buttonClick(command) {
    
    const res = await fetch(`http://192.168.1.80:5000/${command}`, {
        method: 'GET',
        headers: {
            accept: 'application/json',
        }
    })

    console.log(res.status)

    
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
function stop() {
    buttonClick('stop')
}

window.addEventListener('DOMContentLoaded', function () {
    this.document.addEventListener('keydown', (e) => {{
        e.preventDefault()
        if (e.key=='ArrowLeft') {
            left()
        }
        if (e.ley=='ArrowRight') {
            right()
        }
        if (e.key=='ArrowUp') {
            up()
        }
        if (e.key=='ArrowDown') {
            reverse()
        }
    }})
    this.document.addEventListener('keyup', (e)=> {
        stop()
    })




})