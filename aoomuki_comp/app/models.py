from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profil(models.Model):
    name = models.CharField('nom',max_length=200, unique=True)
    description = models.CharField('description',max_length=200, unique=True)
    administrateur = models.BooleanField('administrateur ?',default=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Profils"

class User(models.Model):
    Lastname = models.CharField('nom',max_length=200, unique=True)
    Firstname = models.CharField('prénom',max_length=200, unique=True)
    login = models.CharField('login',max_length=200, unique=True)
    password = models.CharField(max_length=50)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Lastname
    class Meta:
        verbose_name = "Utilisateurs"


class Collaborater(models.Model):
    Lastname = models.CharField('nom',max_length=200, unique=True)
    Firstname = models.CharField('prénom',max_length=200, unique=True)
    Extern = models.BooleanField('externe ?',default=False)
    Society = models.CharField('société',max_length=200, unique=True)
    def __str__(self):
        return self.Lastname
    class Meta:
        verbose_name = "Collaborateurs"

class ListLevel(models.Model):
    value = models.CharField('valeur', max_length=10, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=True)
    def __str__(self):
        return self.value
    class Meta:
        verbose_name = "Liste des niveaux"

class ListInterest(models.Model):
    value = models.CharField('valeur', max_length=10, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=True)
    def __str__(self):
        return self.value
    class Meta:
        verbose_name = "Liste des intérêts"

class ListWorkStation(models.Model):
    name = models.CharField('nom', max_length=50, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Liste postes de travail"

class Field(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    description = models.CharField('description', max_length=250, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Domaine"

class Competence(models.Model):
    name = models.CharField('nom', max_length=50, unique=False)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, default=1)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Compétences"

# class LinkCollaborateurCompetence(models.Model):
#     former = models.BooleanField('formateur ?',default=False)
#     collaborater = 
#     level = 
#     interest = 
#     competence = 
#     def __str__(self):
#         return self.collaborateur
#     class Meta:
#         verbose_name = "liens collaborateurs / compétences"
