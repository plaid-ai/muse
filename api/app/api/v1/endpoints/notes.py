import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends, Query
from typing import List
from app.core.config import settings
from app.services import elevenlabs_service, llm_service, storage_service
from app.api.v1 import schemas
from app.services.elevenlabs_service import client
from datetime import datetime


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()




# --- API Endpoints ---

@router.post(
    "/upload/audio",
    response_model=schemas.NoteCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="오디오 파일 업로드 및 노트 생성",
    description="M4A 오디오 파일을 업로드하면 STT를 수행하고 강의 노트를 생성하여 저장합니다."
)
async def upload_audio_create_note(
    *,
    file: UploadFile = File(..., description="업로드할 M4A 오디오 파일"),
):
    """
    오디오 파일을 받아 처리하는 엔드포인트:
    1. 파일 유효성 검사 (간단한 Content-Type 확인)
    2. ElevenLabs STT 호출
    3. LLM 노트 생성 호출 (자리 표시자)
    4. 노트 저장
    5. 생성된 노트 정보 반환
    """
    # 1. 파일 유효성 검사 (간단하게 Content-Type 확인)
    if not file.content_type or not file.content_type.startswith("audio/"):
        # M4A의 정확한 MIME 타입은 'audio/m4a' 또는 'audio/mp4' 일 수 있음
        logger.warning(f"Received file with potentially incorrect content type: {file.content_type}")
        # 필요시 더 엄격한 검사 추가 가능
        # raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     detail=f"Invalid file type. Expected audio/*, got {file.content_type}"
        # )

    try:
        # 2. ElevenLabs STT 호출
        logger.info(f"Processing file: {file.filename}, content_type: {file.content_type}")
        file_bytes = await file.read()  # 파일 내용 읽기
        transcript = elevenlabs_service.transcribe_audio(file_bytes,file.filename)

        if not transcript:
            logger.error("Transcription resulted in empty text.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Transcription failed or returned empty text."
            )

        # 3. LLM 노트 생성 호출 (현재는 자리 표시자)
        # 실제 LLM API 키 등 필요한 인자 전달 필요
        note_content = await llm_service.generate_lecture_notes(transcript)

        # 4. 노트 저장
        saved_note = storage_service.save_note(
            transcript=transcript, # 원본 텍스트 저장
            summary=note_content["summary"],
            key_points=note_content["key_points"],
            details=note_content["details"]
        )

        # 5. 생성된 노트 정보 반환 (스키마에 맞게)
        # storage_service에서 반환된 dict를 NoteCreateResponse 모델로 변환
        # 날짜 문자열을 datetime 객체로 변환
        saved_note_response = schemas.NoteCreateResponse(
            id=saved_note["id"],
            creation_date=datetime.fromisoformat(saved_note["creation_date"]),
            transcript=saved_note["transcript"],
            summary=saved_note["summary"],
            key_points=saved_note["key_points"],
            details=saved_note["details"]
        )
        logger.info(f"Successfully created note with ID: {saved_note_response.id}")
        return saved_note_response

    except HTTPException as http_exc:
        # 이미 처리된 HTTP 예외는 그대로 다시 발생시킴
        raise http_exc
    except Exception as e:
        logger.error(f"Error processing audio file {file.filename}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred while processing the audio file: {e}"
        )
    finally:
        # 파일 핸들 닫기 (중요)
        await file.close()


@router.get(
    "",
    response_model=schemas.PaginatedNoteListResponse,
    summary="저장된 노트 목록 조회",
    description="저장된 모든 강의 노트를 날짜 내림차순으로 페이지네이션하여 조회합니다."
)
async def get_notes_list(
    page: int = Query(1, ge=1, description="페이지 번호 (1부터 시작)"),
    page_size: int = Query(10, ge=1, le=100, description="페이지 당 노트 수 (1~100)")
):
    """
    저장된 노트 목록을 조회하는 엔드포인트:
    1. 저장소에서 노트 목록 조회 (정렬 및 페이지네이션 적용)
    2. 전체 노트 수 조회
    3. 응답 모델에 맞게 데이터 구성하여 반환
    """
    try:
        notes_page = storage_service.get_all_notes_sorted_by_date(page=page, page_size=page_size)
        total_count = storage_service.get_total_notes_count()

        # NoteListResponse 형식으로 변환 (필요한 필드만 선택)
        notes_for_response = [
            schemas.NoteListResponse(
                id=note["id"],
                creation_date=datetime.fromisoformat(note["creation_date"]),
                summary=note["summary"]
            ) for note in notes_page
        ]

        logger.info(f"Retrieved {len(notes_for_response)} notes for page {page} (page_size={page_size}, total={total_count})")

        return schemas.PaginatedNoteListResponse(
            total_count=total_count,
            page=page,
            page_size=page_size,
            notes=notes_for_response
        )
    except Exception as e:
        logger.error(f"Error retrieving notes list: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred while retrieving notes: {e}"
        )