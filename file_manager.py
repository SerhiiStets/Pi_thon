# -*- coding: utf-8 -*-
"""
Module for working with files (rewriting or reading scripts)
"""

def read_script(script : str, path : str='') -> list:
	"""
	Read through script and returns list of line without \n character

	Parameters
	----------
	script : str
		Script name
	path : str
		Path to script

	Returns
	-------
	list
		List of lines without \n character
	"""

	try:
		with open(path + script, 'r', encoding="utf-8") as file:
			return file.read().splitlines()
	except IOError:
		print(f"{path + script} - No such file or directory")
		return []


def rewrite_script(new_file_arr : list, script : str, path : str=""):
	"""
	Takes reworked list of lines, script name/path and rewrites it with new data

	Parameters
	----------
	new_file_arr : list
		Reworked list of lines from file
	script : str
		Script name
	path : str
		Path to script
	"""

	with open(path + script, 'w', encoding="utf-8") as file:
		file.write('\n'.join(new_file_arr))
