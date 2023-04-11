# coding: utf-8

"""
    Stream Video API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v79.45.0
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

from openapi_client import schemas  # noqa: F401


class WSAuthMessageRequest(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "user_details",
            "token",
        }
        
        class properties:
            token = schemas.StrSchema
        
            @staticmethod
            def user_details() -> typing.Type['ConnectUserDetailsRequest']:
                return ConnectUserDetailsRequest
        
            @staticmethod
            def device() -> typing.Type['DeviceFieldsRequest']:
                return DeviceFieldsRequest
            __annotations__ = {
                "token": token,
                "user_details": user_details,
                "device": device,
            }

    
    user_details: 'ConnectUserDetailsRequest'
    token: MetaOapg.properties.token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_details"]) -> 'ConnectUserDetailsRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device"]) -> 'DeviceFieldsRequest': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token", "user_details", "device", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_details"]) -> 'ConnectUserDetailsRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device"]) -> typing.Union['DeviceFieldsRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token", "user_details", "device", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        device: typing.Union['DeviceFieldsRequest', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WSAuthMessageRequest':
        return super().__new__(
            cls,
            *_args,
            device=device,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.connect_user_details_request import ConnectUserDetailsRequest
from openapi_client.model.device_fields_request import DeviceFieldsRequest
