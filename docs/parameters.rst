Selected Parameters
===================

Here is some further explanation for those not so obvious parameters.

GROUP_EXCLUDE
-------------

Filter the playlist depends on the group title with a blacklist (regular expression).
Note that, it has higher priority than the whitelist ``GROUP_INCLUDE``.

GROUP_INCLUDE
-------------

Filter the playlist depends on the group title with a whitelist (regular expression).
Note that, if set, only groups match the pattern will be included.

CHANNEL_EXCLUDE
---------------

Filter the playlist depends on the channel title by a blacklist (regular expression).
Note that, it has higher priority than the whitelist ``CHANNEL_INCLUDE``.

CHANNEL_INCLUDE
---------------

Filter the playlist depends on the channel title by a whitelist (regular expression).
Note that, if set, only channels match the pattern will be included.

MIN_HEIGHT
----------

HEIGHT is a dominant factor of stream quality,
where 1080 in height means 1080p.
It is necessary to set this filter
if the stream is supposed to be shown on high resolution screens,
e.g., a 4K TV.

CONFIG
------

`CONFIG <https://github.com/huxuan/iptvtools/blob/master/config.json>`_
is a customized configuration to unify ``title`` and ``id``.
``title`` is the exact title which will be shown and
the ``id`` is used for potential match with the template.
A general idea is to make the ``id`` as simple as possible
so they will have a high possibility to match,
though there might be some false positive cases.
So, ``id_unifiers`` can be treated as
a further simplification of ``title_unifier``.

For example, entry ``"-": ""`` will convert ``CCTV-1`` to ``CCTV1``,
entry ``"＋": "+"`` will convert ``CCTV-5＋`` to ``CCTV-5+``.
A whole replacement is also possible,
as ``"BTV冬奥纪实": "北京纪实"`` will
match the whole of ``BTV冬奥纪实`` and
replace it with ``北京纪实``.

Please be caution about using too many of them
since this simplified strategy is just for some basic requirement.
Some entries may lead to some unexpected changes.
For example, entry ``"CCTV-1": "中央1套"`` will convert ``CCTV-11`` to ``中央1套1``.
So, in generally,
only keep those necessary entries and keep it as simple as possible.

SORT_KEYS
---------

List of keys to sort the channels. Valid options currently supported are
`tvg-id`, `height` and `title`. By default, it will work the same as
`-s tvg-id resolution title`, and you can change the order as you want.
If you want to have more keys to be supported, just let me know.

TEMPLATES
---------

A m3u playlist with well-maintained information to cooperate with EPG.
Please refer to `Well‐maintained templates & EPGs <https://github.com/huxuan/iptvtools/wiki/Well%E2%80%90maintained-templates-&-EPGs>`_.

BTW, there is also a list `Well‐maintained playlists <https://github.com/huxuan/iptvtools/wiki/Well%E2%80%90maintained-playlists>`_.

TIMEOUT
-------

TIMEOUT is used to check the connectivity.
Direct check which only fetch the response header tends to be fast.
But it usually takes seconds to probe stream information
depends on your network (bandwidth and latency).
For me, it is about 3 to 5 seconds.

UDPXY
-----

If the IPTV streams is forwarded by UDPXY,
setting it will convert all the urls automatically.
For examples, with UDPXY ``http://192.168.0.1:8888/``,
``rtp://123.45.67.89:1234`` will be converted to
``http://192.168.0.1:8888/rtp/123.45.67.89:1234``.

SKIP_CONNECTIVITY_CHECK
-----

Skip any connectivity check (to be used to just apply title and id unifiers)
use in combination with `-I 0`

