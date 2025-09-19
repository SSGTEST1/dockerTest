# 1. 베이스 이미지 선택 (Python 3.9 공식 이미지 사용)
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. 컨테이너 외부로 노출할 포트 설정
EXPOSE 5000

# 6. 컨테이너가 시작될 때 실행할 명령어
CMD ["python", "app.py"]
