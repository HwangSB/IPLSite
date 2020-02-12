from django.db import models


class Member(models.Model):
    objects = models.Manager()
    profile_image = models.ImageField(upload_to='member/profile_image')
    profile_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32, choices=[('0', 'Professor'), ('1', 'Lab Master'), ('2', 'Lab Manager'), ('3', 'Lab Member'), ('4', 'Graduate')])
    description = models.TextField()

    def __str__(self):
        return self.profile_name
