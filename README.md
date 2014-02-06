Tracking
========

Note : import

- Pour importer un package (comme histogram) tu dois rajouter ton dossier au sys.path:
<b>import sys
sys.path.append</b>

- Pour pouvoir importer des modules qui font partie de package (genre util dan histogram):
Rajouter dans le fichier __init__.py du package la ligne:
<b>import util</b>