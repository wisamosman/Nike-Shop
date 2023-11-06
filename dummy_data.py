import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



from faker import Faker
import random
from nike.models import Nike 





def seed_nike(n):
    fake = Faker()
    images = ['nike1.jpg','nike2.jpg','nike3.jpg','nike4.jpg','nike5.jpg','nike6.jpg','nike7.jpg','nike8.jpg',]
    

    for x in range(n):
        Nike.objects.create(
            name = fake.name() , 
            price = round(random.uniform(20.99,99.99),2) , 
            subtitle=fake.text(max_nb_chars=30) , 
            image = f'nike/{images[random.randint(0,7)]}',
            
        )
    print(f'{n} Product Was Created Successfuly ...')




seed_nike(300)