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


class QueryMembersResponse(
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
            "duration",
            "members",
        }
        
        class properties:
            duration = schemas.StrSchema
            
            
            class members(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MemberResponse']:
                        return MemberResponse
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['MemberResponse'], typing.List['MemberResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'members':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MemberResponse':
                    return super().__getitem__(i)
            next = schemas.StrSchema
            prev = schemas.StrSchema
            __annotations__ = {
                "duration": duration,
                "members": members,
                "next": next,
                "prev": prev,
            }

    
    duration: MetaOapg.properties.duration
    members: MetaOapg.properties.members
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next"]) -> MetaOapg.properties.next: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prev"]) -> MetaOapg.properties.prev: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration", "members", "next", "prev", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prev"]) -> typing.Union[MetaOapg.properties.prev, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration", "members", "next", "prev", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        next: typing.Union[MetaOapg.properties.next, str, schemas.Unset] = schemas.unset,
        prev: typing.Union[MetaOapg.properties.prev, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QueryMembersResponse':
        return super().__new__(
            cls,
            *_args,
            next=next,
            prev=prev,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.member_response import MemberResponse
