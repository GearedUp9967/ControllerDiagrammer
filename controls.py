from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import webbrowser
import os
im = Image.open("logitech.png")
print(im.format, im.size, im.mode)
draw = ImageDraw.Draw(im)
text=""
class TextBox:
    def __init__(self,text,coords,font,right=False):
        self.coords=coords
        self.font=font
        self.text=text
        self.width, self.height = self.font.getsize(self.text)
        if right:
            self.setRightAlign()
        else:
            self.setLeftAlign()
    def setLeftAlign(self):
        self.aligned=(self.coords[0],self.coords[1]-self.height/2)
    def setRightAlign(self):
        self.aligned=(self.coords[0]-self.width,self.coords[1]-self.height/2)
    def getCoords(self):
        return self.aligned
    def getX(self):
        return self.aligned[0]
    def getY(self):
        return self.aligned[1]
    def getText(self):
        return self.text
    def getFont(self):
        return self.font

fnt = ImageFont.truetype("OCRAEXT.ttf", 17)
coordsR={
    "dpad_up":(190,125),
    "dpad_right":(190,145),
    "dpad_left":(190,165),
    "dpad_down":(190,185),
    "back":(270,40),
    "mode":(270,63),
    "start":(270,20),
    "left_stick":(190,320),
    "right_stick":(190,345),
    "left_stick_button":(190,370),
    "right_stick_button":(190,390),
    "right_bumper":(590,365),
    "left_bumper":(850,365),
    "right_trigger":(590,388),
    "left_trigger":(850,388)
    }

coordsL={
    "y":(777,50),
    "x":(777,70),
    "b":(777,85),
    "a":(777,105)
    }
boxes=[]
"""
for r in coordsR:
    boxes.append(TextBox(r,coordsR[r],fnt,right=True))
                 
for l in coordsL:
    boxes.append(TextBox(l,coordsL[l],fnt,right=False))
"""

filename="controls.txt"
if not os.path.isfile(filename):
    file=open(filename,'w+')
    for key in coordsR:
        file.write(key+":\r\n")
    for key in coordsL:
        file.write(key+":\r\n")
    file.close()
        
while True:
    print("Type e to edit or g to generate control diagram")
    letter=input()
    if letter=='e':
        webbrowser.open(filename)
    elif letter=='g':
        file=open(filename)
        for line in file.readlines():
            if line[-1]=='\n':
                line=line[0:-1]
            button=line.split(":")[0]
            text=' '.join(line.split(":")[1:])
            if button in coordsR:
                boxes.append(TextBox(text,coordsR[button],fnt,right=True))
            elif button in coordsL:
                boxes.append(TextBox(text,coordsL[button],fnt,right=False))
        break

for b in boxes:
    draw.text(b.getCoords(),b.getText(),(0,0,0),b.getFont())
"""
for i in range(0,len(boxes)):
    b=boxes[i]
    draw.text(b.getCoords(),b.getText(),(0,0,0),b.getFont())
    draw.text((b.getX(),b.getY()+395),b.getText(),(0,0,0),b.getFont())
"""
im.show()
