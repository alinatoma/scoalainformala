#Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
#__init__ : instanțiem numărător și numitor
import math

class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        if numitor != 0:
            self.numitor = numitor
        else:
            raise ZeroDivisionError("Nu se poate divide la 0")

#__str__ : afisam "numărător/numitor"

    def __str__(self):
        return f"Fractia este: {self.numarator}/{self.numitor}"

#__add__ : returnam o noua fractie care reprezinta adunarea

    def __add__(self, adunare_fractie):
        add_numarator = self.numarator * adunare_fractie.numitor + self.numitor * adunare_fractie.numarator
        add_numitor = self.numitor * adunare_fractie.numitor
        gcd = math.gcd(add_numarator, add_numitor)
        if gcd > 1:
            add_numarator, add_numitor = add_numarator // gcd, add_numitor // gcd
        return Fractie(add_numarator, add_numitor)

#__sub__: returnam o nouă fracție care reprezinta scădearea

    def __sub__(self, scadere_fractie):
        sub_numarator = self.numarator * scadere_fractie.numitor - self.numitor * scadere_fractie.numarator
        sub_numitor = self.numitor * scadere_fractie.numitor
        gcd = math.gcd(sub_numarator,sub_numitor)
        if gcd > 1:
            sub_numarator, sub_numitor = sub_numarator // gcd, sub_numitor // gcd
        return Fractie(sub_numarator, sub_numitor)

#inverse: returnează o nouă fracție (inversa fracției)

    def inverse(self, numarator, numitor):
        self.numitor = numarator
        if numarator != 0:
            self.numarator = numitor
        else:
            raise ZeroDivisionError("Nu se poate divide la 0")
        return f"Fractia inversata este: {self.numarator}/{self.numitor}"

fractie = Fractie(0, 7)
print(fractie)

fractie_1 = Fractie(1, 3)
fractie_2 = Fractie(3, 6)

add_fraction = fractie_1 + fractie_2
print(add_fraction)

fractie_3 = Fractie(4, 2)
fractie_4 = Fractie(1, 2)

sub_fraction = fractie_3 - fractie_4
print(sub_fraction)

print(fractie.inverse(3, 5))
