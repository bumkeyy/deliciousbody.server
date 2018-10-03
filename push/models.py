from django.db import models
from django.contrib.auth.models import User
from userinfo.models import UserInfo


class Push(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekdays_push_list = models.CharField(max_length=500)
    weekend_push_list = models.CharField(max_length=500)
    is_check = models.BooleanField(default=False)
    next_hour = models.IntegerField()


    def save(self, *args, **kwargs):
        if not self.pk:
            weekdays_start = UserInfo.objects.filter(user=self.user).values_list('weekdays_start', flat=True).get(pk=1)
            weekdays_end = UserInfo.objects.filter(user=self.user).values_list('weekdays_end', flat=True).get(pk=1)
            weekend_start = UserInfo.objects.filter(user=self.user).values_list('weekend_start', flat=True).get(pk=1)
            weekend_end = UserInfo.objects.filter(user=self.user).values_list('weekend_end', flat=True).get(pk=1)

            weekdays_list = list()
            weekend_list = list()
            for i in range(weekdays_start, weekdays_end + 1):
                weekdays_list.append(i)
                weekdays_list *= 5
            for i in range(weekend_start, weekend_end + 1):
                weekend_list.append(i)
                weekend_list *= 5
            self.weekdays_push_list = str(weekdays_list)
            self.weekend_push_list = str(weekend_list)
        super(Push, self).save(*args, **kwargs)
















