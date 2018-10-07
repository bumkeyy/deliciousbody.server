from .models import Push


def push_task():
    Push.objects.all().push_check