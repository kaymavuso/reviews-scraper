from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

# This function will be triggered for every new user
# the decorator is like calling post_save.connect(createdProfile, sender=User), see below
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    # print('we get to register signal createProfile')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        # Wasted 2 days because of this: //github.com/gitpod-io/gitpod/issues/965
        # subject = 'Welcome to the Brand Reviews Scraper'
        # message = 'We are glad you are here!'
        # print('about to send mail')

        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER, # this will somehow grab the users email
        #     [profile.email],
        #     fail_silently=False,
        # )
        # print('after sending mail')


# the decorator is like calling post_save.connect(updateUser, sender=Profile), see below
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# This function will be triggered for every profile deletion
# the decorator is like calling post_delete.connect(deleteUser, sender=Profile), see below
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

# post_save.connect(createProfile, sender=User)
# post_save.connect(updateUser, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)