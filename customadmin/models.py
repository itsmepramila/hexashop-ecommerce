from django.db import models


# Create your models here.
class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=100, null=True)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500, null=True)
    Sitefacebooklink = models.CharField(max_length=300, null=True)
    Sitetwitterlink = models.CharField(max_length=300, null=True)
    Siteinstagramlink = models.CharField(max_length=300, null=True)
    Sitelinkdinlink = models.CharField(max_length=300, null=True)
    logo = models.ImageField(
        upload_to="Global/", max_length=200, null=True, default=None
    )
    brochure = models.FileField(upload_to="brochure/", null=True)
    brochure_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.SiteName


class Navigation(models.Model):
    PAGE_TYPE = (
        ("Home", "Home"),
        ("Group", "Group"),   
        
    )

    STATUS = (("Publish", "Publish"), ("Draft", "Draft"))
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(
        choices=PAGE_TYPE, null=True, blank=True, max_length=50
    )
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    short_desc1 = models.TextField(default="")
    short_desc2 = models.TextField(default=" ")
    short_desc3 = models.TextField(default="")
    desc = models.TextField(null=True)
    banner_image = models.ImageField(upload_to="about/", null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    slider_image = models.ImageField(upload_to="about/", null=True)
    Parent = models.ForeignKey(
        "self", related_name="childs", on_delete=models.CASCADE, null=True, blank=True
    )
    brochure = models.FileField(upload_to="brochure/", null=True)
    
    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.name


