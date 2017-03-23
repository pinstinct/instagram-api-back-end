# 소개
구현한 주요 기능은 다음과 같다.

### Post
- GET /api/post/ : 포스트 리스트
- POST /api/post/ : 포스트 추가
- POST /post/create/ : 포스트에 사진 추가

### Authentication
- POST /api/member/token-auth/ : 토큰 발급
- POST /api/member/token-delete/ : 토큰 삭제
- POST /rest-auth/login/ : 로그인
- POST /rest-auth/logout/ : 로그아웃

### Member
- GET /api/member/profile/ : 프로필 목록 (권한: 인증된 사용자)


## Requirements
- Python (3.5.2)
- Django (1.10.6)
- Pillow (4.0.0)
- psycopg2 (2.7)
- DjangoRestFramework (3.6.2)
- django-rest-auth (0.9.1)
- django-cors-headers (2.0.2)


## Installation
```shell
$ pip install -r 'requierements.txt'
```
