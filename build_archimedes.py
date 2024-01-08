#! python

label="Archimedes"
manifest_name="archimedes.json"
manifest_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/manifests/20231220/" + manifest_name
model_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/archimedes9.glb"
comment_id="https://spri-open-resources.s3.us-east-2.amazonaws.com/iiif3dtsg/assets/archimedes_theorem.x3d"

import iiif_prezi3 as pz
from kshell.iiif3d import *

ns = buildManifest(label, manifest_id)



bodyns = buildBasicAnnotationBody(model_id,  GLB_MIMETYPE )
                    
anno = pz.Annotation(id=generate_local_uri(ns.manifest.id),
                  motivation="painting",
                  body=bodyns.body,
                  target=ns.canvas.id)   
                  
ns.anno_page.add_item(anno)

commentns =  buildBasicAnnotationBody(comment_id,  X3D_MIMETYPE ) 

x,y,z = (0.0, 6.0, 0.0)
target = pz.SpecificResource(   id=generate_local_uri(ns.manifest.id),
                                    source=ns.canvas.id,
                                    selector={  "type": "PointSelector", 
                                                "x": x, 
                                                "y": y, 
                                                "z": z
                                              }
                                )
 
# see the IIIF Presentation 3.0 API, Section 3.5, for
# allowed values of the motivation field in IIIF annotations                               
anno = pz.Annotation(id=generate_local_uri(ns.manifest.id),
                  motivation="supplementing",
                  body=commentns.body,
                  target=target) 
 
ns.anno_page.add_item(anno)
                              
jsontext = ns.manifest.json(indent=2)

print(jsontext)
