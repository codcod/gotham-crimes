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
        Latency    29.80ms   26.89ms 197.11ms   75.56%
        Req/Sec     1.62k   548.18     2.93k    68.17%
      Latency Distribution
         50%   22.55ms
         75%   42.12ms
         90%   68.69ms
         99%  115.95ms
      96880 requests in 5.02s, 185.80MB read
      Socket errors: connect 0, read 595, write 0, timeout 0
    Requests/sec:  19317.14
    Transfer/sec:     37.05MB
