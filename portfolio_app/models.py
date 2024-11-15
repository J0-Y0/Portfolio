from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_image_file(value):
    allowed_extensions = [".svg", ".png", ".jpg", ".jpeg"]
    allowed_mime_types = ["image/svg+xml", "image/png", "image/jpeg"]

    # Check file extension
    ext = os.path.splitext(value.name)[1]  # Extracts the file extension
    if ext.lower() not in allowed_extensions:
        raise ValidationError(
            f"Unsupported file format. Allowed types: {', '.join(allowed_extensions)}"
        )

    # Check MIME type if content_type is available
    if hasattr(value, "content_type") and value.content_type not in allowed_mime_types:
        raise ValidationError("Invalid image type.")


class Profile(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    heading = models.CharField(max_length=255)  # heading to your landing page
    sub_heading = models.CharField(max_length=255)  # heading to your profile
    about = models.TextField()

    def __str__(self):
        return "About Me"


class Address(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(
        max_length=100, blank=True, null=True
    )  # optional if you dont want to specify region
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"


class SocialLink(models.Model):
    social_media_name = models.CharField(max_length=50)
    your_address = models.CharField(unique=True, max_length=255)
    logo = models.FileField(
        upload_to="social_logos/",
        validators=[validate_image_file],
    )  # Ensure you have Pillow installed

    def __str__(self):
        return self.social_media_name


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=300)
    address = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Certifications(models.Model):
    title = models.CharField(max_length=200, null=False)
    issued_by = models.CharField(max_length=255, null=False)
    issued_on = models.DateField()
    certificate_link = models.URLField()


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField()
    problem_statement = models.TextField(null=True, blank=True)  # optional
    tags = models.ManyToManyField("Tag", related_name="projects")
    skills_used = models.ManyToManyField("Skill", related_name="projects")
    explored = models.TextField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField("Tag", related_name="skills")
    logo = models.FileField(
        upload_to="skill_logos/",
        validators=[validate_image_file],
        null=True,
        blank=True,
    )  # Ensure you have Pillow installed

    description = models.TextField(null=True, blank=True)  # "What I have done with it"

    def __str__(self):
        return self.name


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    publisher = models.CharField(max_length=100)  # Optional
    tags = models.ManyToManyField("Tag", related_name="blogs")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
