import setuptools
import os
from pathlib import Path

root = Path(os.path.realpath(__file__)).parent
version_file = root / "src" / "dsp" / "VERSION"
readme_file = root / "readme.rst"

extras_require = {}

setuptools.setup(
    name="dsp",
    version=version_file.read_text().strip(),
    license="MIT",
    description="Dyson sphere program recipe calculator.",
    keywords="dyson sphere program",
    long_description=readme_file.read_text(),
    long_description_content_type="text/x-rst",

    url="https://pypi.org/project/dsp",
    download_url="https://pypi.org/project/dsp",
    project_urls={
        "Source": "https://github.com/felix-hilden/dsp",
        "Issues": "https://github.com/felix-hilden/dsp/issues",
    },

    author="Felix Hildén",
    author_email="felix.hilden@gmail.com",
    maintainer="Felix Hildén",
    maintainer_email="felix.hilden@gmail.com",

    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,

    entry_points={
        "console_scripts": [
            "dsp = dsp.cli:main",
        ],
    },

    python_requires=">=3.7",
    install_requires=[
        'PyQt6',
    ],
    extras_require=extras_require,

    classifiers=[],
)
