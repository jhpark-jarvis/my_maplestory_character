# my_maplestory_character

Nexon Open API를 이용하여 내 메이플스토리 계정의 모든 캐릭터 정보를 한눈에 볼 수 있는 Flask 기반 웹 애플리케이션입니다.

## 프로젝트 구조

```
my_maplestory_character/
├── app.py                          # 앱 진입점 (설정 및 실행)
├── config.py                       # 환경 설정 (SECRET_KEY 등)
├── requirements.txt                # 의존성 패키지
├── README.md
├── API_KEY.txt                     # API 키 저장 (git에서 제외)
│
├── maple_app/                      # Flask 애플리케이션 패키지
│   ├── __init__.py                 # 앱 초기화 및 Blueprint 등록
│   ├── data.py                     # 데이터 처리 유틸리티 (레거시)
│   │
│   ├── services/                   # 비즈니스 로직 계층
│   │   ├── __init__.py
│   │   └── nexon_api_service.py    # NEXON Open API 검증 및 조회
│   │
│   ├── routes/                     # Flask Blueprint 라우터
│   │   ├── __init__.py             # Blueprint 등록 함수
│   │   ├── home.py                 # 페이지 라우터 (로그인, 계정 목록)
│   │   └── api.py                  # REST API 라우터 (향후 추가 예정)
│   │
│   ├── templates/                  # HTML 템플릿
│   │   ├── login.html              # 로그인 페이지 (API 키 입력)
│   │   └── account_list.html       # 계정 목록 페이지
│   │
│   └── static/                     # 정적 파일
│       ├── css/
│       │   └── login.css           # 로그인 페이지 스타일
│       ├── js/
│       │   └── login.js            # JavaScript (향후 추가)
│       └── images/
│           └── login_bg.jpg        # 배경 이미지
│
├── migrations/                     # DB 마이그레이션 (향후 추가)
└── venv/                          # 가상 환경
```

## 라우팅 구조

| URL | 메서드 | 설명 |
|-----|--------|------|
| `/` | GET | 로그인 페이지 (API 키 입력) |
| `/account_list` | GET, POST | 계정 목록 조회 페이지 |

## API 키 검증 로직

- **`services/nexon_api_service.py`**
  - `api_key_check(api_key)`: NEXON Open API 키 검증
  - `get_account_list(api_response_data)`: 계정 목록 추출
  - `get_account_first_character(account_list)`: 각 계정의 첫 캐릭터 이름 추출

## 설치 및 실행

### 1. 가상 환경 설정

```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3️⃣ 앱 실행

```bash
python app.py
```

서버는 http://127.0.0.1:5000 에서 실행됩니다.

## 사용 방법

1. 로그인 페이지(`/`)에서 **NEXON Open API 키** 입력
2. "API 찾기" 버튼을 클릭하여 API 키 발급 페이지 접속
3. 계정 목록(`/account_list`)에서 보유한 모든 계정 확인

## 주요 기능

- NEXON Open API를 이용한 API 키 검증
- 계정 목록 조회 및 표시
- 각 계정의 첫 캐릭터 정보 표시
- 캐릭터 상세 정보 조회 (향후 추가 예정)
- 대시보드 및 통계 (향후 추가 예정)

## 📁 아키텍처 설계

### 계층 분리

```
Routes (routes/home.py)
    ↓
Services (services/nexon_api_service.py)
    ↓
External API (NEXON Open API)
```

**장점:**
- 비즈니스 로직과 라우팅 분리 → 유지보수 용이
- 테스트 작성 간편 (서비스 레이어 단위 테스트 가능)
- 코드 재사용성 증가
- 향후 확장에 유리

## 📦 의존성 (requirements.txt)

```
Flask==2.3.0
requests==2.31.0
beautifulsoup4==4.12.0
pandas==2.0.0
```

## 🚧 향후 추가 예정

- [ ] 데이터베이스 통합 (SQLAlchemy + Flask-SQLAlchemy)
- [ ] 캐릭터 상세 정보 조회 API
- [ ] 대시보드 페이지
- [ ] 사용자 인증 시스템
- [ ] 캐릭터 비교 기능
- [ ] 단위 테스트 작성

## 📝 주의사항

- API_KEY.txt는 `.gitignore`에 포함되어 있어 git에 커밋되지 않습니다.
- Debug 모드는 개발 환경에서만 사용하세요.
- 프로덕션 배포 시 WSGI 서버(Gunicorn 등)를 사용하세요.
