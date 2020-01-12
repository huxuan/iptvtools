:tocdepth: 1

iptv-filter
===========

Usage
-----

.. program-output:: iptv-filter -h

Example
-------

There is a `well-maintained IPTV list <https://gist.github.com/sdhzdmzzl/93cf74947770066743fff7c7f4fc5820>`_ only for Beijing Unicom and a `well-maintained templates & EPG <http://epg.51zmt.top:8000/>`_ mainly for China. So for me::

   $ iptv-filter \
   -i https://gist.githubusercontent.com/sdhzdmzzl/93cf74947770066743fff7c7f4fc5820/raw/0be4160f4024320f23daad65bce79e606da47995/bj-unicom-iptv.m3u \
   -t http://epg.51zmt.top:8000/test.m3u

With UDPXY, it becomes::

   $ iptv-filter \
   -i https://gist.githubusercontent.com/sdhzdmzzl/93cf74947770066743fff7c7f4fc5820/raw/0be4160f4024320f23daad65bce79e606da47995/bj-unicom-iptv.m3u \
   -t http://epg.51zmt.top:8000/test.m3u \
   -u http://192.168.0.1:8888

Just replace ``http://192.168.0.1:8888`` with corresponding UDPXY prefix should be OK.
