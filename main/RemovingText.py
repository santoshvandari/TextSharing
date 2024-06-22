from pathlib import Path
import os
from core.settings import BASE_DIR
from main.models import SharedText


# Remove all the Expired Files 
def RemoveAllExpiredFiles():
    texts=SharedText.objects.all()
    for text in texts:
        if file.is_expired():
            file.delete()
    return True
