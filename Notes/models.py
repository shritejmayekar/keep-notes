from django.db import models
from keepNotesAuth.models import User
# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_pinned = models.BooleanField(default=False)
    is_archieved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    

    class Meta:
        verbose_name="Note"
        verbose_name_plural="Notes"

    def __str__(self):
        return self.title
