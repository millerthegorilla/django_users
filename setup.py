import os

from setuptools import find_packages, setup

# Optional project description in README.md:

current_directory = os.path.dirname(os.path.abspath(__file__))

try:

    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:

        long_description = f.read()

except Exception:

    long_description = "django_users a basic auth app for django."

setup(
    # Project name:
    name="django-users",
    # Packages to include in the distribution:
    packages=find_packages(","),
    # Project version number:
    version="0.0.1",
    # List a license for the project, eg. MIT License
    license="MIT",
    # Short description of your library:
    description="A simple django app that includes basic user auth",
    # Long description of your library:
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Your name:
    author="James Miller",
    # Your email address:
    author_email="jamesstewartmiller@gmail.com",
    # Link to your github repository or website:
    url="https://github.com/millerthegorilla/django_users",
    # Download Link from where the project can be downloaded from:
    download_url="",
    # List of keywords:
    keywords=["django", "django_users", "user app"],
    # List project dependencies:
    install_requires=[
        "django>=4.0.1",
        "django_email_verification>=0.2.2",
        "PyJWT>=2.4.0",
        "fuzzywuzzy>=0.18.0",
        "django-recaptcha>=3.0.0",
        "django-crispy-forms>=1.14.0",
        "crispy_bootstrap5>=0.6",
        "python-Levenshtein>=0.12.2",
        "faker>=14.2",
        "django-recaptcha>=3.0.0",
        "pytest>=7.1.2",
        "seleniumbase>=4.2.0",
        "pytest-mock>=3.8.2",
        "pytest-cov>=3.0.0",
        "pytest-django>=4.5.2",
        "pytest-randomly>=3.12",
        "pytest-clarity>=1.0.1",
        "pytest-bdd>=6.0.1",
        "pytest-xdist>=2.5.0",
    ],
    # https://pypi.org/classifiers/
    classifiers=[
        "DevelopmentStatus::2-Pre-Alpha",
        "Framework::Django CMS",
        "Framework::Django::4.0",
    ],
)
