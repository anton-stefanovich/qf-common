from argparse import ArgumentParser
from qf_common import package


parser = ArgumentParser()
parser.add_argument('--username', '-u', type=str, required=True)
parser.add_argument('--password', '-p', type=str, required=True)
parser.add_argument('--files', '-f', type=list, required=True)
params = parser.parse_args()

package.share(
    params.username,
    params.password,
    params.files)
