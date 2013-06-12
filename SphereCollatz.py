import sys

#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
  reads two ints into a[0] and a[1]
	r is a reader
	a is an array of int
	return true if that succeeds, false otherwise
	"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    #assert i < j
    v = 1
    if i > j :
        temp = i
        i = j
        j = temp
    if i < j / 2 :
        i = j / 2
    for k in range(i, j):
        c = 1
        #k = i
        while k > 1 :
            if (k % 2) == 0 :
                k = (k / 2)
                c += 1
            else :
                k = (1.5 * k) + 0.5 #k = (3 * k) + 1
                c += 2
        if (v < c) :
            v = c
        i+=1
    """	
    v = 1
	while(i < j):
		k = i; # new i that can be changed
		while (i > 1):
			n = 0
			if (k%2 == 1):
				k = (3*k) + 1
				n+=1 # increment the counter
			else:
				k = k/2
				n+=1 # increment the counter
			
			if (v < n):
				v = n
				
			i+=1
    """
    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
prints the values of i, j, and v
w is a writer
i is the beginning of the range, inclusive
j is the end of the range, inclusive
v is the max cycle length
"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")  # what is str(i)???

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)



#!/usr/bin/env python

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
% python RunCollatz.py < RunCollatz.in > RunCollatz.out
% chmod ugo+x RunCollatz.py
% RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
% pydoc -w Collatz
"""

# -------
# imports
# -------



#from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
