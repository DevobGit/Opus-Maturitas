# Pour éditer ce fichier de manière agréable, plusieurs programmes existent, je
# vous conseille IDLE qui vient directement lors d'un installation de python
# via https://www.python.org/downloads/ mais vous pouvez aussi choisir d'autres
# solutions telles que PyCharm qui semble fonctionner très bien.

# Les lignes commençant par '#' ne sont pas interprétées par Python. Par
# ailleurs, voici deux conseils/règles de base:
# + n'écrivez pas de ligne avec plus que 79 caractères, cela aide à la lecture
# + commentez votre code, cela le rendra plus lisible

# Le but de ce fichier est de vous familiariser avec python. Une fois python
# (version >3.7) installé sur votre ordinateur, il vous sera possible
# d'exécuter ce fichier en tapant 'python vector.py' dans le terminal. Vous
# devrez ensuite compléter ce fichier en remplaçant tous les '...' par du code
# que vous écrirez afin de faire en sorte que le code ne retourne pas de
# message d'erreur. Travaillez étape par étape, modifiez une fonction à la
# fois. Si la fonction que vous avez écrite fonctionne, vous verrez un message
# de félicitation suivit du message d'erreur suivant. Lorsque vous ne voyez
# plus aucune erreur, c'est que vous avez codé le minimum requis.


# import utile pour calculer une racine carrée
from math import sqrt


# Définissions la classe Vector
class Vector:
    """
    Cette classe implémente les fonctions de base pour la manipulation de
    vecteur en deux dimensions.
    """
    # Le texte ci-dessus est une docstring, elle permet de documenter le code.
    # Cela est différent des commentaires car les docstring peuvent être
    # automatiquement utilisées pour générer une documentation similaire à
    # https://docs.python.org/3/library/math.html

    # Une méthode code qui accomplit une tache. Elle prend au miniminum
    # l'argument self et peut retourner quelque chose. Dans la définition
    # d'une méthode, il est souvent utile de noter quel type de variable est
    # demandé. Ici, la méthode __init__ attend deux arguments de nombres réels
    # (float) et ne retourne rien (None) Les méthodes dont le nom commence et
    # finit par '__' sont spéciales car elles ne doivent jamais être appelées
    # explicitement par l'utilisateur.
    def __init__(self, x: float, y: float) -> None:
        """
        Initialise les attributs de la classe. Elle est appelée automatiquement
        lorsque l'on écrit 'Vecteur(2,3)'.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x};{self.y})"

    # Les 5 méthodes ci-dessous sont aussi spéciales car elles sont appelées par
    # les opérateurs '+,-,-,*,=='.
    def __add__(self, other):
        """Retourne la somme entre le Vector self et le Vector other"""
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        """Retourne la différence entre le Vector self et le Vector other"""
        return Vector(self.x-other.x, self.y-other.y)

    def __neg__(self):
        """Retourne l'inverse du Vector self"""
        return Vector(- self.x , - self.y )

    def __mul__(self, a: float):
        """Retourne le produit entre un float et le Vector self"""
        return Vector(self.x * a , self.y * a)

    def __truediv__(self, a: float):
        """Retourne le quotient entre un float et le Vector self"""
        return Vector(self.x / a , self.y / a)

    # Astuce pour faire en sorte que 4*Vector(2,3) soit égal à Vector(2,3)*4
    __rmul__ = __mul__

    def __eq__(self, other) -> bool:
        """
        Test si le Vector self est égal au Vector other
        """
        if self.x == other.x and self.y == other.y :
            return True
        else :
            return False

    # Méthode qui peut être utilisée explicitement.
    def norm_squared(self) -> float:
        """
        Retourne la norme au carré du Vector self
        """
        return self.x ** 2 + self.y ** 2

    # Pour calculer la norme, lisez le site web référencé ci-dessus afin
    # d'importer le module math et d'utiliser la fonction sqrt.
    def norm(self) -> float:
        #return sqrt(self.norm_squared) ????????
        return sqrt(self.x ** 2 + self.y ** 2)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y


# Une fonction est différente d'une méthode car elle n'appartient pas à une
# classe. En effet, une méthode est une fonction de classe et prend donc un
# argument supplémentaire 'self'. Comme une fonction n'appartient pas à une
# classe, elle ne prend jamais d'argument 'self' mais peut prendre d'autres
# arguments.
def test_vector() -> None:
    """
    Teste que la classe Vector est correctement implémentée. Elle ne prend
    aucun argument et ne retourne rien.

    Ne modifiez rien dans cette fonction!
    """
    print("Bravo, vous savez excuter ce programme")

    a = Vector(4, 2)
    b = Vector(3, -5)
    assert a.x == 4
    assert a.y == 2
    assert b.x == 3
    assert b.y == -5
    print("Bravo, vous avez correctement définit, la méthode __init__")

    c = a+b
    assert c.x == 7
    assert c.y == -3
    print("Bravo, vous savez additionner deux Vector")

    d = a-b
    assert d.x == 1
    assert d.y == 7
    print("Bravo, vous savez soustraire deux Vector")

    e = -d
    assert e.x == -1
    assert e.y == -7
    print("Bravo, vous savez inverser un Vector")

    f = 3*a
    assert f.x == 12
    assert f.y == 6

    g = a*3
    assert g.x == 12
    assert g.y == 6
    print("Bravo, vous savez multiplier un Vector par un réel")

    h = a/2.0
    assert h.x == 2
    assert h.y == 1
    print("Bravo, vous savez diviser un Vector par un réel")

    assert f == g
    print("Bravo, vous savez vérifier si deux Vectors sont égaux")

    assert f.norm_squared() == 180
    print("Bravo, vous savez calculer le carré de la norme d'un Vector")

    i = Vector(3, 4)
    assert i.norm() == 5
    print("Bravo, vous savez calculer la norme d'un Vector")

    # Pour le produit scalaire, vous devez vous même définir la méthode 'dot'
    assert a.dot(b) == 2
    print("Bravo, vous savez calculer le produit scalaire de deux Vector")


if __name__ == "__main__":
    test_vector()