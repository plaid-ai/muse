import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# .env 파일 로드 (Dockerfile에서 직접 환경변수를 주입할 경우 이 줄은 생략 가능)
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Lecture Notes API"
    API_V1_STR: str = "/api/v1"
    ELEVENLABS_API_KEY: str

    # LLM 관련 설정 추가 가능
    # LLM_API_KEY: str | None = None
    # LLM_MODEL_NAME: str = "gemini-pro" # 예시

    class Config:
        # .env 파일에서 환경 변수를 로드하도록 설정
        # Docker 환경에서는 환경 변수를 직접 주입하는 것이 더 일반적입니다.
        # env_file = ".env"
        # env_file_encoding = 'utf-8'
        # case_sensitive = True # 환경 변수 이름 대소문자 구분

        # Docker 환경 변수에서 직접 읽도록 설정 (권장)
        # Pydantic V2 부터는 기본적으로 환경 변수를 읽음
        pass

settings = Settings()


print("✅ API_V1_STR loaded:", settings.API_V1_STR)