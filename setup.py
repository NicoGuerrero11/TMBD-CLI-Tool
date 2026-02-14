from setuptools import setup, find_packages

setup(
    name="tmbd-cli",
    version="1.0.0",
    description="🎬 CLI para consultar películas desde TMDB",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "click>=8.0.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tmbd=tmbd.tmbd:cli",
        ],
    },
    python_requires=">=3.7",
)
