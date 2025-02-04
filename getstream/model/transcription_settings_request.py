# coding: utf-8

"""
    Stream Video API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v80.4.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from getstream.model import schemas  # noqa: F401


class TranscriptionSettingsRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            closed_caption_mode = schemas.StrSchema

            class mode(schemas.EnumBase, schemas.StrSchema):
                class MetaOapg:
                    enum_value_to_name = {
                        "available": "AVAILABLE",
                        "disabled": "DISABLED",
                        "auto-on": "AUTOON",
                    }

                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available")

                @schemas.classproperty
                def DISABLED(cls):
                    return cls("disabled")

                @schemas.classproperty
                def AUTOON(cls):
                    return cls("auto-on")

            __annotations__ = {
                "closed_caption_mode": closed_caption_mode,
                "mode": mode,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["closed_caption_mode"]
    ) -> MetaOapg.properties.closed_caption_mode:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["mode"]
    ) -> MetaOapg.properties.mode:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "closed_caption_mode",
                "mode",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["closed_caption_mode"]
    ) -> typing.Union[MetaOapg.properties.closed_caption_mode, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["mode"]
    ) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "closed_caption_mode",
                "mode",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        closed_caption_mode: typing.Union[
            MetaOapg.properties.closed_caption_mode, str, schemas.Unset
        ] = schemas.unset,
        mode: typing.Union[
            MetaOapg.properties.mode, str, schemas.Unset
        ] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "TranscriptionSettingsRequest":
        return super().__new__(
            cls,
            *_args,
            closed_caption_mode=closed_caption_mode,
            mode=mode,
            _configuration=_configuration,
            **kwargs,
        )
