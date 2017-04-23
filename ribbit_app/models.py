from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.

class Ribbit(models.Model):
	content = models.CharField(max_length=140)
	user = models.ForeignKey(User)
	creation_date = models.DateTimeField(auto_now=True, blank=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
	# symmetrical=False so that, if User A follows B then User B doesn't automatically follow A

	def gravatar_url(self):
		return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
