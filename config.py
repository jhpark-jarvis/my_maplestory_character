import os
import secrets
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)  # 32바이트의 랜덤한 시크릿 키 생성(64자리)
    