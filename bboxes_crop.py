# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 上午10:16
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : bboxes_crop.py
# @Software: PyCharm

import os

from PIL import Image
import xml.etree.ElementTree as ET

count = 0

for filename in os.listdir("./Annotation"):
    basename = os.path.splitext(filename)[0]
    print("filename: ", filename)
    print("basename: ", basename)
    try:
        # file = open(os.path.join(Annotation, directory, basename))
        file = open("./Annotation/" + filename, "r")
        root = ET.fromstring(file.read())
        # dom = parseString(file.read())
        object_sum = len(root.find('object'))
        tree = ET.parse('./Annotation/' + filename)
        file.close()
        for object in range(object_sum):
            xmin = int(root.findall('object')[object].find('bndbox').find('xmin').text)
            ymin = int(root.findall('object')[object].find('bndbox').find('ymin').text)
            xmax = int(root.findall('object')[object].find('bndbox').find('xmax').text)
            ymax = int(root.findall('object')[object].find('bndbox').find('ymax').text)

            name_object = str(root.findall('object')[object].find('name').text)
            # img = Image.open(os.path.join(directory, filename))
            img = Image.open("./images/" + basename + ".jpg")
            cropped = img.crop((xmin, ymin, xmax, ymax))

            # save_file = open("./Cropped" + basename, 'w')
            # cropped.save("./Cropped/" + basename + "_" + name_object + "_" + str(object) + ".jpg")
            cropped.save("./Cropped/" + name_object + "_" + basename + "_" + str(object) + ".jpg")
            # save_file.close()
        count = count + 1


    except Exception as e:
        print("Unexpected error:", str(e))

print("process count: ", count)
