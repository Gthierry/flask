import os
import glob

# exemple
# module/
#   user.py
#   product.py ['users','products']
# resultat =>


# on place la liste des fichiers py dans un tableau dans all
__all__ = [
    os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")
]
# imprime les chemins complets des fichiers py
print(
    [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
)
