from django.db import models
from django.contrib.auth.models import User


class Push(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    push_list = models.CharField(max_length=500, default="1;1;1;1;2;2;2;2;3;3;3;3;4;4;4;4;5;5;5;5;6;6;6;6;7;7;7;7;8;8;8;8;9;9;9;9;10;10;10;10;11;11;11;11;12;12;12;12;13;13;13;13;14;14;14;14;15;15;15;15;16;16;16;16;17;17;17;17;18;18;18;18;19;19;19;19;20;20;20;20;21;21;21;21;22;22;22;22;23;23;23;23;24;24;24;24;")



