def generate_local_uri(refuri="https://www.example.com"):
    """
    Generates a random valid URI using an input URI as a sort of prefix
    This allows the resulting URI to be somewhat recognizable and related
    to similar URI in the same viewed json file, but also obviously 'random'
    to be useful in a local context.
    
    Algorithm will take in a URI, strip off anything that looks like params, query,
    or fragment from a URL, and replace the last component of the path with
    a random string.
    
    Common use case for this is to generate URI for a canvas, annotation page
    which are local to a IIIF manifest, based on the manifest id, which is possibly
    also the URL from which the manifest is retrieved.
    """
    import urllib.parse,posixpath,uuid
    parts = urllib.parse.urlparse(refuri)
    newpath = posixpath.join( posixpath.dirname(parts.path), str(uuid.uuid4()))

    return urllib.parse.urlunparse(
        parts._replace( path=newpath,
                        params="",
                        query="",
                        fragment=""
                        )
    )