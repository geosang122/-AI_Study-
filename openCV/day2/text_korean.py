## 한글 우회 방법
#PIL (Python Image Library)
from PIL import ImageFont, ImageDraw,Image

def myPutText(src,text,pos,font_size,font_color):
    img_pil=Image.fromarray(src)
    draw=ImageDraw.Draw(img_pil)
    font=ImageFont.truetype("fonts/gulim.ttc",font_size)
    draw.text(pos,text,font=font,fill=font_color)
    return np.array(img_pil)

import numpy as np
import cv2

img=np.zeros((512,512,3), dtype=np.uint8)

COLOR=(255,255,255)
FONT_SIZE=30

img=myPutText(img, "상현_simplex",(20,50), FONT_SIZE, COLOR)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()