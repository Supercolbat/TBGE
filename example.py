import TextBGE as engine
import time
import random

canvas = engine.Canvas(21, 6)

ball1 = {
    "position": [random.randint(0,canvas.width), random.randint(0,canvas.height)],
    "velocity": [random.choice([-1,1]), random.choice([-1,1])]
}
ball2 = {
    "position": [random.randint(0,canvas.width), random.randint(0,canvas.height)],
    "velocity": [random.choice([-1,1]), random.choice([-1,1])]
}


canvas.Draw.fill('.')

def updateBalls():
    futureX1 = ball1["position"][0] + ball1["velocity"][0]
    futureY1 = ball1["position"][1] + ball1["velocity"][1]
    futureX2 = ball2["position"][0] + ball2["velocity"][0]
    futureY2 = ball2["position"][1] + ball2["velocity"][1]

    if futureX1 >= canvas.width or futureX1 < 0:
        ball1["velocity"][0] = -ball1["velocity"][0]
    if futureY1 >= canvas.height or futureY1 < 0:
        ball1["velocity"][1] = -ball1["velocity"][1]
    if futureX2 >= canvas.width or futureX2 < 0:
        ball2["velocity"][0] = -ball2["velocity"][0]
    if futureY2 >= canvas.height or futureY2 < 0:
        ball2["velocity"][1] = -ball2["velocity"][1]

    ball1["position"][0] += ball1["velocity"][0]
    ball1["position"][1] += ball1["velocity"][1]
    ball2["position"][0] += ball2["velocity"][0]
    ball2["position"][1] += ball2["velocity"][1]


    frame = canvas.Frame()
    frame.Draw.fill('.')
    frame.Draw.point('O', *ball1["position"])
    frame.Draw.point('X', *ball2["position"])
    frame.merge()


while True:
    updateBalls()
    time.sleep(0.1)
