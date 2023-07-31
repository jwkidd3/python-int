# Argparse

`argparse` is a module in Python's standard library to handle command
line arguments.

## What is it?

1. `generate_gaussians.py`: generate random numbers from a Gaussian
distribution, use the `-h` options to display help on the command
line options. 
```bash
$ ./generate_gaussian.py -h
```
1. `partial_parse.py`: illustrate how to parse only known arguments.
1. `two_stage_parse.py`: parsing input from a file as if it were command
   line arguments (using `shlex`) and merging with command line arguments.
   ```bash
   $ ./two_stage_parse.py  -l mem=8gb -I job_script.pbs -k oe
   ```
1. `job_script.pbs`: file to use with `two_stage_parse.py`.
1. `options_in_file.py`: illustration of how to read options from a file.
   ```bash
   ./options_in_file.py --foo something @file_options.txt
   ```
1. `file_options.txt`: file containing options for `options_in_file.py`.
