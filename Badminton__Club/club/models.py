from django.db import models
import datetime
# Create your models here.

class Sponsers(models.Model):
  Image=models.ImageField(upload_to='static/icons')
  Link = models.CharField(max_length=500,blank=True,default="no link")


class EventsList(models.Model):
  Image = models.ImageField(upload_to='static/EventsGallery')
  Title = models.TextField(max_length=50)
  StartDate = models.DateTimeField(default=datetime.datetime.today())
  # EndDate = models.DateTimeField(default=datetime.datetime.today())
  Location = models.TextField(max_length=50,blank=True)
  Description = models.CharField(max_length=5000,blank=True)
  Description2 = models.CharField(max_length=300,blank=True)
  Register_Soon = models.TextField(max_length=30)
  Google_form = models.TextField(max_length=500)


  def __str__(self):
         return self.Title


class GalleryImages(models.Model):
  Image=models.ImageField(upload_to='static/images')
  EventName = models.TextField(max_length=50,default='all')
  EventDate = models.DateField(default=datetime.datetime.today())
  EventTitle = models.TextField(max_length=50,default='all')
  def __str__(self):
        return self.EventName
  
class GalleryHeadings(models.Model):
  heading = models.TextField(max_length=500)
  EventDate = models.DateField(default=datetime.datetime.today())
  def __str__(self):
        return self.heading


class TeamMembers(models.Model):
    Quote = models.TextField(max_length=100, blank=True, default="...")
    Image = models.ImageField(upload_to='static/images')
    Name = models.TextField(max_length=60)
    Position_and_Year_of_study = models.TextField(max_length=50)
    Twitter = models.CharField(max_length=500, blank=True, default="no link")
    Instagram = models.CharField(max_length=500, blank=True, default="no link")
    Linkedin = models.CharField(max_length=500, blank=True, default="no link")
    Year = models.TextField(max_length=50)

    def __str__(self):
        return self.Name

class TeamHeadings(models.Model):
    heading = models.TextField(max_length=50, blank=True)
    Date = models.DateField(default=datetime.datetime.today())
    def __str__(self):
        return self.heading

class AlumniMembers(models.Model):
    Quote = models.TextField(max_length=100, blank=True, default="...")
    Image = models.ImageField(upload_to='static/images')
    Name = models.TextField(max_length=60)
    Position_and_Year_of_study = models.TextField(max_length=50)
    Twitter = models.CharField(max_length=500, blank=True, default="no link")
    Instagram = models.CharField(max_length=500, blank=True, default="no link")
    Linkedin = models.CharField(max_length=500, blank=True, default="no link")
    Year = models.TextField(max_length=50)

    def __str__(self):
        return self.Name

class AlumniHeadings(models.Model):
    heading = models.TextField(max_length=50, blank=True)
    Date = models.DateField(default=datetime.datetime.today())
    def __str__(self):
        return self.heading

