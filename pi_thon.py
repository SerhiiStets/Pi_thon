# -*- coding: utf-8 -*-
"""
Pi_thon

Pi_thon is a script that tells you if your code is Pi-rfect or not.
All your row's lengths should correspond with correlating pi digit.
Comments and spaces do not count.

@Author: Serhii Stets
"""

import argparse

from os import walk
from mpmath import mp

from cleaner import cleaner
from file_manager import read_script, rewrite_script


def pi_checker(file_arr : list, script : str, path : str=''):
	"""
	Checks line length with a length of correlating pi digit
	If length is not equal adds # Pi_Error comment to that line
	After going through whole file, sends new arr to rewrite_script
	to rewrite old file with new one with comments

	Parameters
	----------
	file_arr : list
        Script transformed to list of lines without \n
	script : str
		Script name
	path : str
		Path to script
	"""

	mp.dps = len(file_arr)                  # get pi with numbers of decimals as len of file
	pi_str = str(mp.pi).replace('.', '')    # pi in string format without a dot
	new_file_arr = file_arr                 # temp arr where the changes will go
	i = err_counter = 0                     # i = index to pi digit, err_counter - number of errors
	docstring_comment_flag = False          # flag to know if we are in docstring to skip counting

	# TODO : if # in the line

	for j, line in enumerate(file_arr):
		stripped_line = line.replace(' ', '').replace('	', '')

		# if docstring comment is in one line then we just skip this line
		if line.count('"""') > 1 and line.count('"""') % 2 == 0:
			continue

		if '"""' in line and docstring_comment_flag:
			# Docstring ends, set flag to False and skip line
			docstring_comment_flag = False
			continue
		elif '"""' in line:
			# Docstring starts, set flag to True
			docstring_comment_flag = True

		# Checks for right circumstances to skip like
		# If we are still in docstring, then skip since it's a comment
		# If the line is empty, also skip
		# If the line start with # then it's a comment, so also skip
		if docstring_comment_flag or len(stripped_line) == 0 or stripped_line[0] == '#':
			continue

		# If the length of line without spaces not equal certain pi digit add an Error to temp arr
		if len(stripped_line) != int(pi_str[i]):
			err_counter += 1
			new_file_arr[j] += f" # Pi_Error: number of character = {len(stripped_line)}, pi number = {pi_str[i]}"
		i += 1

	if err_counter > 0:
		print(f"Found {err_counter} errors in {path + script}")
	else:
		print(f"Congratulations, {path + script} is PI-rfect!")
	rewrite_script(new_file_arr, script, path)


def pi_thon(pi_thon_scripts : str):
	"""
	Takes .py files and send them to pi_checker()

	Parameters
	----------
	pi_thon_scripts : str
		Received file/folder as an argument from args
	"""

	if "." in pi_thon_scripts:
		file_arr = read_script(pi_thon_scripts)
		pi_checker(file_arr, pi_thon_scripts)
	else:
		file_names = next(walk(pi_thon_scripts), (None, None, []))[2]
		for script in file_names:
			if "." in script:
				file_arr = read_script(script, pi_thon_scripts)
				pi_checker(file_arr, script, pi_thon_scripts)
			else:
				print(f"{script} - is not a Python file")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Pi_thon")
	parser.add_argument("-r", "--run", type=str, help="run the Pi_thon script", nargs=1)
	parser.add_argument("-c", "--clean", type=str, help="clean Pi_thon script from Pi_thon comments", nargs=1)
	parser.add_argument("-v", "--version", action="version", version="Pi_thon 1.1")
	args = parser.parse_args()

	if args.run:
		pi_thon(args.run[0])
	elif args.clean:
		cleaner(args.clean[0])
