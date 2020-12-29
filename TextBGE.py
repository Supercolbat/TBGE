import os, time

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]

        self.Draw = Draw(self, True)

        self.update()

    def Frame(self, *args):
        return self.frameClass(self, args)

    class frameClass:
        def __init__(self, parent, args):
            self.parent = parent

            self.height = self.parent.height
            self.width = self.parent.width
            self.canvas = self.parent.canvas

            self.args = args

            self.Draw = Draw(self)

        def merge(self):
            self.parent.canvas = self.canvas
            self.parent.update()

            if "requireIO" in self.args:
                return input("> ")

    def update(self):
        os.system("clear")
        print('\n'.join([''.join(l) for l in self.canvas]))

class Draw:
    def __init__(self, parent, autoUpdate=False):
        self.parent = parent
        self.drawUpdate = lambda: self.parent.update() if autoUpdate else None

    def point(self, char, x, y):
        self.parent.canvas[y][x] = char
        
        self.drawUpdate()

    def fill(self, char):
        self.parent.canvas = [[char for _ in range(self.parent.width)] for _ in range(self.parent.height)]
        
        self.drawUpdate()

    def rect(self, char, x1, y1, x2, y2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                try:
                    self.parent.canvas[y][x] = char
                except:
                    pass
        
        self.drawUpdate()

    def text(self, string, x, y, maxWidth=None):
        for i,c in enumerate(string):
            if x+i >= self.parent.width or (maxWidth and x+i > maxWidth): break
            self.parent.canvas[y][x+i] = c

        self.drawUpdate()