from setuptools import setup

setup(
    name = 'pbdoctorb',
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    license=open("LICENSES.txt").read(),
    scripts = ["bin/chem"],
    zip_safe = False,
    install_requires=["pbcore >= 0.8.0"]
)
