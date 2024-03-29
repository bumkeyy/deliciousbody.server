from rest_framework.serializers import ModelSerializer
from .models import UserInfo


class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = UserInfo
        exclude = ('user', 'prev_video_id', 'next_video_id',
                   'weekdays_prev_hour', 'weekdays_next_hour',
                   'weekend_prev_hour', 'weekend_next_hour',
                   'weekdays_push_list', 'weekend_push_list',)




from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers

###### IMPORT YOUR USER MODEL ######
from django.contrib.auth.models import User

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm
    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        ###### FILTER YOUR USER MODEL ######
        if not User.objects.filter(email=value).exists():

            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),

            ###### USE YOUR TEXT FILE ######
            'email_template_name': 'message.txt',

            'request': request,
        }
        self.reset_form.save(**opts)