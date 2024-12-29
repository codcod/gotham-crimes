Gotham Crime Data
=================

Example app built with [Starlette](https://starlette.io).

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
        Latency    39.04ms   22.14ms 127.64ms   64.16%
        Req/Sec     1.06k   210.18     1.58k    65.17%
      Latency Distribution
         50%   34.73ms
         75%   54.51ms
         90%   71.57ms
         99%   93.42ms
      63557 requests in 5.05s, 121.83MB read
      Socket errors: connect 0, read 552, write 14, timeout 0
    Requests/sec:  12578.75
    Transfer/sec:     24.11MB
