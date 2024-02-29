# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.too_many_requests_error import TooManyRequestsError
from .types.forbidden_error_body import ForbiddenErrorBody
from .types.internal_server_error_body import InternalServerErrorBody
from .types.post_chat_request_messages_item import PostChatRequestMessagesItem
from .types.post_chat_response import PostChatResponse
from .types.too_many_requests_error_body import TooManyRequestsErrorBody

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BrevianApi:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )

    def post_chat(self, *, messages: typing.List[PostChatRequestMessagesItem], agent_id: str) -> PostChatResponse:
        """
        Parameters:
            - messages: typing.List[PostChatRequestMessagesItem].

            - agent_id: str.
        ---
        from brevian import PostChatRequestMessagesItem, PostChatRequestMessagesItemRole
        from brevian.client import BrevianApi

        client = BrevianApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_chat(
            messages=[
                PostChatRequestMessagesItem(
                    role=PostChatRequestMessagesItemRole.USER,
                    content="content",
                )
            ],
            agent_id="agentId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "chat"),
            json=jsonable_encoder({"messages": messages, "agentId": agent_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostChatResponse, _response.json())  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalServerErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBrevianApi:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )

    async def post_chat(self, *, messages: typing.List[PostChatRequestMessagesItem], agent_id: str) -> PostChatResponse:
        """
        Parameters:
            - messages: typing.List[PostChatRequestMessagesItem].

            - agent_id: str.
        ---
        from brevian import PostChatRequestMessagesItem, PostChatRequestMessagesItemRole
        from brevian.client import AsyncBrevianApi

        client = AsyncBrevianApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.post_chat(
            messages=[
                PostChatRequestMessagesItem(
                    role=PostChatRequestMessagesItemRole.USER,
                    content="content",
                )
            ],
            agent_id="agentId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "chat"),
            json=jsonable_encoder({"messages": messages, "agentId": agent_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostChatResponse, _response.json())  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalServerErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)