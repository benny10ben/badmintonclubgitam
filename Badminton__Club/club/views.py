from django.shortcuts import render
from .models import Sponsers, EventsList, GalleryImages, GalleryHeadings, TeamMembers, TeamHeadings, AlumniMembers, AlumniHeadings
import datetime
# Create your views here.

def  home(request):
    sponsers = Sponsers.objects.all()
    eventslist = EventsList.objects.all().order_by('StartDate')
    context = {'sponsers': sponsers, 'eventslist':eventslist}
    return render(request,'club/home.html', context)


def Events(request):
    eventslist = EventsList.objects.all().order_by('-StartDate')
    context = {'eventslist':eventslist}
    return render(request,'club/Events.html', context)


def Gallery(request):
    galleryimages = GalleryImages.objects.all().order_by('-EventDate')
    galleryheadings = GalleryHeadings.objects.all().order_by('-EventDate')
    context = {'galleryimages':galleryimages,'galleryheadings':galleryheadings}
    return render(request,'club/Gallery.html', context)


def  Team(request):
    teammembers = TeamMembers.objects.all()
    teamheadings = TeamHeadings.objects.all().order_by('Date')
    alumnimembers = AlumniMembers.objects.all()
    alumniheadings = AlumniHeadings.objects.all().order_by('-Date')
    context = {'teammembers': teammembers, 'teamheadings':teamheadings, 'alumnimembers': alumnimembers, 'alumniheadings':alumniheadings}
    return render(request,'club/Team.html', context)

