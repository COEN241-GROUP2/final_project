# Test 1

Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 100
```

Number of containers:

```
75
```

Log:
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

# Test 2
Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 200
```

Number of containers:

```
142
```

Log:
```
Started phase 0, duration: 10s @ 09:42:42(-0800) 2020-11-09
Report @ 09:42:52(-0800) 2020-11-09
Elapsed time: 10 seconds
  Scenarios launched:  1970
  Scenarios completed: 1939
  Requests completed:  1939
  Mean response/sec: 197.79
  Response time (msec):
    min: 75.3
    max: 856.3
    median: 103.9
    p95: 697.9
    p99: 770.8
  Codes:
    200: 1939

Warning:
CPU usage of Artillery seems to be very high (pids: 2846)
which may severely affect its performance.
See https://artillery.io/docs/faq/#high-cpu-warnings for details.

Report @ 09:42:52(-0800) 2020-11-09
Elapsed time: 11 seconds
  Scenarios launched:  30
  Scenarios completed: 61
  Requests completed:  61
  Mean response/sec: 42.11
  Response time (msec):
    min: 84.1
    max: 240.8
    median: 142.7
    p95: 229.5
    p99: 240
  Codes:
    200: 61

All virtual users finished
Summary report @ 09:42:52(-0800) 2020-11-09
  Scenarios launched:  2000
  Scenarios completed: 2000
  Requests completed:  2000
  Mean response/sec: 185.87
  Response time (msec):
    min: 75.3
    max: 856.3
    median: 104.6
    p95: 697.2
    p99: 770.5
  Scenario counts:
    0: 2000 (100%)
  Codes:
    200: 2000
```

# Test 3

Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 300
```

Number of containers:

```
158
```

Log:
```
Started phase 0, duration: 10s @ 17:58:15(-0800) 2020-11-11
Report @ 17:58:25(-0800) 2020-11-11
Elapsed time: 10 seconds
  Scenarios launched:  2215
  Scenarios completed: 2119
  Requests completed:  2119
  Mean response/sec: 222.19
  Response time (msec):
    min: 93
    max: 1709.9
    median: 149.6
    p95: 742
    p99: 812.5
  Codes:
    200: 2119

Warning:
CPU usage of Artillery seems to be very high (pids: 9320)
which may severely affect its performance.
See https://artillery.io/docs/faq/#high-cpu-warnings for details.

Report @ 17:58:29(-0800) 2020-11-11
Elapsed time: 14 seconds
  Scenarios launched:  785
  Scenarios completed: 881
  Requests completed:  881
  Mean response/sec: 184.74
  Response time (msec):
    min: 200.5
    max: 1638
    median: 318.9
    p95: 401.7
    p99: 1593.3
  Codes:
    200: 881

All virtual users finished
Summary report @ 17:58:29(-0800) 2020-11-11
  Scenarios launched:  3000
  Scenarios completed: 3000
  Requests completed:  3000
  Mean response/sec: 210.38
  Response time (msec):
    min: 93
    max: 1709.9
    median: 229
    p95: 729.8
    p99: 1430.4
  Scenario counts:
    0: 3000 (100%)
  Codes:
    200: 3000
```

# Test 4

Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 150
```

Number of containers:

```
112
```

Log:
```
Started phase 0, duration: 10s @ 14:44:12(-0800) 2020-11-13
Report @ 14:44:22(-0800) 2020-11-13
Elapsed time: 10 seconds
  Scenarios launched:  1498
  Scenarios completed: 1296
  Requests completed:  1296
  Mean response/sec: 150.86
  Response time (msec):
    min: 98.9
    max: 1414.9
    median: 695.3
    p95: 1369.6
    p99: 1389.4
  Codes:
    200: 1296

Report @ 14:44:24(-0800) 2020-11-13
Elapsed time: 11 seconds
  Scenarios launched:  2
  Scenarios completed: 204
  Requests completed:  204
  Mean response/sec: 1.33
  Response time (msec):
    min: 955.8
    max: 1376.1
    median: 1275.5
    p95: 1349.9
    p99: 1368.7
  Codes:
    200: 204

All virtual users finished
Summary report @ 14:44:24(-0800) 2020-11-13
  Scenarios launched:  1500
  Scenarios completed: 1500
  Requests completed:  1500
  Mean response/sec: 130.78
  Response time (msec):
    min: 98.9
    max: 1414.9
    median: 771.5
    p95: 1365.7
    p99: 1389
  Scenario counts:
    0: 1500 (100%)
  Codes:
    200: 1500
```

# Test 5

Artillery
```yaml
  phases:
    - duration: 10
      arrivalRate: 250
```

Number of containers:

```
?
```

Log:
```
```