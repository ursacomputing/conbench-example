import conbench.runner

import example.math


@conbench.runner.register_benchmark
class BenchmarkAdd(conbench.runner.Benchmark):
    name = "add"

    def run(self, **kwargs):
        yield self.conbench.benchmark(
            self._get_benchmark_function(),
            self.name,
            options=kwargs,
        )

    def _get_benchmark_function(self):
        return lambda: example.math.add(1, 1)


@conbench.runner.register_benchmark
class BenchmarkSubtract(conbench.runner.Benchmark):
    name = "subtract"

    def run(self, **kwargs):
        yield self.conbench.benchmark(
            self._get_benchmark_function(),
            self.name,
            options=kwargs,
        )

    def _get_benchmark_function(self):
        return lambda: example.math.subtract(100, 1)
