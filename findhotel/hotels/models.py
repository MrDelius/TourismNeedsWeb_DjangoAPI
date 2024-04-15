from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    search_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"id - {self.pk}, name - {self.name}"


class Need(models.Model):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='place_images/', null=True, blank=True)
    republic = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.CharField(max_length=255, null=True)
    rating = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    search_history = models.TextField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    saved_count = models.IntegerField(default=0)

    def __str__(self):
        return f"title - {self.title}, type - {self.type}"

    def num_likes(self):
        return self.userlikedneed_set.count()

    def num_views(self):
        return self.usersawneed_ser.count()


class UserLikedNeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} likes: {self.need.title}"


class UserCommentedNeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.name} commented on: {self.need.title}: {self.comment}"


class UserSawNeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} saw: {self.need.title}"


"""class Room(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    hotel = models.ForeignKey(Need, on_delete=models.CASCADE)


class Rental(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
"""
