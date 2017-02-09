
pt $lit $ramAdd 0 #set initial ram address
add $pc $lit $1 1 #Save the location of the next instruction, top of loop
lk $0
minus $0 $lit $ram 48		#convert ascii value into number and store in ram
add $ramAdd $lit $ramAdd 1	#increment the ram address
e $0 $lit $7 0
invert $7 $7
je $7 $lit $1 $pc 0			#if input number was 0, jump to top of loop
pt $ramAdd $2				#save ram address. That's how many elements are in our "list" - 1
pt $lit $5 0				#set the outer loop index to 0
add $pc $lit $3 1			#save next instruction as top of outer loop
pt $lit $6 0				#set the inner loop index to 0
add $pc $lit $4 1			#save next instruction as top of inner loop
pt $6 $ramAdd				#load current element and next into registers
pt $ram $10
add $lit $6 $ramAdd 1
pt $ram $11
jlt $10 $11 $lit $pc 22 	#test to see if we don't need to swap
je  $10 $11 $lit $pc 22
pt $10 $ram					#load data back in swapped
pt $6 $ramAdd
pt $11 $ram
add $lit $6 $6 1			#increment inner loop index
jlt $6 $2 $4 $pc			#jump to top of inner loop
add $lit $5 $5 1            #increment outer loop index
jlt $5 $2 $3 $pc			#jump to top of outer loop 
