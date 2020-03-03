Selected Parameters
===================

Here is some further explanation for those not so obvious parameters.

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
a further simplification of ``titile_unifier``.

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

TEMPLATE
--------

A m3u playlist with well-maintained information to cooperate with EPG.
Please refer to `Well‐maintained templates & EPGs <https://github.com/huxuan/iptvtools/wiki/Well%E2%80%90maintained-templates-&-EPGs>`_.

BTW, there is also a list `Well‐maintained playlists <https://github.com/huxuan/iptvtools/wiki/Well%E2%80%90maintained-playlists>`_.

TIMEOUT
-------

TIMEOUT is used to check the connectivity.
Direct check which only fecth the response header tends to be fast.
But it usually takes seconds to probe stream information
depends on your network (bandwidth and latency).
For me, it is about 3 to 5 seconds.

UDPXY
-----

If the IPTV streams is forwarded by UPDXY,
setting it will convert all the urls automatically.
For examples, with UDPXY ``http://192.168.0.1:8888/``,
``rtp://123.45.67.89:1234`` will be converted to
``http://192.168.0.1:8888/rtp/123.45.67.89:1234``.
