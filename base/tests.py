 ##   <!--input type ='text' name="Chercher-sujet" value="{{ search_input }}">
 ##      <input type="submit" value="Chercher">
#</form> 

#<div class="task-items-wtrapper">
    ##   {% for task in tasks %}
 #   <div class="task-warapper">
  #      {% if task.complete %}
   #        <div class ="task-title">
    ##           <div class="task-complete-icon"></div>
      ##         <i><s><a href = "{% url 'task-update' task.id %}">{{ task }}</a></s></i>
  ##           </div>
      ##       </div>
          ##   </div>
 ##            </div>
     ##          <a class="Delete-link" href= "{% url 'task-delete' task.id %}" >&#215;</a>
  ##            </div>
 ##             </div>
  ##             {% else %}
  ##             <div class ="task-title">
  ##                <div class="task-incomplete-icon"></div>
  ##                <a href = "{% url 'task-update' task.id %}">{{ task }}</a>
   ##            <a class="Delete-link" href= "{% url 'task-delete' task.id %}" >&#215;</a>
   ##           {% endif %}


      ##     </div>
    ##   {% empty %}
    ##   <h3>No items in list</h3>
  ##     {% endfor %}


 ##  </div-->

    

class Karaté(Pestice):
    pass
class Blouz(Pestice):
    pass
class AG3(Pestice):
    pass
class Agrale(Pestice):
    pass
class Coperniko(Pestice):
    pass
class Confidor(Pestice):
              pass
class Valmec(Pestice):
    pass


class Joker(Pestice):
              pass
class Pixel(Pestice):
    pass
class Coperide(Pestice):
    pass
class Agrale(Pestice):
    pass
class Coperniko(Pestice):
    pass
class Mospelan(Pestice):
              pass
class Rodo(Pestice):
    pass

class Fozika(Pestice):
              pass
class Movento(Pestice):
    pass
class enfidor_speed(Pestice):
    pass
class Agrale(Pestice):
    pass
class Coperniko(Pestice):
    pass
class Mospelan(Pestice):
              pass
class Rodo(Pestice):
    pass


class Joker(models.Model):
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