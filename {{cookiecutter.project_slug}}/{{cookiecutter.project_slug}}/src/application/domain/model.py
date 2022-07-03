from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
