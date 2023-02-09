import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="test_package",
    version="0.0.1",
    author="pargim",
    author_email="mohan.tita@gmail.com",
    packages=["test_package"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohankashyap/open_face_package",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
