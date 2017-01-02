lk 0		load the first character x
lk 1		load the second character y
ll 48 2		load ascii conversion value
minus 0 2 0	convert from ascii to number
minus 1 2 1	convert from ascii to number
ll 0 2		loop counter
ll 0 3		working total
ll 1 4		load loop incremental value
ll 9 5		load jump destination
add 0 3 3	add x to working total
add 4 2 2	increment loop counter
jlt 2 1 5 7	if loop counter < x then jump back to the top