import re
from psd_tools import PSDImage
import pytoshop
image_location = "18CY1_Blade_Optane.JA_JP.psd"

psd_loaded = PSDImage.load(image_location)

layer = psd_loaded.layers[1]

#psd.print_tree()
for layeres in layer.descendants():
    if layeres.kind == "type":
        print("ID: " + str(layeres.layer_id) +
              "\nName: " + layeres.name +
              "\ntext: " + layeres.text +
              "\nheight: " + str(layeres.height) +
              "\nwidth: " + str(layeres.width) +
              "\nopacity: " + str(layeres.opacity))
        #print(layeres.engine_data)

with open(image_location, 'rb') as fd:
    psd = pytoshop.read(fd)
    print(psd.layer_and_mask_info.layer_info.layer_records[12].name)
    for layerRecord in psd.layer_and_mask_info.layer_info.layer_records:
        #decoded = pytoshop.util.decode_unicode_string(layerRecord.name)
        print(layerRecord.name + " ")
        if layerRecord.name == "第 8 世代インテル® Core™ プロセッサー":
            print("test")