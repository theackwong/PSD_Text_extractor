from psd_tools import PSDImage
import json

image_location = "18CY1_Blade_Optane.JA_JP.psd"

psd_loaded = PSDImage.load(image_location)

psd_layers = psd_loaded.layers
extracted_text_info = {}

for group in psd_layers:
    if group.kind == "group":
        for group_layer in group.descendants():
            if group_layer.kind == "type":
                layer_info = {}

                print("Layer ID: " + str(group_layer.layer_id) +
                      "\nName: " + group_layer.name +
                      "\ntext: " + group_layer.text +
                      "\nheight: " + str(group_layer.height) +
                      "\nwidth: " + str(group_layer.width) +
                      "\nopacity: " + str(group_layer.opacity) + "\n")

                layer_info = { "layer_id": str(group_layer.layer_id),
                               "name" : group_layer.name,
                               "text" : group_layer.text,
                               "height" : group_layer.height,
                               "width" : group_layer.width,
                               "opacity" : group_layer.opacity}

                extracted_text_info[group_layer.layer_id] = layer_info


with open('data.json', 'w', encoding='utf-8') as output:
    json.dump(extracted_text_info, output, indent=4, ensure_ascii=False)