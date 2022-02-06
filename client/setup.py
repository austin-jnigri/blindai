import os
import setuptools
import subprocess
import platform
import re
import sys
from setuptools import Extension
from setuptools.command.build_ext import build_ext 


#Build the third party library
subprocess.check_call(["./scripts/build"])

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

def find_version():
    version_file = read("blindai/version.py")
    version_re = r"__version__ = \"(?P<version>.+)\""
    version = re.match(version_re, version_file).group("version")
    return version

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def build_extension(self, ext):

        if platform.system() == "Windows":
            raise RuntimeError("Currently, the library can only be built on linux")

        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        cfg = "Debug" if debug else "Release"

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",
        ]
        
        build_args = []

        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or PyPA-build.
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += [f"-j{self.parallel}"]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=self.build_temp
        )
        subprocess.check_call(['./scripts/edit_runpath'])

setuptools.setup(
    name="blindai",
    author="Mithril-Security",
    version=find_version(),
    author_email="contact@mithrilsecurity.io",
    description="A python library for creating gRPC clients for blindai inference server",
    license="",
    keywords="confidential computing inference client enclave",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["lib/*.so", "tls/*.pem"]},
    ext_modules=[CMakeExtension("pybind11_module")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    python_requires=">=3.6.8",
    install_requires=[
       "cryptography>=35.0.0",
       "toml",
       "grpcio",
       "grpcio-tools",
       "bitstring"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ",
        "Operating System :: Linux",
    ],
)