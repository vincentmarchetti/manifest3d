import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


from subprocess import Popen
import sys, os.path


manifest_entries = [
("Astronaut",    "astronaut.json",   "build_astronaut.py"),
("Archimedes",    "archimedes.json", "build_archimedes.py"),
("Saxaphone",     "saxophone.json",   "build_saxophone.py"),
("Nun's cell",    "nuns_cell.json",  "build_nuns_cell.py"),
("Venus de Milo", "venus.json"    ,  "build_venus.py"),
("Whale Skull",   "whale.json"    ,  "build_whale.py"),
]


for _, manifest_name, script_name in manifest_entries:
    commands = ["env", "PYTHONPATH=iiif-prezi3", sys.executable, script_name]
    outfile = os.path.join("./dist", manifest_name)
    message = "executing %s > %s" % ( str(commands), outfile)
    logger.info(message)
    with open(outfile,"w") as outf:
        res = Popen(commands, stdout=outf).wait()
