# An example project using Conbench

- https://github.com/ursacomputing/conbench


```
conbench-example
├── LICENSE
├── README.md
├── example
│   ├── __init__.py
│   ├── benchmarks
│   │   ├── __init__.py
│   │   └── benchmark_math.py                      (benchmark the code)
│   ├── math.py                                    (the code)
│   └── tests
│       ├── __init__.py
│       ├── benchmarks
│       │   ├── __init__.py
│       │   └── test_benchmark_math.py             (test the benchmarks)
│       └── test_math.py                           (test the code)
├── requirements-test.txt
└── setup.py
```

## Quick start


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


## Contributing


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
example/tests/test_math.py::test_add PASSED
example/tests/test_math.py::test_subtract PASSED
example/tests/benchmarks/test_benchmark_math.py::test_benchmark_add PASSED
example/tests/benchmarks/test_benchmark_math.py::test_benchmark_substract PASSED
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
