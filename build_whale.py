#! python


"""
The manifest generated in this script includes a SpecificResource with a selector
of type PointSelector specifying a 3D location. This PointSelector as of 1/3/2024
is not part of an IIIF API nor implemented in the iiif_prezi3 PyPI package.

This script requires importing a (development branch) of iiif_prezi3 which does allow
using the 3D form of point selector. Such an extension is available at 
git@github.com:vincentmarchetti/iiif-prezi3.git
branch kshell-main commit 9ea7c54
"""
label="Whale Cranium & Mandible"
manifest_name="whale.json"
manifest_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/manifests/20231220/" + manifest_name
model_id_cranium=  "https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/whale_cranium.glb"
model_id_mandible= "https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/whale_mandible.glb"

import iiif_prezi3 as pz
from kshell.iiif3d import *

ns = buildManifest(label, manifest_id)



for model_url, location in [
    (model_id_cranium,  (0.0, 0.15, -0.05)),
    (model_id_mandible, (0.0, 0.0,   0.0))
]:
    body  = buildBasicAnnotationBody(model_url,  GLB_MIMETYPE ).body
    
    x,y,z = location
    target = pz.SpecificResource(   id=generate_local_uri(ns.manifest.id),
                                    source=ns.canvas.id,
                                    selector={  "type": "PointSelector", 
                                                "x": x, 
                                                "y": y, 
                                                "z": z
                                              }
                                )
                    
    anno = pz.Annotation(id=generate_local_uri(ns.manifest.id),
                      motivation="painting",
                      body=body,
                      target=target)   
                  
    ns.anno_page.add_item(anno)

    
             
jsontext = ns.manifest.json(indent=2)

print(jsontext)
