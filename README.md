# Example project using Conbench

- https://github.com/ursacomputing/conbench


```
conbench-example
├── LICENSE
├── README.md
├── example
│   ├── __init__.py
│   ├── benchmarks
│   │   ├── __init__.py
│   │   └── benchmark_math.py            (the benchmarks)
│   ├── math.py                          (the code)
│   └── tests
│       ├── __init__.py
│       ├── benchmarks
│       │   ├── __init__.py
│       │   ├── _asserts.py              (custom asserts)
│       │   └── test_benchmark_math.py   (test the benchmarks)
│       ├── conftest.py                  (pytest)
│       └── test_math.py                 (test the code)
├── requirements-test.txt
└── setup.py

```

### Create workspace
    $ cd
    $ mkdir -p envs
    $ mkdir -p workspace


### Create virualenv
    $ cd ~/envs
    $ python3 -m venv example
    $ source example/bin/activate


### Clone repo
    (example) $ cd ~/workspace/
    (example) $ git clone https://github.com/ursacomputing/conbench-example.git


### Install dependencies
    (example) $ cd ~/workspace/conbench-example/
    (example) $ pip install -r requirements-test.txt
    (example) $ python setup.py develop


### Format code
    (example) $ cd ~/workspace/conbench-example/
    (example) $ black .
        reformatted foo.py
    (example) $ git add foo.py


### Sort imports
    (example) $ cd ~/workspace/conbench-example/
    (example) $ isort .
        Fixing foo.py
    (example) $ git add foo.py


### Lint code
    (qa) $ cd ~/workspace/conbench-example/
    (qa) $ flake8
    ./foo/bar/__init__.py:1:1: F401 'FooBar' imported but unused


### Run tests
    (example) $ cd ~/workspace/conbench-example/example/
    (example) $ pytest -vv tests/

```
tests/test_math.py::test_add PASSED
tests/test_math.py::test_subtract PASSED
tests/benchmarks/test_benchmark_math.py::test_benchmark_add PASSED
tests/benchmarks/test_benchmark_math.py::test_benchmark_add_cli PASSED
tests/benchmarks/test_benchmark_math.py::test_benchmark_substract PASSED
tests/benchmarks/test_benchmark_math.py::test_benchmark_substract_cli PASSED

```


### Generate coverage report
    (example) $ cd ~/workspace/conbench-example/
    (example) $ coverage run --source example -m pytest example/tests/ 
    (example) $ coverage report -m
    
```
Name                                              Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------
example/__init__.py                                   0      0   100%
example/benchmarks/__init__.py                        0      0   100%
example/benchmarks/benchmark_math.py                 16      0   100%
example/math.py                                       4      0   100%
example/tests/__init__.py                             0      0   100%
example/tests/benchmarks/__init__.py                  0      0   100%
example/tests/benchmarks/test_benchmark_math.py      14      0   100%
example/tests/test_math.py                            5      0   100%
-------------------------------------------------------------------------------
TOTAL                                                39      0   100%
```

### List benchmarks
    (example) $ cd ~/workspace/conbench-example/example
    (example) $ conbench --help

```
Usage: conbench [OPTIONS] COMMAND [ARGS]...

  Conbench: Language-independent Continuous Benchmarking (CB) Framework

Options:
  --help  Show this message and exit.

Commands:
  add       Run add benchmark.
  subtract  Run subtract benchmark.
 ```

### Benchmark help
    (example) $ cd ~/workspace/conbench-example/example
    (example) $ conbench add --help

 ```
 Usage: conbench add [OPTIONS]

  Run add benchmark.

Options:
  --iterations INTEGER   [default: 1]
  --drop-caches BOOLEAN  [default: False]
  --gc-collect BOOLEAN   [default: True]
  --gc-disable BOOLEAN   [default: True]
  --show-result BOOLEAN  [default: True]
  --show-output BOOLEAN  [default: False]
  --run-id TEXT          Group executions together with a run id.
  --run-name TEXT        Name of run (commit, pull request, etc).
  --help                 Show this message and exit.
 ```

### Run a benchmark
    (example) $ cd ~/workspace/conbench-example/example
    (example) $ conbench add --iterations=5 --show-output=true

 ```
Benchmark output:
2

Benchmark result:
{
    "batch_id": "e02e6c3591c24375b959499ccd667eb6",
    "context": {
        "benchmark_language": "Python",
        "benchmark_language_version": "Python 3.9.6"
    },
    "github": {
        "commit": "6afeca0cfb09bfa3c25eccc2bc146ccc560bbc85",
        "repository": "https://github.com/ursacomputing/conbench-example"
    },
    "machine_info": {
        "architecture_name": "arm64",
        "cpu_core_count": "8",
        "cpu_frequency_max_hz": "0",
        "cpu_l1d_cache_bytes": "65536",
        "cpu_l1i_cache_bytes": "131072",
        "cpu_l2_cache_bytes": "4194304",
        "cpu_l3_cache_bytes": "0",
        "cpu_model_name": "Apple M1",
        "cpu_thread_count": "8",
        "gpu_count": "0",
        "gpu_product_names": [],
        "kernel_name": "20.6.0",
        "memory_bytes": "17179869184",
        "name": "diana",
        "os_name": "macOS",
        "os_version": "11.5.2"
    },
    "run_id": "e02e6c3591c24375b959499ccd667eb6",
    "stats": {
        "data": [
            "0.000001",
            "0.000000",
            "0.000000",
            "0.000000",
            "0.000000"
        ],
        "iqr": "0.000000",
        "iterations": 5,
        "max": "0.000001",
        "mean": "0.000000",
        "median": "0.000000",
        "min": "0.000000",
        "q1": "0.000000",
        "q3": "0.000000",
        "stdev": "0.000001",
        "time_unit": "s",
        "times": [],
        "unit": "s"
    },
    "tags": {
        "name": "add"
    },
    "timestamp": "2021-09-05T05:06:12.586697+00:00"
}
 ```
