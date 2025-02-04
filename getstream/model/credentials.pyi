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

class Credentials(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "server",
            "ice_servers",
            "token",
        }

        class properties:
            class ice_servers(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["ICEServer"]:
                        return ICEServer
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["ICEServer"], typing.List["ICEServer"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "ice_servers":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "ICEServer":
                    return super().__getitem__(i)
            @staticmethod
            def server() -> typing.Type["SFUResponse"]:
                return SFUResponse
            token = schemas.StrSchema
            __annotations__ = {
                "ice_servers": ice_servers,
                "server": server,
                "token": token,
            }
    server: "SFUResponse"
    ice_servers: MetaOapg.properties.ice_servers
    token: MetaOapg.properties.token

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["ice_servers"]
    ) -> MetaOapg.properties.ice_servers: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["server"]
    ) -> "SFUResponse": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["token"]
    ) -> MetaOapg.properties.token: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "ice_servers",
                "server",
                "token",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["ice_servers"]
    ) -> MetaOapg.properties.ice_servers: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["server"]
    ) -> "SFUResponse": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["token"]
    ) -> MetaOapg.properties.token: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "ice_servers",
                "server",
                "token",
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
        server: "SFUResponse",
        ice_servers: typing.Union[
            MetaOapg.properties.ice_servers,
            list,
            tuple,
        ],
        token: typing.Union[
            MetaOapg.properties.token,
            str,
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
    ) -> "Credentials":
        return super().__new__(
            cls,
            *_args,
            server=server,
            ice_servers=ice_servers,
            token=token,
            _configuration=_configuration,
            **kwargs,
        )

from getstream.model.ice_server import ICEServer
from getstream.model.sfu_response import SFUResponse
