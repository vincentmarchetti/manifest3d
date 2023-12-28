#! python

label="Whale Cranium & Mandible"
manifest_name="whale.json"
manifest_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/manifests/20231220/" + manifest_name
model_id_1="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/whale_cranium.glb"
model_id_2="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/whale_mandible.glb"

import iiif_prezi3 as pz
from kshell.iiif3d import *

ns = buildManifest(label, manifest_id)



bodyns = buildBasicAnnotationBody(model_id_1,  GLB_MIMETYPE )
                    
anno = pz.Annotation(id=generate_local_uri(ns.manifest.id),
                  motivation="painting",
                  body=bodyns.body,
                  target=ns.canvas.id)   
                  
ns.anno_page.add_item(anno)
               
jsontext = ns.manifest.json(indent=2)

print(jsontext)
