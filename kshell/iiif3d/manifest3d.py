
import iiif_prezi3  as pz

from .common import generate_local_uri



def buildManifest(label, manifest_id):
    """
    build and return a simple IIIF manifest structure which has a manifest and
    the required label value, manifest has a single canvas, canvas a single AnnotationPage
    
    
    
    
    returns an instance of SimpleNamespace with attributes
    manifest, canvas, anno_page
    typical usage will be:
    
    ns = build3DManifest(....)
    mycanvas = ns.canvas     # mycanvas an instance of iiif_prezi3.Canvas
    mymanifest = ns.manifest # mymanifest an instance of iiif_prezi3.Manifest
    mypage = ns.anno_page    # mypage an instance of iiif_prezi3.AnnotationPage
    
    Simple manifest structure follows the IIIF Cookbook:
    https://iiif.io/api/cookbook/recipe/0001-mvm-image/
    python code: https://iiif-prezi.github.io/iiif-prezi3/recipes/0001-mvm-image/
    """
    from types import SimpleNamespace
    
    manifest = pz.Manifest(id = manifest_id, label = label)
    canvas = pz.Canvas(id = generate_local_uri(manifest_id), width=32, height=32)
    anno_page = pz.AnnotationPage(id=generate_local_uri(manifest_id))
    manifest.add_item(canvas)
    canvas.add_item(anno_page)
    return SimpleNamespace(
        canvas=canvas,
        anno_page=anno_page,
        manifest=manifest
    )