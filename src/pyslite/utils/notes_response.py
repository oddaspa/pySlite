"""
Copyright 2024 Odd Gunnar Aspaas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator



class NoteInfo(BaseModel):
    id: str
    parentNoteId: str
    title: str
    updatedAt: datetime
    url: str
    attributes: Optional[List[str]] = None
    columns: Optional[List[str]] = None

    @validator("updatedAt")
    def parse_datetime(cls, value):
        return datetime.fromisoformat(value.replace('Z', '+00:00'))


class NotesResponse(BaseModel):
    nextCursor: Optional[str] = None
    hasNextPage: bool
    total: int
    notes: List[NoteInfo]

