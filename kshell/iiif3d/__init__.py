import iiif_prezi3 
iiif_prezi3.config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
del iiif_prezi3


"""
see https://www.iana.org/assignments/media-types/media-types.xhtml#model
    https://www.iana.org/assignments/media-types/model/gltf-binary
"""
GLB_MIMETYPE = "model/gltf-binary"

from .common import generate_local_uri
from .manifest3d import buildManifest
from .anno_body import buildBasicAnnotationBody