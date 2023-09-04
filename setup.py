from setuptools import setup, find_packages

setup(
    name="YourProjectName",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'keras',
        'opencv-python',
        'pygame',
        'numpy',
    ],
    author="Amin Ravanbakhsh",
    author_email="amin.ravanbakhsh.1999@gmail.com",
    description="Warning to drivers in case of drowsiness.",
    # license="MIT",  # Or any other license you're using
    # keywords="some keywords relating to your project",
    # url="URL to your project's repository or homepage",
)