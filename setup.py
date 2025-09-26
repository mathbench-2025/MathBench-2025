from setuptools import setup, find_packages

setup(
    name="mathbench2025",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.1",
        "tqdm>=4.66",
        "jsonschema>=4.18",
        "openai>=1.0"
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'mathbench-eval = examples.run_eval_example:main',
        ],
    },
    include_package_data=True,
    description="MathBench-2025: Benchmark for evaluating mathematical reasoning in LLMs",
    author="Anonymous",
    url="https://github.com/yourname/MathBench2025",
    license="MIT",
)
