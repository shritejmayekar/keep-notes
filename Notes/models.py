from django.db import models
from keepNotesAuth.models import User
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_pinned = models.BooleanField(default=False)
    is_archieved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=99)
    color = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ['-sort_order','-created_at']
        db_table ="keep_notes"

    def __str__(self):
        return self.title
