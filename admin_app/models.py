from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Category"
    



class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'category')
        verbose_name_plural = "Sub Category"    




class Apps(models.Model):
    app_name = models.CharField(max_length=100)
    app_link = models.URLField(max_length=500)
    point = models.IntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.app_name
    
    class Meta:
        verbose_name_plural = "Apps"



