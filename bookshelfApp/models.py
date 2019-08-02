from django.db import models
from django_jalali.db import models as jmodels


class bookshelfs(models.Model):
     FRESHMAN = 'FR'
     SOPHOMORE = 'SO'
     JUNIOR = 'JR'
     SENIOR = 'SR'
     YEAR_IN_SCHOOL_CHOICES = [
          (FRESHMAN, 'Freshman'),
          (SOPHOMORE, 'Sophomore'),
          (JUNIOR, 'Junior'),
          (SENIOR, 'Senior'),
     ]
     name = models.CharField(
         max_length=30,
         choices=YEAR_IN_SCHOOL_CHOICES,

     )

    # ).only("first_name", "last_name")
    # name = models.CharField(max_length=30)

     publicationDate = jmodels.jDateField()
#     publicationDate = models.DateField()
     pageNumber = models.IntegerField()
     firstPublished = models.BooleanField()


     def __str__(self):
          return self.name

     def better_time(self):
          return self.publicationDate.strftime('%d-%m-%Y')

     def anotherDateFormat(self):
          return self.publicationDate.strftime('%b %d %Y ')

