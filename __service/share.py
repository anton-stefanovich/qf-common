from argparse import ArgumentParser
from qf_common import package


parser = ArgumentParser()
parser.add_argument('--username', '-u', type=str, required=True)
parser.add_argument('--password', '-p', type=str, required=True)
params = parser.parse_args()

package.share(
    params.username,
    params.password,
    package.create(
        name='qf-common', packages=['qf_common'],
        description='Useful things for QF projects',
        url='https://github.com/quality-first/qf-common',
    ))
