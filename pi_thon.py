# -*- coding: utf-8 -*-
"""
Pi_thon

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

	mp.dps = len(file_arr)
	pi_str = str(mp.pi).replace('.', '')
	new_file_arr = file_arr
	i = err_counter = 0
	for j, line in enumerate(file_arr):
		# TODO : """ type of comments
		# TODO : if # in the line
		if len(line.replace(' ', '')) == 0 or line.replace(' ', '').replace('	', '')[0] == '#':
			i -= 1
		else:
			line_len = len(line.replace(' ', '').replace('	', ''))
			if line_len != int(pi_str[i]):
				err_counter += 1
				new_file_arr[j] += f" # Pi_Error: number of character = {line_len}, pi number = {pi_str[i]}"
		i += 1
	if err_counter > 0:
		print(f"Found {err_counter} errors in {path + script}")
	else:
		print("Congratulations, {path + script} is PIrfect!")
	rewrite_script(new_file_arr, script, path)


def pi_thon(pi_thon_scripts : str):
	"""
	Takes .py files and send them to pi_checker()

	Parameters
	----------
	pi_thon_scripts : str
		Received file/folder as an argument from args
	"""

	if pi_thon_scripts[-3:] == ".py":
		file_arr = read_script(pi_thon_scripts)
		pi_checker(file_arr, pi_thon_scripts)
	else:
		file_names = next(walk(pi_thon_scripts), (None, None, []))[2]
		for script in file_names:
			if script[-3:] == ".py":
				file_arr = read_script(script, pi_thon_scripts)
				pi_checker(file_arr, script, pi_thon_scripts)
			else:
				print(f"{script} - is not a Python file")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Pi_thon")
	parser.add_argument("-r", "--run", type=str, help="run the Pi_thon script", nargs=1)
	parser.add_argument("-c", "--clean", type=str, help="clean Pi_thon script from Pi_thon comments", nargs=1)
	args = parser.parse_args()

	if args.run:
		pi_thon(args.run[0])
	elif args.clean:
		cleaner(args.clean[0])
