# coding=utf-8
from __future__ import unicode_literals

import conftest

import pytest

from mopidy_pandora.uri import PandoraUri, StationUri, TrackUri


def test_pandora_parse_mock_uri():

    uri = "pandora:mock"

    obj = PandoraUri.parse(uri)

    assert isinstance(obj, PandoraUri)
    assert obj.uri == uri


def test_pandora_parse_unicode_mock_uri():

    uri = PandoraUri("pandora:Ω≈ç√∫˜µ≤≥÷")

    obj = PandoraUri.parse(uri.uri)

    assert isinstance(obj, PandoraUri)
    assert obj.uri == uri.uri


def test_pandora_parse_int_mock_uri():

    uri = PandoraUri(1)

    obj = PandoraUri.parse(uri.uri)

    assert isinstance(obj, PandoraUri)
    assert obj.uri == uri.uri


def test_pandora_parse_none_mock_uri():

    uri = PandoraUri()

    assert uri.quote(None) == ''


def test_pandora_parse_invalid_mock_uri():
    with pytest.raises(IndexError):

        PandoraUri().parse('invalid')


def test_station_uri_from_station(station_mock):

    station_uri = StationUri.from_station(station_mock)

    assert station_uri.uri == "pandora:" + \
        station_uri.quote(conftest.MOCK_STATION_SCHEME) + ":" + \
        station_uri.quote(conftest.MOCK_STATION_ID) + ":" + \
        station_uri.quote(conftest.MOCK_STATION_TOKEN)


def test_station_uri_parse(station_mock):

    station_uri = StationUri.from_station(station_mock)

    obj = StationUri.parse(station_uri.uri)

    assert isinstance(obj, StationUri)

    assert obj.scheme == conftest.MOCK_STATION_SCHEME
    assert obj.station_id == conftest.MOCK_STATION_ID
    assert obj.token == conftest.MOCK_STATION_TOKEN

    assert obj.uri == station_uri.uri


def test_track_uri_from_track(playlist_item_mock):

    track_uri = TrackUri.from_track(playlist_item_mock)

    assert track_uri.uri == "pandora:" + \
        track_uri.quote(conftest.MOCK_TRACK_SCHEME) + ":" + \
        track_uri.quote(conftest.MOCK_STATION_ID) + ":" + \
        track_uri.quote(conftest.MOCK_TRACK_TOKEN)


def test_track_uri_from_track_for_ads(ad_item_mock):

    track_uri = TrackUri.from_track(ad_item_mock)

    assert track_uri.uri == "pandora:" + \
        track_uri.quote(conftest.MOCK_TRACK_SCHEME) + "::" + \
        track_uri.quote(TrackUri.ADVERTISEMENT_TOKEN) + ":" + \
        track_uri.quote(conftest.MOCK_TRACK_NAME) + ":::" + \
        track_uri.quote(conftest.MOCK_TRACK_AUDIO_HIGH) + ":" + \
        track_uri.quote(0)


def test_track_uri_parse(playlist_item_mock):

    track_uri = TrackUri.from_track(playlist_item_mock)

    obj = TrackUri.parse(track_uri.uri)

    assert isinstance(obj, TrackUri)

    assert obj.scheme == conftest.MOCK_TRACK_SCHEME
    assert obj.station_id == conftest.MOCK_STATION_ID
    assert obj.token == conftest.MOCK_TRACK_TOKEN

    assert obj.uri == track_uri.uri


def test_track_uri_is_ad(playlist_item_mock, ad_item_mock):

    track_uri = TrackUri.from_track(ad_item_mock)
    obj = TrackUri.parse(track_uri.uri)

    assert obj.is_ad_uri()

    track_uri = TrackUri.from_track(playlist_item_mock)
    obj = TrackUri.parse(track_uri.uri)

    assert not obj.is_ad_uri()
