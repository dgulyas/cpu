l 3 0		load the first number
l 4 1		load the second number
l 0 2		loop counter
l 0 3		working total
l 1 4		load loop incremental value
l 6 5		load jump destination
add 0 3 3	add x to working total
add 4 2 2	increment loop counter
jlt 2 1 5 7	if loop counter < x then jump back to the top