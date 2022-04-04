# Pi_thon

Pi_thon is a script that tells you if your code is Pi-rfect or not.
All your rows length should corresponde with correlating pi digit. Comments do not count.<br><br>
Example<br>
```python
# This is working Python and Pi_thon script

n=4               # 3.
0                 # 1
s = (n            # 4
	*         # 1
	 n ** 2)  # 4
print(s,)         # 9
```
```
64

Process finished with exit code 0
```
Is this stupid? Yes. Should you or I try to make something more complicated from this? Why not?

## Installation

Clone this repo and install requirements.txt
```
$ git clone https://github.com/SerhiiStets/Pi_thon.git
$ pip install -r /path/to/requirements.txt
```

## Usage
```
$ python pi_thon.py --help

  Pi_thon

  Usage
    $ python pi_thon.py [<options> ...]

  Options
    -h, --help             show this help message and exit
    -r, --run              run the Pi_thon script
    -c, --clean            clean Pi_thon script from Pi_thon comments
    -v, --version          show program's version number and exit
```

## Example

### Usage Examples
```
$ python pi_thon.py -r examples/
$ python pi_thon.py --run examples/is_even.py
$ python pi_thon.py -c examples/
$ python pi_thon.py --clean examples/is_even.py
```
### Right Pi_thon script example
This script shows if single digit number is even or odd
`pi = 3,141592653589`
```python
# -*- coding: utf-8 -*-
n=4                       # 3.
0                         # 1
if (n                     # 4
	%                 # 1
	4/2):             # 4
	print("E"         # 9
		  ""      # 2
		  "ven")  # 6
else:                     # 5
	n=1               # 3
	s="O"             # 5
	s = s + "dd"      # 8
	print(s,)         # 9

```


## Contributing

All bugs, feature requests, pull requests, feedback, etc., are welcome. [Create an issue](https://github.com/SerhiiStets/Pi_thon/issues)
