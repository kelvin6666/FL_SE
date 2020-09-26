from django.shortcuts import render

from django.utils.safestring import mark_safe
import json
# Create your views here.
def index(request): #Takes request and return to index.html
    return render(request, 'chat/index.html', {})

def room(request, room_name): # Takes request and return to room.html
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })