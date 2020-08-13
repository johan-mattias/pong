radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        ping.change(LedSpriteProperty.X, 1)
    } else if (receivedNumber == -1) {
        ping.change(LedSpriteProperty.X, -1)
    } else {
    	
    }
})
input.onButtonPressed(Button.A, function () {
    pong.change(LedSpriteProperty.X, -1)
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    pong.change(LedSpriteProperty.X, 1)
    radio.sendNumber(-1)
})
let ping: game.LedSprite = null
let pong: game.LedSprite = null
radio.setGroup(1)
pong = game.createSprite(2, 5)
ping = game.createSprite(2, 0)
let ball = game.createSprite(2, 2)
ball.turn(Direction.Right, 45)
game.setLife(3)
basic.forever(function () {
    if (ball.isTouching(pong)) {
        ball.set(LedSpriteProperty.Y, 3)
        basic.pause(200)
        game.addScore(1)
    } else if (ball.get(LedSpriteProperty.Y) == 4) {
        basic.pause(200)
        game.removeLife(1)
    } else if (ball.isTouching(ping)) {
        ball.set(LedSpriteProperty.Y, 1)
        basic.pause(200)
    } else {
    	
    }
    ball.move(1)
    ball.ifOnEdgeBounce()
    basic.pause(2000)
    radio.sendValue("ballx", ball.get(LedSpriteProperty.X))
    radio.sendValue("bally", ball.get(LedSpriteProperty.Y))
})
