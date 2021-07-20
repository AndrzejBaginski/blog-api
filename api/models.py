from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	email = models.EmailField(verbose_name='email', max_length=254, unique=True)
	phone = models.CharField(null=True, max_length=250)
	self_description = models.CharField(null=True, blank=True, max_length=500)
	user_pic = models.ImageField(upload_to="user_pics", default="default.png", height_field=None, width_field=None, max_length=None)

	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	@property
	def imageURL(self):
		try:
			url = 'http://127.0.0.1:7000/static' + self.user_pic.url
		except Exception:
			url = ''
		return url

	def __str__(self):
		return f'{self.id} {self.first_name} {self.last_name}'

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	title = models.CharField(max_length=100, null=False, blank=False, unique=True)
	content = models.CharField(max_length=2000, null=False, blank=False)
	image = models.ImageField(upload_to="post_pics", default="default.png", height_field=None, width_field=None, max_length=None)

	@property
	def imageURL(self):
		try:
			url = 'http://127.0.0.1:7000/static' + self.image.url
		except Exception:
			url = ''
		return url

	@property
	def number_of_likes(self):
		likes = self.postlike_set.all()
		return likes.count()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
	username = models.CharField(max_length=50, null=False, blank=False)
	content = models.CharField(max_length=2000, null=False, blank=False)

	@property
	def number_of_likes(self):
		likes = self.commentlike_set.all()
		return likes.count()

	def __str__(self):
		return f'{self.username} on  {self.post}'

class PostLike(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} likes {self.post}'

class CommentLike(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} likes {self.comment}'