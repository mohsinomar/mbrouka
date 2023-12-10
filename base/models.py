from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domaine=models.CharField(max_length=50,blank=False,null=True)
    Parcelle = models.CharField(max_length=50, blank=True, null=True)
    Varieté=models.CharField(max_length=50, blank=True, null=True)                                                 
    Secteur= models.CharField(max_length=50, blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Parcelle
    class Meta:
        ordering = ['complete']

class Fertigation(models.Model):
    cat_choice = (
        ('Ammonitrate', 'Ammonitrate'),
      	('Sulfat_potasse', 'Sulfat_potasse'),
      	('MAP', 'MAP'),
        ('Nitrat_potasse', 'Nitrat_potasse'),
      	('Calcium', 'Calcium'),
      	('Complet', 'Complet'),
        ('Acide', 'Acide'),
        ('Sequestrine', 'Sequestrine'),
        ('Uree_46', 'Uree_46'),
        ('Kimia', 'Kimia'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domaine=models.CharField(max_length=50,blank=False,null=True)
    date=models.CharField(max_length=50,blank=False,null=True)
    ammonitrate=models.IntegerField(blank=True,null=True)
    map=models.IntegerField(blank=True,null=True)
    sulfate=models.IntegerField(blank=True,null=True)
    calcium=models.IntegerField(blank=True,null=True)
    case1=models.IntegerField(blank=True,null=True)
    case2=models.IntegerField(blank=True,null=True)
    organique=models.IntegerField(blank=True,null=True)
    qté_eau=models.IntegerField(blank=True,null=True)
    dure_irr=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.domaine
###############################################################################

class Fertile(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domaine=models.CharField(max_length=50,blank=False,null=True)
    date=models.CharField(max_length=50,blank=False,null=True)
    s_initial=models.IntegerField(blank=True,null=True)
    entree=models.IntegerField(blank=True,null=True)
    sortie=models.IntegerField(blank=True,null=True)
    destination=models.CharField(max_length=50,blank=True,null=True)
    s_restant=models.IntegerField(blank=True,null=True) 

    def __str__(self):
                  return self.domaine
    

class Amon(Fertile):
    pass
class Map(Fertile):
    pass
class Sulf(Fertile):
    pass
class Calc(Fertile):
    pass
class Nitr(Fertile):
    pass
class Uree(Fertile):
              pass
class Kimia(Fertile):
    pass

class Phytos(models.Model):
    phytos_choice = (
    ('Karaté', 'Karaté'),
  	('Blouz', 'Blouz'),
  	('AG3', 'AG3'),
    ('Agrale', 'Agrale'),
  	('Coperniko', 'Coperniko'),
  	('Confidor', 'Confidor'),
    ('Valmec', 'Valmec'),
    ('Joker', 'Joker'),
    ('Pixel', 'Pixel'),
    ('Coperide', 'Coperide'),
    ('Mospelan', 'Mospelan'),
    ('Rodo', 'Rodo'),
    ('Fozika', 'Fozika'),
    ('Movento', 'Movento'),
    ('enfidor-speed', 'enfidor-speed'),
    ('Magnome', 'Magnome'),
    ('Samba', 'Samba'),
    ('Fozika_ca', 'Fozika_ca'),
    ('Soufre', 'Soufre'),
    ('Nissorun', 'Nissorun'),
    ('Tridicorp Jaguar', 'Tridicorp Jaguar'),
    ('Twinteck zin+mn', 'Twinteck zin+mn'),
    ('Fengib', 'Fengib'),
    ('Ariatox', 'Ariatox'),
    ('Kimia', 'Kimia'),
    ('Proximo', 'Proximo'),
    )
    variete_choice = (
    ('Nules', 'Nules'),
  	('Bruno', 'Bruno'),
    ('Orograndé', 'Orograndé'),
    ('Clémentine','Clémentine'),
  	('Nour', 'Nour'),
    ('Laarache', 'Laarache'),
    ('Nadorcott', 'Nadorcott'),
  	('Navel', 'Navel'),
    ('Maroc_late', 'Maroc_late'),
    ('Salustiana', 'Salustiana'),
    ('Citron', 'Citron'),    
    ('W.sanguine', 'W.sanguine'),
    ('Pomelo', 'Pomelo'),

)
    outiel_choice=(
       ('citerne_atomiseur', 'citerne_atomiseur'),
  	('citerne_manuelle', 'citerne_manuelle'),
    ('citerne_a_dos', 'citerne_a_dos'),  
    )
    meteo_choice=(
    ('calme', 'calme'),
    ('vent', 'vent'),
  	('nuage', 'nuage'),
    ('pluie', 'pluie'),  
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domaine=models.CharField(max_length=50,blank=False,null=True)
    date=models.CharField(max_length=50,blank=False,null=True)
    varieté=models.CharField(max_length=50, blank=False,choices=variete_choice)
    parcelle=models.CharField(max_length=50,blank=False,null=True)
    horaire=models.CharField(max_length=50,blank=False,null=True)
    produit=models.CharField(max_length=50, blank=False,choices=phytos_choice)
    matiére_avtive=models.CharField(max_length=50,blank=False,null=True)
    ennemi_ciblé=models.CharField(max_length=50, blank=True)
    qté_produits=models.CharField(max_length=50, blank=False)
    outiel=models.CharField(max_length=50, blank=False,choices=outiel_choice)
    ouvries=models.CharField(max_length=50, blank=False)
    temperature=models.CharField(max_length=50, blank=False)
    météo=models.CharField(max_length=50, blank=False,choices=meteo_choice)

    def __str__(self):
                  return self.domaine
    


class Pestice(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domaine=models.CharField(max_length=50,blank=False,null=True)
    date=models.CharField(max_length=50,blank=False,null=True)
    s_initial=models.IntegerField(blank=True,null=True)
    entree=models.IntegerField(blank=True,null=True)
    sortie=models.IntegerField(blank=True,null=True)
    destination=models.CharField(max_length=50,blank=True,null=True)
    s_restant=models.IntegerField(blank=True,null=True) 

    def __str__(self):
                  return self.domaine


class Userpassword(models.Model):
            username=models.CharField(max_length=255)  
            password=models.CharField(max_length=255)


class OrderEng(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    producteur=models.CharField(max_length=50,blank=False,null=True)
    date1=models.CharField(max_length=50,blank=False,null=True)
    date2=models.CharField(max_length=50,blank=False,null=True)
    amm=models.IntegerField(blank=True,null=True)
    map=models.IntegerField(blank=True,null=True)
    sulf=models.IntegerField(blank=True,null=True)
    nitr=models.CharField(max_length=50,blank=True,null=True)
    calc=models.IntegerField(blank=True,null=True) 
    champ=models.CharField(max_length=50,blank=False,null=True)
    def __str__(self):
                  return self.producteur           
       
            










