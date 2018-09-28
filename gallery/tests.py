from django.test import TestCase
from .models import Image, Category, Location, tags

# Create your tests here.
class ImageTestClass(TestCase):

    #setup method
    def setUp(self):
        naivasha = Location(name='naivasha')
        naivasha.save()
        cat = Category(name='flowers')
        cat.save()
        
        self.lilies= Image(image = 'jpg', image_name= 'lilies', image_description= 'flowers', image_location= naivasha,image_category=cat)
        self.lilies.save()

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lilies,Image))

    #save method
    def test_save_method(self):
        self.lilies.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #delete method
    def delete_image_method(self):
        self.lilies.save_image()
        self.lilies.delete_image()
        images = Image.objects.all()   
        self.assertTrue(len(images) == 0) 

    # retrieve all images
    def test_can_retrieve_all_images(self):
        self.lilies.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1) 

    #test update method
    # def test_can_update_images(self):
    #     self.lilies.save_image()
    #     cat = Image.objects.filter(image_name='Lilies').update(image_name= 'LILIES')
    #     fetch_cat = Image.objects.get(image_name='LILIES')
    #     self.assertEqual(fetch_cat.image_name,'LILIES')
       

class LocationTestClass(TestCase):
    def setUp(self):
        self.naivasha = Location(name = 'Naivasha')
       
    def test_save_method(self):
        self.naivasha.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    #delete method
    def delete_location_method(self):
        self.naivasha.save_location()
        self.naivasha.delete_location()
        locations = Location.objects.all()   
        self.assertTrue(len(locations) == 0)     

class CategoryTestClass(TestCase):
    def setUp(self):
       self.flowers = Category(name='flowers')

    #save method
    def test_save_method(self):
        self.flowers.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    #delete method
    def test_delete_method(self):
        self.flowers.save_category()
        self.flowers.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)     

    