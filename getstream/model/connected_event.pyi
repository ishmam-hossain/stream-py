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

class ConnectedEvent(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This event is sent when the WS connection is established and authenticated, this event contains the full user object as it is stored on the server
    """

    class MetaOapg:
        required = {
            "connection_id",
            "me",
            "created_at",
            "type",
        }

        class properties:
            connection_id = schemas.StrSchema
            created_at = schemas.DateTimeSchema

            @staticmethod
            def me() -> typing.Type["OwnUserResponse"]:
                return OwnUserResponse
            type = schemas.StrSchema
            __annotations__ = {
                "connection_id": connection_id,
                "created_at": created_at,
                "me": me,
                "type": type,
            }
    connection_id: MetaOapg.properties.connection_id
    me: "OwnUserResponse"
    created_at: MetaOapg.properties.created_at
    type: MetaOapg.properties.type

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["connection_id"]
    ) -> MetaOapg.properties.connection_id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["me"]
    ) -> "OwnUserResponse": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "connection_id",
                "created_at",
                "me",
                "type",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["connection_id"]
    ) -> MetaOapg.properties.connection_id: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["me"]
    ) -> "OwnUserResponse": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "connection_id",
                "created_at",
                "me",
                "type",
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
    ) -> "ConnectedEvent":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from getstream.model.own_user_response import OwnUserResponse
