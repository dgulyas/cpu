l 3 0		load the first number (3)
l 4 1		load the second number (4)
l 0 2		loop counter
l 0 3		working total
l 1 4		load loop incremental value (1)
l 6 5		load jump destination (operation number 6)
add 0 3 3	add first number to working total
add 4 2 2	increment loop counter
jlt 2 1 5 7	if loop counter < x then jump back to the top