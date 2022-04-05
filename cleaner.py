# -*- coding: utf-8 -*-
"""
Cleaner module to remove # Pi_Error comments from .py files
"""

import argparse

from os import walk

from file_manager import read_script, rewrite_script


def remove_comments(file_arr : list) -> list:
	"""
	Takes list, removes Pi_thon comments from elements and returns clean list

	Parameters
	----------
	file_arr : list
		Original file as list of lines

	Returns
	-------
	list
	"""
	clean_file_arr = file_arr
	for i, line in enumerate(file_arr):
		if "Pi_Error" in line:
			clean_file_arr[i] = file_arr[i].split(" # Pi_Error")[0]
	return clean_file_arr


def cleaner(pi_thon_scripts : str):
	"""
	Cleans .py files from comments left by Pi_thon script
	Ex: # Pi_Error: number of character = 12, pi number = 7

	Parameters
	----------
	pi_thon_scripts : str
		Received file/folder as an argument from args
	"""

	if "." in pi_thon_scripts:
		file_arr = read_script(pi_thon_scripts)
		clean_file_arr = remove_comments(file_arr)
		rewrite_script(clean_file_arr, pi_thon_scripts)
	else:
		file_names = next(walk(pi_thon_scripts), (None, None, []))[2]
		for script in file_names:
			if "." in script:
				file_arr = read_script(script, pi_thon_scripts)
				clean_file_arr = remove_comments(file_arr)
				rewrite_script(clean_file_arr, script, pi_thon_scripts)
			else:
				print(f"{script} - is not a Python file")
	print(f"{pi_thon_scripts} is cleaned")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Pi_thon cleaner")
	parser.add_argument("-c", "--clean", type=str,
						help="clean Pi_thon script from Pi_thon comments", nargs=1, required=True)
	args = parser.parse_args()
	cleaner(args.clean[0])
