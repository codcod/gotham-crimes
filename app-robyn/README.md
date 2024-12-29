Gotham Crime Data
=================

Example app built with [Robyn framework](https://robyn.tech).

To start developing with Robyn use the following (until
[#1042](https://github.com/sparckles/Robyn/issues/1046) has been resolved):

    uv init my-app --name app -p 3.12
    uv add robyn "sqlalchemy[asyncio]"

To run this example application:

    uv sync
    make .db
    make run

and in a separate command window:

    make wrk/get

which on Mac M1 it gives you result such as:

    wrk -t12 -c500 -d5s --latency "http://127.0.0.1:8000/api/crimes?skip=0&take=10"
    Running 5s test @ http://127.0.0.1:8000/api/crimes?skip=0&take=10
      12 threads and 500 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    40.09ms   14.65ms 101.79ms   53.70%
        Req/Sec     1.02k   119.29     1.28k    85.50%
      Latency Distribution
         50%   41.11ms
         75%   53.65ms
         90%   58.24ms
         99%   63.82ms
      60845 requests in 5.02s, 5.98MB read
      Socket errors: connect 0, read 645, write 0, timeout 0
    Requests/sec:  12127.36
    Transfer/sec:      1.19MB
