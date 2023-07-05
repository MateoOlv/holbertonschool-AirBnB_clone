#!/usr/bin/python3
"""Initalizes the main."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
