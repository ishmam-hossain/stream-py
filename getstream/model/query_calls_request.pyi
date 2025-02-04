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

class QueryCallsRequest(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "sort",
        }

        class properties:
            class sort(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["SortParamRequest"]:
                        return SortParamRequest
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["SortParamRequest"],
                        typing.List["SortParamRequest"],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "sort":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "SortParamRequest":
                    return super().__getitem__(i)

            class filter_conditions(schemas.DictSchema):
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                def __getitem__(
                    self, name: typing.Union[str,]
                ) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                def get_item_oapg(
                    self, name: typing.Union[str,]
                ) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[
                        MetaOapg.additional_properties,
                        dict,
                        frozendict.frozendict,
                        str,
                        date,
                        datetime,
                        uuid.UUID,
                        int,
                        float,
                        decimal.Decimal,
                        bool,
                        None,
                        list,
                        tuple,
                        bytes,
                        io.FileIO,
                        io.BufferedReader,
                    ],
                ) -> "filter_conditions":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class limit(schemas.Int32Schema):
                pass
            next = schemas.StrSchema
            prev = schemas.StrSchema
            watch = schemas.BoolSchema
            __annotations__ = {
                "sort": sort,
                "filter_conditions": filter_conditions,
                "limit": limit,
                "next": next,
                "prev": prev,
                "watch": watch,
            }
    sort: MetaOapg.properties.sort

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["sort"]
    ) -> MetaOapg.properties.sort: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["filter_conditions"]
    ) -> MetaOapg.properties.filter_conditions: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["limit"]
    ) -> MetaOapg.properties.limit: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["next"]
    ) -> MetaOapg.properties.next: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["prev"]
    ) -> MetaOapg.properties.prev: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["watch"]
    ) -> MetaOapg.properties.watch: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "sort",
                "filter_conditions",
                "limit",
                "next",
                "prev",
                "watch",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["sort"]
    ) -> MetaOapg.properties.sort: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["filter_conditions"]
    ) -> typing.Union[MetaOapg.properties.filter_conditions, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["limit"]
    ) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["next"]
    ) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["prev"]
    ) -> typing.Union[MetaOapg.properties.prev, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["watch"]
    ) -> typing.Union[MetaOapg.properties.watch, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "sort",
                "filter_conditions",
                "limit",
                "next",
                "prev",
                "watch",
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
        filter_conditions: typing.Union[
            MetaOapg.properties.filter_conditions,
            dict,
            frozendict.frozendict,
            schemas.Unset,
        ] = schemas.unset,
        limit: typing.Union[
            MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        next: typing.Union[
            MetaOapg.properties.next, str, schemas.Unset
        ] = schemas.unset,
        prev: typing.Union[
            MetaOapg.properties.prev, str, schemas.Unset
        ] = schemas.unset,
        watch: typing.Union[
            MetaOapg.properties.watch, bool, schemas.Unset
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
    ) -> "QueryCallsRequest":
        return super().__new__(
            cls,
            *_args,
            filter_conditions=filter_conditions,
            limit=limit,
            next=next,
            prev=prev,
            watch=watch,
            _configuration=_configuration,
            **kwargs,
        )

from getstream.model.sort_param_request import SortParamRequest
