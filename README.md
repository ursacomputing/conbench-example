# Example project using Conbench

Conbench is a language-independent, Continuous Benchmarking (CB) framework. 

- https://github.com/ursacomputing/conbench

The suggested project structure for benchmarks mirrors your project structure
for tests. The pytest docs cover common project structures and their pros and
cons.

- https://docs.pytest.org/en/6.2.x/goodpractices.html#choosing-a-test-layout-import-rules

```
conbench-example
├── LICENSE
├── README.md
├── example
│   ├── .conbench                              (conbench credentials, do not commit)
│   ├── __init__.py
│   ├── benchmarks
│   │   ├── __init__.py
│   │   └── benchmark_arithmetic.py            (benchmark the code)
│   ├── arithmetic.py                          (the code)
│   └── tests
│       ├── __init__.py
│       ├── benchmarks
│       │   ├── __init__.py
│       │   ├── _asserts.py                    (custom asserts)
│       │   └── test_benchmark_arithmetic.py   (test the benchmarks)
│       ├── conftest.py                        (pytest configuration)
│       └── test_arithmetic.py                 (test the code)
├── requirements.txt
├── requirements-test.txt
└── setup.py
```

Like a project with tests, a project with benchmarks: 

- has a `benchmarks` directory just like a `tests` directory
- prefixes benchmark files with `benchmark_*.py` just like `test_*.py` for tests

To run benchmarks using the Conbench CLI, `cd` into the directory containing
your benchmarks. 

    $ cd conbench-example/example/benchmarks/
    
Or more optimally, if you've placed your benchmarks in a directory called
`benchmarks`, you can run your benchmarks from the top-level of your project.  

    $ cd conbench-example/example/

For benchmark discovery, the Conbench CLI looks for files that start with
`benchmark`, or end with either `benchmark.py` or `benchmarks.py`.

To publish benchmark results to a Conbench server, Conbench will look for a
`.conbench` file in either the directory containing benchmarks, or one level
higher alongside your `benchmarks`s directory. For example:

    conbench-example/example/.conbench 
    
    -- or --
    
    conbench-example/example/benchmarks/.conbench 


The `.conbench` file contains the URL of the Conbench server to publish results
to, as well as the benchmarking user credentials.    

    $ cat .conbench 
    url: http://localhost:5000
    email: conbench@example.com
    password: conbench

Like all code, benchmarks should be tested for correctness. Basic example
benchmark tests can be found here: 

- [test_benchmark_arithmetic.py](https://github.com/ursacomputing/conbench-example/blob/main/example/tests/benchmarks/test_benchmark_arithmetic.py)


Refer to the Conbench README for more complete documentation.

- https://github.com/ursacomputing/conbench


### Create workspace
    $ cd
    $ mkdir -p envs
    $ mkdir -p workspace


### Create virualenv
    $ cd ~/envs
    $ python3 -m venv example
    $ source example/bin/activate


### Clone repository
    (example) $ cd ~/workspace/
    (example) $ git clone https://github.com/ursacomputing/conbench-example.git


### Install dependencies
    (example) $ cd ~/workspace/conbench-example/
    (example) $ pip install -r requirements.txt
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
    (example) $ cd ~/workspace/conbench-example/
    (example) $ pytest -vv example/tests/

```
tests/test_arithmetic.py::test_add PASSED
tests/test_arithmetic.py::test_subtract PASSED
tests/benchmarks/test_benchmark_arithmetic.py::test_benchmark_add PASSED
tests/benchmarks/test_benchmark_arithmetic.py::test_benchmark_add_cli PASSED
tests/benchmarks/test_benchmark_arithmetic.py::test_benchmark_substract PASSED
tests/benchmarks/test_benchmark_arithmetic.py::test_benchmark_substract_cli PASSED

```


### Generate coverage report
    (example) $ cd ~/workspace/conbench-example/
    (example) $ coverage run --source example -m pytest tests 
    (example) $ coverage report -m
    
```
coverage report -m
coverage report -m
Name                                                    Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------
example/__init__.py                                         0      0   100%
example/arithmetic.py                                       4      0   100%
example/benchmarks/__init__.py                              0      0   100%
example/benchmarks/benchmark_arithmetic.py                 16      0   100%
example/tests/__init__.py                                   0      0   100%
example/tests/benchmarks/__init__.py                        0      0   100%
example/tests/benchmarks/_asserts.py                        7      0   100%
example/tests/benchmarks/test_benchmark_arithmetic.py      27      0   100%
example/tests/conftest.py                                   2      0   100%
example/tests/test_arithmetic.py                            5      0   100%
-------------------------------------------------------------------------------------
TOTAL                                                      61      0   100%
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
 