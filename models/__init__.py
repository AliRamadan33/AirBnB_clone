#!/usr/bin/python3
"""__init__ magic methods for models directorys"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
