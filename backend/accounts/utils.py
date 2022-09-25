
"""
This module defines a set of utility functions the account app
"""
import hashlib
import time
from .types import UserType


def user_profile_path(instance: UserType, filename: str) -> str:
    """
    returns the path for user profile image
    should always return a unique path
    """
    extension = filename.split(".").pop()
    directory_name = f"{instance.email}_{instance.pk}"
    hash = hashlib.md5(str(time.time()).encode()).hexdigest()
    return f"images/profile/{directory_name}/{hash}.{extension}"