from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=255, default='example@example.com')
    phone_no = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True, help_text="Enter the full address")

    def __str__(self):
        return "%s %s %s %s %s" % (self.first_name, self.last_name, self.phone_no, self.email_id, self.address)
