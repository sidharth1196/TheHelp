from django.db import models
from User.models import Worker, UserProfile

# Create your models here.

status_choice = (('Accepted', 'Accepted'),
                 ('In progress', 'In progress'),
                 ('Completed', 'Completed'),
                )

class Quote(models.Model):
    title = models.CharField(max_length=100)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    work_desc = models.TextField()
    charge = models.DecimalField(max_digits=6, decimal_places=2, default='0.0')
    modified_date = models.DateTimeField()
    start_date = models.DateTimeField()
    comments = models.TextField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Order(models.Model):
    title = models.CharField(max_length=100)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    completed_date = models.DateTimeField(blank=True, null = True)
    review = models.TextField(blank=True, null = True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default='0.0')
    status = models.CharField(max_length= 20, choices=status_choice)

    def __str__(self):
        return self.title