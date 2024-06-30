from pathlib import Path
import os
from core.settings import BASE_DIR
from main.models import SharedText


# Remove all the Expired Files 
def RemoveAllExpiredFiles():
    texts=SharedText.objects.all()
    for text in texts:
        if text.is_expired():
            text.delete()
    return True
