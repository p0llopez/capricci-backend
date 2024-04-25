from typing import Any

from ninja_schema import ModelSchema
from pydantic import BaseModel


class BaseModelSchema(ModelSchema):
    def create(self, **kwargs: Any) -> Any:
        model_class = self.Config.model
        data = self.dict()
        data.update(kwargs)

        return model_class._default_manager.create(**data)

    def update(self, instance: Any, **kwargs: Any) -> Any:
        if not instance:
            msg = "Instance is required to update an object."
            raise Exception(msg)

        data = self.dict(exclude_none=True)
        data.update(kwargs)

        for attr, value in data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def save(self, instance: Any | None = None, **kwargs: Any) -> Any:
        if instance:
            result = self.update(instance, **kwargs)
            assert result is not None, "`update()` did not return an object instance."
        else:
            result = self.create(**kwargs)
            assert result is not None, "`create()` did not return an object instance."

        return result


class DetailsSchema(BaseModel):
    details: dict


class IdSchema(BaseModel):
    id: Any
