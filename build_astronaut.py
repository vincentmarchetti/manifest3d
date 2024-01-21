#! python

label="Astronaut"
manifest_name="astronaut.json"
manifest_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/manifests/20231220/" + manifest_name
model_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/astronaut.glb"

import iiif_prezi3 as pz
from kshell.iiif3d import *

ns = buildManifest(label, manifest_id)
ns.manifest.add_label("космонавт", "ru") # Russian
ns.manifest.add_label("宇航员" ,"zh-CN")  # simplified Chinese


bodyns = buildBasicAnnotationBody(model_id,  GLB_MIMETYPE )
                    
anno = pz.Annotation(id=generate_local_uri(ns.manifest.id),
                  motivation="painting",
                  body=bodyns.body,
                  target=ns.canvas.id)   
                  
ns.anno_page.add_item(anno)
               
jsontext = ns.manifest.json(indent=2)

print(jsontext)
