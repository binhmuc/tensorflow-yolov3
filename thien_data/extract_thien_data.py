import os
import xml.etree.ElementTree as ET
import glob
classes = ["car"]


def convert_annotation(image_id, list_file):
    xml_path = os.path.join('.','Annotations/%s.xml'%(image_id))
    in_file = open(xml_path)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " +  " ".join([str(a) for a in b]) + " " + str(2))



list_file = open("labels.txt", 'w')
listImg = glob.glob("./IMG/*.jpg")
for img in listImg:
    image_id = img[6:-4]
    print(image_id)
    list_file.write('./thien_data' + img[1:])
    convert_annotation(image_id, list_file)
    list_file.write('\n')

#     list_file.write(image_path)
#     convert_annotation(year, image_id, list_file)
#     list_file.write('\n')
# list_file.close()