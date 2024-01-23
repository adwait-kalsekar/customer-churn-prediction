from django.db import models
import uuid

# Create your models here.

class Slide(models.Model):
    CATEGORY_TYPE = (
        ('intro', 'Introduction'),
        ('eda', 'Visualization'),
        ('clf', 'Classification'),
        ('clus', 'Clustering'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    slide_num = models.IntegerField(unique=True)
    image = models.ImageField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_TYPE)

    def __str__(self):
        return self.name
    
class Prediction(models.Model):
    GENDER_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    GEOGRAPHY_TYPE = (
        ('Spain', 'Spain'),
        ('Germany', 'Germany'),
        ('France', 'France'),
    )

    NUM_PROD = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    )

    CHOICE_TYPE = (
        ("1", "Yes"),
        ("0", "No"),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_TYPE)
    credit_score = models.IntegerField()
    geography = models.CharField(max_length=100, choices=GEOGRAPHY_TYPE)
    tenure = models.IntegerField()
    balance = models.IntegerField()
    num_of_prod = models.IntegerField(choices=NUM_PROD)
    has_cr_card = models.CharField(max_length=10, choices=CHOICE_TYPE)
    is_active = models.CharField(max_length=10, choices=CHOICE_TYPE)
    estimated_salary = models.IntegerField()
    prediction_1 = models.CharField(max_length=100)
    probability_1 = models.FloatField()
    prediction_2 = models.CharField(max_length=100)
    probability_2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name