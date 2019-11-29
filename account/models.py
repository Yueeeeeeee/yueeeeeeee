from django.db import models
from django.contrib.auth.models import User
from hashlib import md5

# Create your models here.
class Contact(models.Model):

    user_following = models.ForeignKey(
        to=User,
        related_name='following_set',
        on_delete=models.CASCADE
    )
    user_followed = models.ForeignKey(
        to=User,
        related_name='followed_set',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(
            self.user_following, self.user_followed
        )

def gravatar(self, size=80):
    md5_digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(md5_digest, size)

User.add_to_class(
    'gravatar',
    gravatar
)

User.add_to_class(
    'following',
    models.ManyToManyField(
        to=User,
        through=Contact,
        related_name='followers',
        symmetrical=False
    )
)