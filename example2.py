import TextBGE as engine

canvas = engine.Canvas(17, 3)
out = "..."

while True:
    frame = canvas.Frame()
    frame.Draw.fill("#")
    frame.Draw.rect(" ", 1, 1, 16, 2)
    frame.merge()

    frame = canvas.Frame("requireIO")
    frame.Draw.text(out, 2, 1, 14)
    out = frame.merge()