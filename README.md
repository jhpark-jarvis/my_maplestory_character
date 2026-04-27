# my_maplestory_character

Nexon Open API를 이용하여 내 메이플스토리 계정의 모든 캐릭터 정보를 한눈에 볼 수 있는 Flask 기반 웹 애플리케이션입니다.

## 주요 기능

- API 키 검증 - NEXON Open API 키 검증 및 계정 정보 조회
- 계정 목록 조회 - 모든 계정 및 첫 캐릭터 정보 표시
- 캐릭터 목록 조회 - 각 계정별 모든 캐릭터 조회
- 캐릭터 상세 정보 - 직업, 레벨, 경험치, 월드, 생성일 등 표시
- 세션 관리 - API 키 세션을 통한 안전한 정보 전달

## 프로젝트 구조

```bash
my_maplestory_character/
├── app.py                          # 앱 진입점 (설정 및 실행)
├── config.py                       # 환경 설정 (SECRET_KEY 등)
├── requirements.txt                # 의존성 패키지
├── README.md
├── check_routes.py                 # 라우팅 확인 스크립트
├── test_api.py                     # API 테스트 스크립트
├── API_KEY.txt                     # API 키 저장 (git에서 제외)
│
├── maple_app/                      # Flask 애플리케이션 패키지
│   ├── __init__.py                 # 앱 초기화 및 Blueprint 등록
│   ├── data.py                     # 데이터 처리 유틸리티 (레거시)
│   │
│   ├── services/                   # 비즈니스 로직 계층
│   │   ├── __init__.py
│   │   └── nexon_api_service.py    # NEXON Open API 서비스
│   │       ├── api_key_check()           # API 키 검증 및 계정 조회
│   │       ├── get_account_list()       # 계정 목록 추출
│   │       ├── get_account_first_character() # 첫 캐릭터 추출
│   │       ├── get_character_list()     # 캐릭터 목록 조회
│   │       ├── get_character_detail()   # 캐릭터 상세 정보 조회
│   │       └── get_character_basic()   # 캐릭터 기본 정보 조회
│   │
│   ├── routes/                     # Flask Blueprint 라우터
│   │   ├── __init__.py             # Blueprint 등록 함수
│   │   ├── home.py                 # 페이지 라우터
│   │   │   ├── login()                  # 로그인 페이지
│   │   │   ├── account_list()           # 계정 목록 페이지 (GET/POST)
│   │   │   └── characters()             # 캐릭터 목록 페이지
│   │   └── api.py                  # REST API 라우터 (향후 추가)
│   │
│   ├── templates/                  # HTML 템플릿
│   │   ├── login.html              # 로그인 페이지 (API 키 입력)
│   │   ├── account_list.html       # 계정 목록 페이지 (테이블)
│   │   └── characters.html         # 캐릭터 목록 페이지 (카드 그리드)
│   │
│   └── static/                     # 정적 파일
│       ├── css/
│       │   └── login.css           # 로그인 페이지 스타일
│       ├── js/
│       │   └── login.js            # JavaScript
│       └── images/
│           └── login_bg.jpg        # 배경 이미지
│
├── migrations/                     # DB 마이그레이션 (향후 추가)
└── venv/                          # 가상 환경
```

## 라우팅 구조

| URL | 메서드 | 설명 | 파라미터 |
|-----|--------|------|---------|
| `/` | GET | 로그인 페이지 | - |
| `/account_list` | GET, POST | 계정 목록 페이지 | `api_key` (GET만) |
| `/characters/<account_id>` | GET | 캐릭터 목록 페이지 | `account_id` |

## 데이터 플로우

```
1. 사용자가 로그인 페이지(/)에서 API 키 입력
   └─ GET /account_list?api_key=xxx 또는 POST /account_list

2. 서버에서 API 키 검증
   ├─ api_key_check() - NEXON API에 검증 요청
   ├─ 세션에 API 키 저장
   └─ 계정 목록 & 첫 캐릭터 조회

3. account_list.html 렌더링
   └─ 테이블 형식으로 계정 & 첫 캐릭터 표시

4. 사용자가 계정 선택
   └─ GET /characters/<account_id>

5. 서버에서 캐릭터 목록 조회
   ├─ 세션에서 API 키 확인
   ├─ get_character_list() - NEXON API에 캐릭터 요청
   └─ 결과 데이터 정렬 & 추출

6. characters.html 렌더링
   └─ 카드 그리드 형식으로 캐릭터 표시
```

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

### 3. 앱 실행

```bash
python app.py
```

서버는 **http://127.0.0.1:5000** 에서 실행됩니다.

## 사용 방법

### 웹 UI 사용
1. 브라우저에서 `http://127.0.0.1:5000` 접속
2. NEXON Open API 키 입력 후 "로그인"
3. 계정 목록에서 계정 선택
4. 캐릭터 목록 확인

### API 키 발급
- [NEXON Open API 페이지](https://openapi.nexon.com/) 접속
- 계정 생성 후 API 키 발급

## 세션 관리

- 저장 위치: Flask의 암호화된 쿠키 (서버 메모리)
- 만료 시간: 기본값 (브라우저 세션)
- 보안: SECRET_KEY로 암호화

## 의존성 (requirements.txt)

```
Flask==2.3.3              # 웹 프레임워크
requests==2.31.0          # HTTP 라이브러리
beautifulsoup4==4.12.2    # HTML 파싱
pandas==2.0.3             # 데이터 처리
Werkzeug==2.3.7           # WSGI 유틸리티
```

## 아키텍처 설계

### 계층 분리

```
Presentation Layer (Templates)
    ↓
Routes Layer (routes/home.py)
    ↓
Services Layer (services/nexon_api_service.py)
    ↓
External API (NEXON Open API)
```

## 테스트

### 라우팅 확인
```bash
python check_routes.py
```

### API 함수 테스트
```bash
python test_api.py
```

## 향후 추가 예정

- [ ] 데이터베이스 통합 (SQLAlchemy)
- [ ] 사용자 인증 시스템 (로그인/회원가입)
- [ ] 캐릭터 비교 기능
- [ ] 대시보드 및 통계
- [ ] 캐릭터 검색 기능
- [ ] 단위 테스트 작성
- [ ] Docker 컨테이너화
- [ ] 배포 (Heroku, AWS 등)

## 주의사항

- API_KEY.txt는 `.gitignore`에 포함 (git 커밋 X)
- Debug 모드는 개발 환경에서만 사용
- 프로덕션 배포 시 WSGI 서버(Gunicorn) 필수
- SECRET_KEY는 환경변수로 관리 권장

## 문제 해결

### 세션이 만료된다면
- 브라우저 쿠키 확인
- `session.modified = True` 설정 확인
- SECRET_KEY 설정 확인

### 캐릭터 목록이 표시되지 않는다면
- API 키 유효성 확인
- 계정에 활성 캐릭터 있는지 확인
- 브라우저 개발자 도구에서 네트워크 탭 확인

### 돌아가기 버튼이 작동하지 않는다면
- 세션 쿠키 확인
- api_key 파라미터 전달 확인
- 브라우저 캐시 삭제
