from django.urls import path
from . import views
from .views import TutorialDetailView,TutorialListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name= 'tutorial-home'),
    path("tutorial/", login_required(TutorialListView.as_view()), name="tutorial"),
    path("tutorial/<int:pk>/", TutorialDetailView.as_view(), name='tutorial-detail'),
    path("search/", views.search),
    path("upload/notes/",views.upload,name='new-notes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)