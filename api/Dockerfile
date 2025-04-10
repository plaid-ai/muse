# MUSE/api/Dockerfile

# 1. 베이스 이미지 선택
FROM python:3.8.20

# 2. 작업 디렉토리 설정 (컨테이너 내부 경로)
WORKDIR /app

# 3. 환경 변수 설정 (선택 사항)
ENV PYTHONUNBUFFERED=1

# 4. 시스템 의존성 설치 (필요시 주석 해제)
# RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# 5. Python 의존성 설치
# requirements.txt 먼저 복사하여 레이어 캐싱 활용
# Docker 빌드 컨텍스트가 MUSE/api/ 이므로, 현재 디렉토리의 requirements.txt를 의미함
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. 애플리케이션 코드 복사
# Docker 빌드 컨텍스트(MUSE/api/) 아래의 app 폴더를 컨테이너의 /app/app 으로 복사
COPY ./app /app/app

# 7. 포트 노출
EXPOSE 8000

# 8. 애플리케이션 실행 명령어
# 컨테이너 내 /app 디렉토리에서 uvicorn 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]