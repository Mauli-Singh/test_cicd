import os
from django.utils import timezone
from apps.user.models import CustomUser
from apps.diary.models import DiaryNote

def create_sample_entries():
    user, created = CustomUser.objects.get_or_create(
        username="john_doe",
        email="john@example.com",
        date_of_birth="1990-01-01"
    )

    if created:
        user.set_password("password123")
        user.save()

    diary_entries = [
        {
            "title": "First Diary Entry",
            "description": "This is the description for the first diary entry.",
            "link_id": "link1",
            "author": user,
            "is_accepting_comments": True,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        },
        {
            "title": "Second Diary Entry",
            "description": "This is the description for the second diary entry.",
            "link_id": "link2",
            "author": user,
            "is_accepting_comments": True,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        },
        {
            "title": "Third Diary Entry",
            "description": "This is the description for the third diary entry.",
            "link_id": "link3",
            "author": user,
            "is_accepting_comments": True,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        }
    ]

    # Create diary entries
    for entry in diary_entries:
        DiaryNote.objects.create(**entry)

    print("Sample Diary Entries Created Successfully!")

#create_sample_entries()