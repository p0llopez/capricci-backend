from typing import Any

from ninja import Schema


class DetailsSchema(Schema):
    details: dict


class IdSchema(Schema):
    id: Any


class TokenSchema(Schema):
    token: str
