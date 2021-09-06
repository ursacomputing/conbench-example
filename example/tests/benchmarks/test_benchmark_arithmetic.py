from example.benchmarks import benchmark_arithmetic
from example.tests.benchmarks import _asserts

ADD_HELP = """
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
"""


SUBSTRACT_HELP = """
Usage: conbench subtract [OPTIONS]

  Run subtract benchmark.

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
"""


def _assert_benchmark(result, name):
    assert result["tags"] == {"name": name}
    assert result["context"]["benchmark_language"] == "Python"


def test_benchmark_add():
    benchmark = benchmark_arithmetic.BenchmarkAdd()
    [(result, output)] = benchmark.run(iterations=1)
    _assert_benchmark(result, "add")
    assert output == 2  # 1 + 1 = 2


def test_benchmark_add_cli():
    command = ["conbench", "add", "--help"]
    _asserts.assert_cli(command, ADD_HELP)


def test_benchmark_substract():
    benchmark = benchmark_arithmetic.BenchmarkSubtract()
    [(result, output)] = benchmark.run(iterations=1)
    _assert_benchmark(result, "subtract")
    assert output == 99  # 100 - 1 = 99


def test_benchmark_substract_cli():
    command = ["conbench", "subtract", "--help"]
    _asserts.assert_cli(command, SUBSTRACT_HELP)
