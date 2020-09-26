from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #To use django authentication system
from django.urls import reverse #to get reverse
from PIL import Image #easy saving and manipulating of image 

class category (models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)

    def get_absolute_url(self): #this is needed so because the slug for each category is different, hence this is needed to specify the args for the url
        return reverse('category',args=[self.slug])

    def __str__(self):
        return self.category

class question (models.Model):
    title = models.CharField(max_length=100) #use charfield to limit user input
    liked_by = models.ManyToManyField(User,related_name='liked_by_question',blank = True)
    like = models.IntegerField(default=0)
    content = models.TextField() #use TextField if there is no limit for the content
    image = models.ImageField(upload_to="image",blank=True)
    date_published = models.DateTimeField(default=timezone.now) #auto-select the current time
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user is deleted the question will be deleted
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qna')

   

class comment(models.Model):
    post = models.ForeignKey(question,on_delete=models.CASCADE,related_name="comments")
    liked_by = models.ManyToManyField(User,related_name='liked_by',blank = True)
    like = models.IntegerField(default=0)
    r_token = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('qna')






    