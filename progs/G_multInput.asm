lk 0			#load the first character x
lk 1			#load the second character y
minus 0 6 0	48	#convert from ascii to number
minus 1 6 1	48	#convert from ascii to number
pt 6 2 0		#loop counter
pt 6 3 0		#working total
add 0 3 3		#add x to working total (top of loop)
add 6 2 2 1		#increment loop counter by 1
jlt 2 1 6 7 6	#if loop counter < x then jump back to the top of loop
add 6 3 6 48	#Add 48 to working total and pass to screen