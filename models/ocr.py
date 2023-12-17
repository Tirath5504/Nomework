from PIL import Image
import pytesseract
from pytesseract import Output
import re
import cv2
import numpy as np
import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r'D:\PYTHON\Mumbai Hacks 23\test.png')
# cv2.waitKey(0)
img = cv2.resize(img, (600, 360))
hImg, wImg, _ = img.shape

# output_folder = 'cropped_contours'
# os.makedirs(output_folder, exist_ok=True)

boxes = pytesseract.image_to_boxes(img) #so ik borders of each letter

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
# cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged,   
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
# cv2.imshow('Canny Edges After Contouring', edged) 
# cv2.waitKey(0) 
  
############

#STACK OVERFLOW CODE FOR SVG GENERATION OF ALL CONTOURS

# with open("path.svg", "w+") as f:
#     f.write(f'<svg width="{wImg}" height="{hImg}" xmlns="http://www.w3.org/2000/svg">')

#     for c in contours:
#         f.write('<path d="M')
#         for i in range(len(c)):
#             x, y = c[i][0]
#             f.write(f"{x} {y} ")
#         f.write('" style="stroke:pink"/>')
#     f.write("</svg>")
    
    
    ##############
    
#
    
# with open("path.svg", "w+") as f:
#     for idx, c in enumerate(contours):
#         f.write(f'<svg width="{wImg}" height="{hImg}" xmlns="http://www.w3.org/2000/svg">')
#         f.write(f'<path d="M')
#         for i in range(len(c)):
#             x, y = c[i][0]
#             f.write(f"{x} {y} ")
#         f.write(f'" style="stroke:pink"/>')
#         f.write(f'</svg>\n')
    
  ################
  
  #GPT CODE TO GENERATE SVG OF ALL CHARACTERS EACH
  
# if not os.path.exists("svg_all"):
#       os.makedirs("svg_all")
#       for i, contour in enumerate(contours):
        
#       # Create an SVG element
#         svg_root = Element('svg')
#         svg_root.set('xmlns', 'http://www.w3.org/2000/svg')
#         # Create a path element for the contour
#         path_element = SubElement(svg_root, 'path')
#         path_data = ' '.join(['M{},{} '.format(point[0][0], point[0][1]) + ' '.join(['L{},{}'.format(p[0], p[1]) for p in point[1:]]) for point in contour])
#         path_element.set('d', path_data)
#         # Save the SVG file
#         svg_file_path = os.path.join(output_folder, f'character_{i}.svg')
#         with open(svg_file_path, 'w') as svg_file:
#             svg_file.write(minidom.parseString(tostring(svg_root)).toprettyxml(indent='  '))
            
################
# cv2.drawContours(img, contours, -1, (0, 255, 0), 3) 
# cv2.imshow('Contours', img) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 
# cv2.imwrite("contours.png", img) 

# # Create output folder for cropped characters
output_folder = 'cropped_characters'
os.makedirs(output_folder, exist_ok=True)
# boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
  b = b.split(' ')
  character = b[0]
  x , y , w , h = int(b[1]), int(b[2]), int(b[3]), int(b[4])    
  # Crop the character image
#   if is_within_bounds(x, y, w, h, wImg, hImg):
    
  im = edged[hImg-h:hImg-y , x:w]
    # imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # ret,thresh = cv2.threshold(imgray,127,255,0)
    # contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(thresh, contours, -1, (0,255,0), 3)

  # Save the cropped image in the output folder
  cv2.imwrite(os.path.join(output_folder, f'{character}.jpg'), im)


# 2 parts : do ocr to know bound boxes for each character. then do contour detection and store that image then crop that image according to bound boxes 

for b in boxes.splitlines():
  b = b.split(' ')
  
  character = b[0]
  x , y , w , h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
  print(x,y,w,h)
#   character_image = img[hImg - h:y, x:w]

  cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)  
  cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)
  
cv2.imshow('img', img)
cv2.waitKey(0)