from django.db import models
from kbspre.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):
    """ Image Model """
    #id = THIS USER ID
    id = 1
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    ''' 
    comment_set
    comment_set = (LOOK IN ALL THE COMMENTS FOR THE ONES THAT HAVE 'IMAGE' = 1)
    image_set = (LOOK IN ALL THE COMMENTS FOR THE ONES THAT HAVE 'IMAGE' = THIS IMAGE ID)
    comment_set = (LOOK IN ALL THE COMMENTS FOR THE ONES THAT HAVE 'IMAGE' = THIS IMAGE ID)
    like_set = (LOOK IN ALL THE COMMENTS FOR THE ONES THAT HAVE 'IMAGE' = THIS IMAGE ID)
    '''
    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampedModel): 
    """ Comment Model """
    message = models.TextField(null=True)

    playername = models.TextField(null=True)
    score = models.IntegerField(null=True)
    tel = models.TextField(null=True)
    survey = models.IntegerField(null=True)
    note = models.TextField(null=True)
    step = models.IntegerField(null=True)
    mail = models.TextField(null=True)

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True,related_name='comments')

    def __str__(self):
        #return self.score
        #return self.step
        return self.playername
        return self.tel
        return self.mail
        #return self.survey
        return self.note
        return self.message

    class Meta:
        ordering = ['-created_at']

class Like(TimeStampedModel):
    """ Like Model """
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True,related_name='likes')
    
    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)