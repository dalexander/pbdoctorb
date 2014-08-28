from setuptools import setup

setup(
    name = 'pbdoctorb',
    version = "0.1.0",
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    license=open("LICENSES.txt").read(),
    scripts = ["bin/chem",
               "bin/baxSieve",
               "bin/baxSlimmer",
               "bin/runStats"],
    zip_safe = False,
    install_requires=["pbcore >= 0.8.0"]
)
