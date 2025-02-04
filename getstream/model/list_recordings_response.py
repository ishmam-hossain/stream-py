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


class ListRecordingsResponse(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "duration",
            "recordings",
        }

        class properties:
            duration = schemas.StrSchema

            class recordings(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["CallRecording"]:
                        return CallRecording

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["CallRecording"], typing.List["CallRecording"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "recordings":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> "CallRecording":
                    return super().__getitem__(i)

            __annotations__ = {
                "duration": duration,
                "recordings": recordings,
            }

    duration: MetaOapg.properties.duration
    recordings: MetaOapg.properties.recordings

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["recordings"]
    ) -> MetaOapg.properties.recordings:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "duration",
                "recordings",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["recordings"]
    ) -> MetaOapg.properties.recordings:
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
                "duration",
                "recordings",
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
            None,
        ],
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
    ) -> "ListRecordingsResponse":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


from getstream.model.call_recording import CallRecording
