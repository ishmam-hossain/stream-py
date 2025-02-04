
from datetime import datetime, timedelta
import os

import jwt
from getstream.version import VERSION
import pytest
from getstream import Stream

VIDEO_API_KEY = os.environ.get("VIDEO_API_KEY")
BASE_URL = "https://video.stream-io-api.com/video"
VIDEO_API_SECRET = os.environ.get("VIDEO_API_SECRET")
TIMEOUT = 6

CALL_ID = "c1b0e1e0-9f1b-4c7d-8c3a-9e8a5f0e6b6c"


def create_call_type_data():
    return {
        "name": "example_calltype3",
        "settings": {
            "audio": {
                "access_request_enabled": True,
                "opus_dtx_enabled": True,
            },
            "recording": {
                "audio_only": True,
                "mode": "available",
                "quality": "audio-only",
            },
            "backstage": {
                "enabled": True,
            },
            "broadcasting": {
                "enabled": True,
                "hls": {
                    "auto_on": True,
                    "enabled": True,
                    "quality_tracks": ["audio-only", "360p", "480p", "720p", "1080p", "1440p"],
                },
            },
            "screensharing": {
                "access_request_enabled": True,
                "enabled": True,
            },
            "transcription": {
                "closed_caption_mode": "available",
                "mode": "available",
            },
            "video": {
                "access_request_enabled": True,
                "enabled": True,
                "camera_facing": "front",
                "target_resolution": {
                    "bitrate": 240,
                    "height": 240,
                    "width": 1000,
                },
            },
        },
    }


@pytest.fixture(scope="module")
def client():
    return Stream(
    api_key=VIDEO_API_KEY,
    api_secret=VIDEO_API_SECRET,
    timeout=TIMEOUT,
    video_base_url=BASE_URL,
    )

def test_video_client_initialization(client):
    assert client.api_key == VIDEO_API_KEY
    assert client.api_secret == VIDEO_API_SECRET
    assert client.video.base_url == BASE_URL
    assert client.video.timeout == TIMEOUT




def test_create_call_type(client):
    data = create_call_type_data()
    response = client.video.create_call_type(data)
    print(response)
    assert response['name'] == "example_calltype3"
    assert "settings" in response

def test_update_call_type(client):
    name = "example_calltype3"
    updated_data = {
        "settings": {
            "audio": {
                "access_request_enabled": False,
            },
            "recording": {
                "audio_only": False,
            },
        },
    }
    response = client.video.update_call_type(name, updated_data)
    
    assert response["settings"]["audio"]["access_request_enabled"] == False
    assert response["settings"]["recording"]["audio_only"] == False

def test_get_call_type(client):
    name = "example_calltype3"
    response = client.video.get_call_type(name)
 
    assert response["name"] == "example_calltype3"


def test_list_call_types(client):
    response = client.video.list_call_types()
    keys = response["call_types"].keys()
    assert "example_calltype3" in keys


def test_delete_call_type(client):
    response = client.video.delete_call_type("example_calltype3")

    assert "duration" in response

def test_create_token(client):
    token = client.create_token()
    assert token is not None
    #decode claims

    decoded = jwt.decode(token, VIDEO_API_SECRET, algorithms=["HS256"])
    assert decoded["iss"] == f"stream-video-python@{VERSION}"
    assert decoded["sub"] == "server-side"
    assert decoded["iat"] is not None
