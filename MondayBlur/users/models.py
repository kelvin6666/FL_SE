from django.db import models
from django.contrib.auth.models import User
from QnA.models import comment
#a place to communicate with database
#tells how the data structure should be in db
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #make sure no duplicate username 
    image = models.ImageField(default="default.png", upload_to="profile_pics") #specify this is image
    
    def __str__(self):#make data in database readable 
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):#saves user profile
        super().save(*args, **kwargs)
                                                                                                                                                                                                                                                                                         
#database for points
class Reward(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    accu_quest_likes = models.IntegerField(default=0)
    accu_comment_likes = models.IntegerField(default=0)
    accu_rtoken = models.IntegerField(default=0)
    accu_quest_likes_percentage = models.FloatField(default=0)
    accu_comment_likes_percentage = models.FloatField(default=0)
    accu_rtoken_percentage = models.FloatField(default=0)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    








        


