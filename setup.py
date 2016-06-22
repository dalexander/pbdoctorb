from setuptools import setup

setup(
    name = 'pbdoctorb',
    version = "0.3.0",
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    license=open("LICENSES.txt").read(),
    scripts = ["bin/chem",
               "bin/baxSieve",
               "bin/baxSlimmer",
               "bin/hpLengthDistribution",
               "bin/runStats",
               "bin/summarizeUnrolledAlignments",
               "bin/trxSieve"],
    zip_safe = False,
    install_requires=["pbcore >= 1.2.6", "docopt >= 0.6.2" ]
)
