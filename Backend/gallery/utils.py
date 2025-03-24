import uuid
from django.utils.text import slugify

def generate_custom_id(suffix):
    full_uuid = str(uuid.uuid4())
    uuid_part = f"{full_uuid[:8]}-{full_uuid[9:13]}"

    slugified_name = slugify(suffix)[:20]

    return f"{uuid_part}-{slugified_name}"
