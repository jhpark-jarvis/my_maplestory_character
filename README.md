# my_maplestory_character
내 메이플스토리 캐릭터 정리(Flask)

```bash
my_maplestory_character/
├── app.py                    # 또는 run.py - 앱 시작점
├── requirements.txt
├── maple_app/
│   ├── __init__.py          # Flask 앱 기본화
│   ├── models.py            # DB 모델 (SQLAlchemy)
│   ├── data.py              # 데이터 처리
│   ├── routes/              # 라우트 분리
│   │   ├── __init__.py
│   │   ├── home.py
│   │   └── api.py
│   ├── templates/           # HTML 템플릿
│   │   ├── base.html
│   │   └── home.html
│   └── static/              # CSS, JS, 이미지
│       ├── css/
│       ├── js/
│       └── images/
├── migrations/              # Flask-Migrate (DB 버전 관리)
└── config.py               # 환경 설정
```
