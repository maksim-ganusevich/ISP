from setuptools import setup

setup(
    name = "lab2",
    version = "1.0",
    author = "Maksim Hanusevich",
    author_email = "2001maksim49@gmail.com",
    packages = ["additional", "factory", "json_serializer", 
        "pickle_serializer", "yaml_serializer",
        "toml_serializer"],
    scripts = ["serializer.py"]
)