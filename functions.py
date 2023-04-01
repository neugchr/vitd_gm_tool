# functions.py
import re

def solve_op(formula_string):	# need not be given a string with parentheses
	# we search for ** signs with numbers to the left and right and replace it by a^b
	ptrn = re.compile('([0-9\.\,]+)(\*\*)([0-9\.\,]+)')
	x = ptrn.search(formula_string)
	while x:
		lh = float(x.group(1))
		rh = float(x.group(3))
		res = lh**rh
		formula_string = ptrn.sub(str(res), formula_string, count =1)
		x = ptrn.search(formula_string)
	# next multiplication
	ptrn = re.compile('([0-9\.\,]+)(\*)([0-9\.\,]+)')
	x = ptrn.search(formula_string)
	while x:
		lh = float(x.group(1))
		rh = float(x.group(3))
		res = lh*rh
		formula_string = ptrn.sub(str(res), formula_string, count =1)
		x = ptrn.search(formula_string)
	# division
	ptrn = re.compile('([0-9\.\,]+)(\/)([0-9\.\,]+)')
	x = ptrn.search(formula_string)
	while x:
		lh = float(x.group(1))
		rh = float(x.group(3))
		res = lh/rh
		formula_string = ptrn.sub(str(res), formula_string, count =1)
		x = ptrn.search(formula_string)
	# addition
	ptrn = re.compile('([0-9\.\,]+)(\+)([0-9\.\,]+)')
	x = ptrn.search(formula_string)
	while x:
		lh = float(x.group(1))
		rh = float(x.group(3))
		res = lh+rh
		formula_string = ptrn.sub(str(res), formula_string, count =1)
		x = ptrn.search(formula_string)
	# subtraction
	ptrn = re.compile('([0-9\.\,]+)(\-)([0-9\.\,]+)')
	x = ptrn.search(formula_string)
	while x:
		lh = float(x.group(1))
		rh = float(x.group(3))
		res = lh-rh
		formula_string = ptrn.sub(str(res), formula_string, count =1)
		x = ptrn.search(formula_string)
	return(formula_string)


def solve(formula_string):
	formula_string.replace('{','(').replace('}',')').replace('[','(').replace(']',')')
	ptrn = re.compile('([\(]){1}([^\(]+?)([\)]{1})')	# search for inner brackets
	x = ptrn.search(formula_string)
	while x:
		formula_string = ptrn.sub(str(solve_op(x.group(2))), formula_string, count =1)
		x = ptrn.search(formula_string)
	return(solve_op(formula_string))

