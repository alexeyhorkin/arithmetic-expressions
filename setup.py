from setuptools import setup  # type: ignore


packages = {
    'calculator': 'calculator/'
}

setup(
    name="calculator",
    version='0.0.1',
    author="Alexey, Khorkin",
    license="MIT",
    description="Module for simple arithmetic calculation",
    packages=packages,
    package_dir=packages,
    include_package_data=False
)
