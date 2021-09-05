from example.benchmarks import benchmark_math


def _assert_benchmark(result, name):
    assert result["tags"] == {"name": name}
    assert result["context"]["benchmark_language"] == "Python"


def test_benchmark_add():
    benchmark = benchmark_math.BenchmarkAdd()
    [(result, output)] = benchmark.run(iterations=1)
    _assert_benchmark(result, "add")
    assert output == 2  # 1 + 1 = 2


def test_benchmark_substract():
    benchmark = benchmark_math.BenchmarkSubtract()
    [(result, output)] = benchmark.run(iterations=1)
    _assert_benchmark(result, "subtract")
    assert output == 99  # 100 - 1 = 99
