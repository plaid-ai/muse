from datetime import datetime
from typing import List, Dict
import uuid

_notes = []

def save_note(transcript: str, summary: str, key_points: List[str], details: str) -> Dict:
    note = {
        "id": str(uuid.uuid4()),
        "creation_date": datetime.utcnow().isoformat(),
        "transcript": transcript,
        "summary": summary,
        "key_points": key_points,
        "details": details,
    }
    _notes.append(note)
    return note

def get_all_notes_sorted_by_date(page: int = 1, page_size: int = 10) -> List[Dict]:
    sorted_notes = sorted(_notes, key=lambda x: x["creation_date"], reverse=True)
    start = (page - 1) * page_size
    end = start + page_size
    return sorted_notes[start:end]

def get_total_notes_count() -> int:
    return len(_notes)
