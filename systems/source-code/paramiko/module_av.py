#!/usr/bin/env python

from argparse import ArgumentParser
import ssh
import sys


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='do ls on remote server')
    arg_parser.add_argument('--host', required=True,
                            help='host name to connect to')
    arg_parser.add_argument('--user', required=True,
                            help='user name to connect as')
    arg_parser.add_argument('module', help='module to query for')
    options = arg_parser.parse_args()
    ssh = ssh.connect(options.host, options.user)
    cmd = f'bash -l -c module av {options.module};'
    _, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    for line in stdout:
        print(line.rstrip())
    for line in stderr:
        print(line.rstrip(), file=sys.stderr)
    ssh.close()
