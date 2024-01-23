from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
      uuid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
      created_at=models.DateTimeField(auto_now=True)
      update_at=models.DateTimeField(auto_now_add=True)

      class Meta:
            abstract=True