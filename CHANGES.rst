Changelog
=========

v0.4.3 (UNRELEASED)
-------------------

- Switch to Black code formatting.
- Update docs to refer to new Pandora 'Premium' subscription model instead of the old 'Plus'.

v0.4.2 (Apr 21, 2019)
---------------------

- Pin pydora dependency to pydora>=1.13,<2. (Resolves: `#70 <https://github.com/jcass77/mopidy-pandora/issues/70>`_).


v0.4.1 (Dec 29, 2018)
---------------------

- Update package dependencies used during development to the latest versions.
- Migrate all tests to pytest. Resolve pytest 4.0 deprecation errors.
- Switch to Xenial Travis build environment.

**Fixes**

- Use the updated Station API introduced in pydora 1.12.0. (Fixes: `#65 <https://github.com/jcass77/mopidy-pandora/issues/65>`_).
- Implement ``LRUCache``'s ``__missing__``. (Fixes: `#66 <https://github.com/jcass77/mopidy-pandora/issues/66>`_).

v0.4.0 (Sep 20, 2017)
---------------------

- Update documentation to refer to new 'Pandora Plus' subscription model instead of the old 'Pandora One'.
- Update troubleshooting guide with more workarounds for cross-signed certificates using OpenSSL < 1.0.2.
- Allow station URI's to be added to playlists and the Mopidy tracklist. (Addresses: `#58 <https://github.com/jcass77/mopidy-pandora/issues/58>`_).

v0.3.0 (Jul 8, 2016)
--------------------

**Features and improvements**

- Add support for searching Pandora stations. (Addresses: `#36 <https://github.com/jcass77/mopidy-pandora/issues/36>`_).
- Switch default partner device configuration values from ``IP01`` (iPhone) to ``android-generic``, which provides more
  stream quality configuration options.

**Fixes**

- Album and artist URIs now point back to the Pandora track. (Fixes: `#51 <https://github.com/jcass77/mopidy-pandora/issues/51>`_).


v0.2.2 (Apr 13, 2016)
---------------------

- Fix an issue that would cause Mopidy-Pandora to raise an exception if a track did not have the ``bitrate`` field specified.
  Please refer to the updated `configuration <https://github.com/jcass77/mopidy-pandora#configuration>`_ options for
  ``preferred_audio_quality`` for details on the effect that the chosen partner device has on stream quality options.
  (Fixes: `#48 <https://github.com/jcass77/mopidy-pandora/issues/48>`_).

v0.2.1 (Feb 6, 2016)
--------------------

- Fix to prevent the Mopidy-Pandora backend from starting up if logging in to the Pandora server failed.
  (Fixes: `#44 <https://github.com/jcass77/mopidy-pandora/issues/44>`_).
- Fixed an issue that would cause only the first few doubleclick events to be processed correctly.

v0.2.0 (Jan 26, 2016)
---------------------

**Features and improvements**

- Now displays all of the correct track information during playback (e.g. song and artist names, album covers, track
  length, bitrate etc.).
- Simulate dynamic tracklist (workaround for `#2 <https://github.com/jcass77/mopidy-pandora/issues/2>`_)
- Add support for browsing genre stations. Note that clicking on a genre station will automatically add that station to
  your profile.
- Add ability to delete a station by setting one of the doubleclick event parameters to ``delete_station``.
- Move 'QuickMix' to the top of the station list. Stations that will be played as part of QuickMix are marked with an
  asterisk (*).
- Scrobbling tracks to Last.fm is now supported.
- Station lists are now cached which speeds up startup and browsing of the list of stations dramatically. Configuration
  parameter ``cache_time_to_live`` can be used to specify when cache items should expire and be refreshed (in seconds).
- Force Mopidy to stop when skip limit is exceeded (workaround for `#1221 <https://github.com/mopidy/mopidy/issues/1221>`_).
- Now plays advertisements which should prevent non-Pandora Premium accounts from being locked after extended use.
- Tracks are now played in ``consume`` instead of ``repeat`` mode. This is more in line with how Pandora deals with
  track playback. It also avoids infinite loops on unplayable tracks, which is still an issue in Mopidy 1.1.2.
- Station sort order now defaults to alphabetical. This makes it easier to find stations if the user profile contains
  more than a few stations.
- Added link to a short troubleshooting guide on the README page.

**Fixes**

- Unplayable tracks are now removed from the tracklist. (Fixes: `#38 <https://github.com/jcass77/mopidy-pandora/issues/38>`_).
- Adds are now always assigned a unique URI. (Fixes: `#39 <https://github.com/jcass77/mopidy-pandora/issues/39>`_).
- Maximum skip limits are now reset whenever user browses another folder. (Fixes: `#43 <https://github.com/jcass77/mopidy-pandora/issues/43>`_).

v0.1.8 (Jan 8, 2016)
--------------------

- Update dependencies: requires at least pydora 1.5.1.

v0.1.7 (Oct 31, 2015)
---------------------

- Configuration parameter ``auto_set_repeat`` has been renamed to ``auto_setup`` - please update your Mopidy
  configuration file.
- Now resumes playback after a track has been rated.
- Enhanced auto_setup routines to ensure that ``consume``, ``random``, and ``single`` modes are disabled as well.
- Optimized auto_setup routines: now only called when the Mopidy tracklist changes.

v0.1.6 (Oct 26, 2015)
---------------------

- Release to pypi

v0.1.5 (Aug 20, 2015)
---------------------

- Add option to automatically set tracks to play in repeat mode when Mopidy-Pandora starts.
- Add experimental support for rating songs by re-using buttons available in the current front-end Mopidy extensions.
- Audio quality now defaults to the highest setting.
- Improved caching to revert to Pandora server if station cannot be found in the local cache.
- Fix to retrieve stations by ID instead of token.
- Add unit tests to increase test coverage.

v0.1.4 (Aug 17, 2015)
---------------------

- Limit number of consecutive track skips to prevent Mopidy's skip-to-next-on-error behaviour from locking the user's
  Pandora account.
- Better handling of exceptions that occur in the backend to prevent Mopidy actor crashes.
- Add support for unicode characters in station and track names.

v0.1.3 (Jul 11, 2015)
---------------------

- Update to work with release of Mopidy version 1.0
- Update to work with pydora version >= 1.4.0: now keeps the Pandora session alive in tha API itself.
- Implement station list caching to speed up browsing.
- Get rid of 'Stations' root directory. Browsing now displays all of the available stations immediately.
- Fill artist name to improve how tracks are displayed in various Mopidy front-end extensions.

v0.1.2 (Jun 20, 2015)
---------------------

- Enhancement to handle ``Invalid Auth Token`` exceptions when the Pandora session expires after long periods of
  inactivity. Allows Mopidy-Pandora to run indefinitely on dedicated music servers like the Pi MusicBox.
- Add configuration option to sort stations alphabetically, instead of by date.

v0.1.1 (Mar 22, 2015)
---------------------

- Added ability to make preferred audio quality user-configurable.

v0.1.0 (Dec 28, 2014)
---------------------

- Initial release.
