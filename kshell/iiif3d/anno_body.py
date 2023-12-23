
import iiif_prezi3  as pz

def buildBasicAnnotationBody(model_id, mimetype):
    """
    based on the prototype at https://github.com/IIIF/3d/blob/main/manifests/basel-october-2023/model_origin.json
    added a mimetype value
    """
    from types import SimpleNamespace
    
    retVal = SimpleNamespace()
    retVal.body = pz.ResourceItem(  id=model_id,
                                    type="Model",
                                    format= mimetype )
    return retVal