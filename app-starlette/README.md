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
        Latency    31.70ms   15.37ms 215.47ms   78.96%
        Req/Sec     1.29k   181.57     1.99k    79.83%
      Latency Distribution
         50%   30.20ms
         75%   38.29ms
         90%   47.39ms
         99%   80.44ms
      77969 requests in 5.07s, 148.86MB read
      Socket errors: connect 0, read 1489, write 30, timeout 0
    Requests/sec:  15370.43
    Transfer/sec:     29.35MB
