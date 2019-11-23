let myGamePiece;
let myObstacles = [];
let myScore;

// for starting the main frame and add game piece
function startGame() {
    myGame.start();
    myScore = new myGameComponent("20px", "Consolas", "black", 300, 40, "text");
    myGamePiece = new myGameComponent(30, 30, "red", 10, 120, "gamer");
    myGamePiece.gravityAcceleration = 0.05;
}

function reloadGame() {
	myGame.stop();
	myGame.clear();
	//myGame = {};
	myGamePiece = {};
	myObstacles = [];
	myScore = {};
	startGame()
}


// game main frame
const myGame = {
    // initiate the game frame
    start : function() {
        this.canvas = document.getElementById("myGame1Canvas");
        this.canvas.width = 465;
        this.canvas.height = 320;
        this.context = this.canvas.getContext("2d");
        this.frameNo = 0;

        this.interval = setInterval(updateGame, 20); // update game frame every 20 ms
        // add keyboard listener
        window.addEventListener('keydown', function(e) {
            myGame.key = e.keyCode;
        });
        window.addEventListener('keyup', function(e) {
            myGame.key = false;
        });
    },
    // function for clearing the frame
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    // function to stop the game
    stop : function() {
        clearInterval(this.interval);
    },
}

function everyNFrame(n) {
    return (myGame.frameNo / n) % 1 === 0;
}

// component in the game frame
function myGameComponent(width, height, color, x, y, type) {
    this.type = type;
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    this.speedX = -1;
    this.speedY = 0;
    this.gravitySpeed = 0;
    this.gravityAcceleration = 0;

    // render rectangle
    this.update = function() {
        let ctx = myGame.context;
        if(this.type === "text") {
            ctx.font =  this.width + " " + this.height;
            ctx.fillStyle = color;
            ctx.fillText(this.text, this.x, this.y);
        } else {
            ctx.fillStyle = color;
            ctx.fillRect(this.x, this.y, this.width, this.height);
        }
    };

    // calculate new position
    this.newPose = function() {
        this.gravitySpeed += this.gravityAcceleration;
        if(this.gravitySpeed > 0.5) {
            this.gravitySpeed = 0.5;
        }

        if(this.speedX > 1) {this.speedX = 1; };
        if(this.speedX < -1) {this.speedX = -1; };
        if(this.speedY > 1) {this.speedY = 1; };
        if(this.speedY < -1) {this.speedY = -1; };

        this.x += this.speedX;
        this.y += this.speedY + this.gravitySpeed;

        // prevent the game piece from passing the wall
        if(this.type === "gamer") {
            if(this.y > (myGame.canvas.height - myGamePiece.height)) {
                this.y = myGame.canvas.height - myGamePiece.height;
            }
            if(this.y < 0) {
                this.y = 0;
            }
            if(this.x > (myGame.canvas.width - myGamePiece.width)) {
                this.x = myGame.canvas.width - myGamePiece.width;
            }
            if(this.x < 0) {
                this.x = 0;
            }
        }
    };

    // determine if the game piece is crashed
    this.crashWith = function(otherOBJ) {
        let myLeft = this.x;
        let myRight = this.x + this. width;
        let myTop = this.y;
        let myBottom = this.y + this.height;
        let objLeft = otherOBJ.x;
        let objRight = otherOBJ.x + otherOBJ. width;
        let objTop = otherOBJ.y;
        let objBottom = otherOBJ.y + otherOBJ.height;
        let crash = true;
        if ((myBottom < objTop) || (myTop > objBottom) || (myRight < objLeft) || (myLeft > objRight)) {
            crash = false;
        }
        return crash;
    }
}

function updateGame() {
    for(let i = 0; i < myObstacles.length; i += 1) {
        if(myGamePiece.crashWith(myObstacles[i])) {
            myGame.stop();
            return;
        }
    }
    myGame.clear();
    myGame.frameNo += 1;

    // react to keyboard input and set velocity
    if (myGame.key && myGame.key === 37) {
        myGamePiece.speedX += -0.2;
    };
    if (myGame.key && myGame.key === 39) {
        myGamePiece.speedX += 0.2;
    };
    if (myGame.key && myGame.key === 38) {
        myGamePiece.speedY += -0.25;
    };
    if (myGame.key && myGame.key === 40) {
        myGamePiece.speedY += 0.15;
    };

    // add new obstacles with random position
    if (myGame.frameNo === 1 || everyNFrame(150)) {
        let minHeight = 20;
        let maxHeight = 200;
        let height = Math.floor(Math.random() * (maxHeight - minHeight + 1) + minHeight);
        let minGap = 50;
        let maxGap = 200;
        let gap = Math.floor(Math.random() * (maxGap - minGap + 1) + minGap);
        myObstacles.push(new myGameComponent(20, height, "green", myGame.canvas.width, 0));
        myObstacles.push(new myGameComponent(20, myGame.canvas.width - height - gap, "green", myGame.canvas.width, height + gap));
    }

    // update obstacles
    for(let i = 0; i < myObstacles.length; i += 1) {
        myObstacles[i].newPose();
        myObstacles[i].update();
    }

    // update score
    myScore.text = "Score: " + myGame.frameNo;
    myScore.update();

    // update game piece
    myGamePiece.newPose();
    myGamePiece.update();
}