from datetime import date
import uuid

def upload_post_image(instance, filename):
        ext = filename.split('.')[-1]
        return f"uploads/images/{date.today().strftime('%Y/%m/%d')}/img_{uuid.uuid4()}.{ext}"