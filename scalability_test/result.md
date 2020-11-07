# Test 1

Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 100
```

Result:
```
Started phase 0, duration: 10s @ 08:43:34(-0700) 2020-10-28
Report @ 08:43:44(-0700) 2020-10-28
Elapsed time: 10 seconds
  Scenarios launched:  999
  Scenarios completed: 990
  Requests completed:  990
  Mean response/sec: 100.5
  Response time (msec):
    min: 60.2
    max: 905.1
    median: 84
    p95: 717.6
    p99: 803.2
  Codes:
    200: 990

Report @ 08:43:45(-0700) 2020-10-28
Elapsed time: 10 seconds
  Scenarios launched:  1
  Scenarios completed: 10
  Requests completed:  10
  Mean response/sec: 3.92
  Response time (msec):
    min: 83.4
    max: 100.1
    median: 93.2
    p95: 100.1
    p99: 100.1
  Codes:
    200: 10

All virtual users finished
Summary report @ 08:43:45(-0700) 2020-10-28
  Scenarios launched:  1000
  Scenarios completed: 1000
  Requests completed:  1000
  Mean response/sec: 95.6
  Response time (msec):
    min: 60.2
    max: 905.1
    median: 84
    p95: 716.9
    p99: 802.8
  Scenario counts:
    0: 1000 (100%)
  Codes:
    200: 1000
```

Container No:
75

# Test 2
Artillery
```yaml
  pool: 100
  phases:
    - duration: 10
      arrivalRate: 500
```

Result:
```
Started phase 0, duration: 10s @ 09:06:09(-0700) 2020-10-28
Report @ 09:06:19(-0700) 2020-10-28
Elapsed time: 10 seconds
  Scenarios launched:  2465
  Scenarios completed: 2435
  Requests completed:  2435
  Mean response/sec: 247.54
  Response time (msec):
    min: 78.8
    max: 958.8
    median: 109.3
    p95: 136
    p99: 731.8
  Codes:
    200: 2435

Warning:
CPU usage of Artillery seems to be very high (pids: 33523)
which may severely affect its performance.
See https://artillery.io/docs/faq/#high-cpu-warnings for details.

Report @ 09:06:29(-0700) 2020-10-28
Elapsed time: 20 seconds
  Scenarios launched:  2467
  Scenarios completed: 2292
  Requests completed:  2292
  Mean response/sec: 247.44
  Response time (msec):
    min: 85.6
    max: 2107.2
    median: 174.4
    p95: 648
    p99: 955.9
  Codes:
    200: 2292

Warning: High CPU usage warning (pids: 33523).
See https://artillery.io/docs/faq/#high-cpu-warnings for details.

Report @ 09:06:30(-0700) 2020-10-28
Elapsed time: 22 seconds
  Scenarios launched:  68
  Scenarios completed: 273
  Requests completed:  273
  Mean response/sec: 38.46
  Response time (msec):
    min: 381.2
    max: 2398.3
    median: 940.8
    p95: 1392.7
    p99: 1921.7
  Codes:
    200: 273

All virtual users finished
Summary report @ 09:06:31(-0700) 2020-10-28
  Scenarios launched:  5000
  Scenarios completed: 5000
  Requests completed:  5000
  Mean response/sec: 229.15
  Response time (msec):
    min: 78.8
    max: 2398.3
    median: 120.4
    p95: 776.1
    p99: 1308.3
  Scenario counts:
    0: 5000 (100%)
  Codes:
    200: 5000
```

Container numbers:
68

# Test 3
root@instance-1:~/coen241# artillery run load_test.yaml 
Started phase 0, duration: 10s @ 17:41:13(+0000) 2020-11-04
Report @ 17:41:23(+0000) 2020-11-04
Elapsed time: 10 seconds
  Scenarios launched:  2759
  Scenarios completed: 2721
  Requests completed:  2721
  Mean response/sec: 276.53
  Response time (msec):
    min: 112.6
    max: 337.9
    median: 126.2
    p95: 231.3
    p99: 296.8
  Codes:
    200: 2721
Warning: 
CPU usage of Artillery seems to be very high (pids: 3050)
which may severely affect its performance.
See https://artillery.io/docs/faq/#high-cpu-warnings for details.
Report @ 17:41:24(+0000) 2020-11-04
Elapsed time: 11 seconds
  Scenarios launched:  241
  Scenarios completed: 279
  Requests completed:  279
  Mean response/sec: 185.5
  Response time (msec):
    min: 109.4
    max: 293.4
    median: 127.6
    p95: 172.5
    p99: 262.4

load_param:
10, 300


