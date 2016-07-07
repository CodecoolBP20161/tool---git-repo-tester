#!/usr/bin/python3
import subprocess
import os
import sys
import random


def run(command_list):
    process = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    error = process.stderr.decode("utf-8")  # returning the stderr text, if any
    if len(error) > 0:
        return error
    return process.stdout.decode("utf-8")


def main():
    if len(sys.argv) <= 1:
        raise ValueError('git repo url is expected as the first argument for this script')

    script_to_run = 'test.py'
    if len(sys.argv) > 2:
        script_to_run = sys.argv[2]

    # Possible links
    # "git@github.com:CodecoolBP20161/sql-native-basic-exercises-Csyk.git"
    # "https://github.com/CodecoolBP20161/sql-native-basic-exercises-Csyk"
    # "https://github.com/CodecoolBP20161/sql-native-basic-exercises-Csyk.git"
    url = sys.argv[1].replace('.git', '')
    repo_name = url[url.rfind('/') + 1:] + '-' + str(random.randint(1000, 9999))
    url = url.replace('https://github.com/', 'git@github.com:') + '.git'

    run(['git', 'clone', url, repo_name])
    os.chdir(repo_name)
    print(run(['python3', script_to_run]))
    os.chdir('..')


if __name__ == '__main__':
    main()
