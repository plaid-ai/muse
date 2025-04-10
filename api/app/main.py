from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
import logging

from app.core.config import settings
from app.api.v1.endpoints import notes as notes_v1

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api_prefix = settings.API_V1_STR
if not api_prefix.startswith("/"):
    api_prefix = "/" + api_prefix


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{api_prefix}/openapi.json"
)

# --- Exception Handlers ---
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# --- Routers ---
app.include_router(notes_v1.router, prefix=settings.API_V1_STR + "/notes", tags=["Notes"])

# --- Root Endpoint ---
@app.get("/", summary="Health Check", tags=["Default"])
async def read_root():
    """기본 상태 확인 엔드포인트"""
    logger.info("Health check endpoint accessed.")
    return {"status": "ok", "message": f"Welcome to {settings.PROJECT_NAME}!"}

# --- Startup Event (선택 사항: 앱 시작 시 리소스 초기화 등) ---
@app.on_event("startup")
async def startup_event():
    logger.info("Application startup...")
    # 예: 데이터베이스 연결 풀 생성, 전역 ElevenLabs 클라이언트 초기화 등
    # global_elevenlabs_client = await elevenlabs_service.get_elevenlabs_client(settings.ELEVENLABS_API_KEY)
    # app.state.elevenlabs_client = global_elevenlabs_client # app.state에 저장하여 사용 가능
    logger.info("Application startup complete.")

# --- Shutdown Event (선택 사항: 앱 종료 시 리소스 정리 등) ---
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown...")
    # 예: 데이터베이스 연결 종료 등
    logger.info("Application shutdown complete.")

# --- Uvicorn 실행 (로컬 테스트용) ---
# Docker 환경에서는 Dockerfile의 CMD/ENTRYPOINT를 사용하므로 이 부분은 주석 처리하거나 제거해도 됩니다.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)