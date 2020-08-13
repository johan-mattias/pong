def on_received_number(receivedNumber):
    if receivedNumber == 1:
        ping.change(LedSpriteProperty.X, 1)
    elif receivedNumber == -1:
        ping.change(LedSpriteProperty.X, -1)
    else:
        pass
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    pong.change(LedSpriteProperty.X, -1)
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pong.change(LedSpriteProperty.X, 1)
    radio.send_number(-1)
input.on_button_pressed(Button.B, on_button_pressed_b)

ping: game.LedSprite = None
pong: game.LedSprite = None
radio.set_group(1)
pong = game.create_sprite(2, 5)
ping = game.create_sprite(2, 0)
ball = game.create_sprite(2, 2)
ball.turn(Direction.RIGHT, 45)
game.set_life(3)

def on_forever():
    if ball.is_touching(pong):
        ball.set(LedSpriteProperty.Y, 3)
        basic.pause(200)
        game.add_score(1)
    elif ball.get(LedSpriteProperty.Y) == 4:
        basic.pause(200)
        game.remove_life(1)
    elif ball.is_touching(ping):
        ball.set(LedSpriteProperty.Y, 1)
        basic.pause(200)
    else:
        pass
    ball.move(1)
    ball.if_on_edge_bounce()
    basic.pause(2000)
    radio.send_value("ballx", ball.get(LedSpriteProperty.X))
    radio.send_value("bally", ball.get(LedSpriteProperty.Y))
basic.forever(on_forever)
