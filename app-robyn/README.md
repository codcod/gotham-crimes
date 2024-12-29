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
        Latency    28.41ms   20.89ms 144.95ms   68.79%
        Req/Sec     1.56k   310.14     2.30k    68.33%
      Latency Distribution
         50%   24.73ms
         75%   37.51ms
         90%   60.22ms
         99%   89.14ms
      93234 requests in 5.01s, 179.52MB read
      Socket errors: connect 0, read 504, write 9, timeout 0
    Requests/sec:  18597.97
    Transfer/sec:     35.81MB
