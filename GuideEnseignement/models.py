from django.db import models

# Create your models here.
class Ville(models.Model):
    Nom=models.CharField(max_length=200)

    def __str__(self):
        return self.Nom
class Univérsite(models.Model):
    Nom=models.CharField(max_length=200)
    Adresse=models.CharField(max_length=200)
    Ville = models.ForeignKey(Ville,verbose_name="Ville", on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom
class TypeEtablissement(models.Model):
    Nom=models.CharField(max_length=200)

    def __str__(self):
        return self.Nom
class Etablissement(models.Model):
    Nom=models.CharField(max_length=200)
    Adresse=models.CharField(max_length=200)
    Ville = models.ForeignKey(Ville, verbose_name="Ville" , on_delete=models.CASCADE)
    Univérsite = models.ForeignKey(Univérsite, verbose_name="Univérsite", on_delete=models.CASCADE ,null=True,blank=True)
    lieu=models.CharField(max_length=200)
    TypeEtablissement = models.ForeignKey(TypeEtablissement,  verbose_name="TypeEtablissement",on_delete=models.CASCADE)
    Capacite=models.IntegerField
    Description=models.TextField(max_length=500)

    def __str__(self):
        return self.Nom
class Département(models.Model):
    Nom = models.CharField(max_length=200)
    Etablissement = models.ForeignKey(Etablissement,  verbose_name="Etablissement" ,on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom
class Bac(models.Model):
    Nom = models.CharField(max_length=2,unique=True)
    def __str__(self):
        return self.Nom
class BrancheL3(models.Model):
    Nom = models.CharField(max_length=200)

    def __str__(self):
        return self.Nom
class BrancheL2(models.Model):
    Nom = models.CharField(max_length=200)
    BrancheL3 = models.ForeignKey(BrancheL3, verbose_name="BrancheL3", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Nom
class Bac(models.Model):
    Nom = models.CharField(max_length=2,unique=True)
    def __str__(self):
        return self.Nom

class Filier(models.Model):
    Nom = models.CharField(max_length=200)
    Département = models.ForeignKey(Département, verbose_name="Département" , on_delete=models.CASCADE)
    Bac = models.ForeignKey(Bac,  verbose_name="Bac" ,on_delete=models.CASCADE)
    BrancheL2 = models.ForeignKey(BrancheL2, verbose_name="BrancheL2", on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.Nom

