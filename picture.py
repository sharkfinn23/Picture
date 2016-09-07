"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
rectangle = PolygonAsset([(0,0), (0,100), (250,100), (250,0)], thinline, blue)
circle = CircleAsset(25, thinline, red)
ellipse = EllipseAsset(10, 30, thinline, green)
roof= PolygonAsset([(50,100), (175,0), (300,100), (50,100)], thinline, red)


Sprite(rectangle, (50, 100))
Sprite(roof)
Sprite(ellipse, (175,170))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
