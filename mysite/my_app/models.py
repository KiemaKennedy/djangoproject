from django.db import models

# This is a search model in the admin.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

#stores the sought object with its name rather than search_object(1)
    def __str__(self):
        return '{}'.format(self.search)

#corrects the searchs in the admin to its plural
    class Meta:
        verbose_name_plural = 'Searches'