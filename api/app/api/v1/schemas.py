from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class NoteBase(BaseModel):
    summary: str = Field(..., description="강의 요약")
    key_points: List[str] = Field(..., description="핵심 포인트 목록")
    details: str = Field(..., description="세부 내용")

class NoteCreateResponse(NoteBase):
    id: str = Field(..., description="생성된 노트의 고유 ID")
    creation_date: datetime = Field(..., description="노트 생성 날짜 및 시간 (UTC)")
    transcript: Optional[str] = Field(None, description="원본 오디오 트랜스크립트 (선택 사항)")

class NoteListResponse(BaseModel):
    id: str
    creation_date: datetime
    summary: str

class PaginatedNoteListResponse(BaseModel):
    total_count: int = Field(..., description="전체 노트 수")
    page: int = Field(..., description="현재 페이지 번호")
    page_size: int = Field(..., description="페이지 당 노트 수")
    notes: List[NoteListResponse] = Field(..., description="현재 페이지의 노트 목록")

class TranscriptionResponse(BaseModel):
    transcript: str = Field(..., description="오디오 파일의 텍스트 트랜스크립트")