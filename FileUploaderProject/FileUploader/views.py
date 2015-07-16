from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

#import models and forms
from FileUploader.models import Image
from FileUploader.forms import ImageUploadForm

#imported static for debugging purposes
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.

#this view will respond to file uploads
def index(request):
    print("View loaded")
    if request.method =='GET':
        print("request method is GET! " + str(request))
    if request.method =='POST':
        print("request method was POST")
        #create a form from the model I made
        form = ImageUploadForm(request.POST, request.FILES)
        #check form contains no errors
        if form.is_valid():
            #create a new image and save it! file param must be name of attribute in ImageUploadForm
            newImage = Image(imageFile = request.FILES['imageFile'])
            newImage.save()
            #redirect to success page!
            return HttpResponseRedirect('/image/')
    else:
            #create an empty form if it failed
            form = ImageUploadForm()

    #render the page and pass the dictionary to the view
    #changed render_to_response to render as documentation states it also returns a RequestContext by default
    return  render(request, 'index.html', {'form': form})

def images(request):
    #debugging
    #retrieve all uploaded images.
    #Image.delete()
    images = Image.objects.all()
    return render(request, 'images.html', {'images': images})
