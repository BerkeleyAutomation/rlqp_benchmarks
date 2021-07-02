import setuptools


# https://stackoverflow.com/questions/57744466/how-to-properly-structure-internal-scripts-in-a-python-project
setuptools.setup(
    name="rlqp_benchmarks",
    version="1.0.0",
    author="anonymous",
    author_email="anonymous",
    description="RLQP training code and scripts",
    install_requires=[
        'pandas',
        'osqp', # 0.6.2.post0
        'cvxpy', # 1.1.13
    ]#,
#    packages=["rlqp_train"]
)
