import os

class Config:
    SECRET_KEY = open("SECRET_KEY", "r").read().strip()