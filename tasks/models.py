from django.db import models
from django.core.exceptions import ValidationError

class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.is_archived and self.is_deleted:
            raise ValidationError('Only one of the two checkboxes can be checked (is_archived or is_deleted).')
        return super().clean()