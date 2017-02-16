pt $lit $ramAdd 0 			#set initial ram address
add $pc $lit $1 1 			#Save the location of the next instruction, top of loop
lk $0
minus $0 $lit $0 48			#convert ascii value into number (can't store in ram because we need to compare it latter)
pt $0 $ram					#store the number in ram
add $ramAdd $lit $ramAdd 1	#increment the ram address
e $0 $lit $7 0				#test is number was 0
je $7 $lit $1 $pc 0			#if test returned false, jump to top of loop
minus $ramAdd $lit $2 1		#save ram address. It's the num elements in list
pt $lit $5 0				#set the outer loop index to 0
add $pc $lit $3 1			#save next instruction as top of outer loop
pt $lit $6 0				#set the inner loop index to 0
add $pc $lit $4 1			#save next instruction as top of inner loop
pt $6 $ramAdd				#load current element and next element into registers
pt $ram $10
add $lit $6 $ramAdd 1
pt $ram $11
jlt $10 $11 $lit $pc 24 	#test to see if we don't need to swap
je  $10 $11 $lit $pc 24
pt $10 $ram					#load data back in swapped
pt $6 $ramAdd
pt $11 $ram
add $lit $6 $6 1			#increment inner loop index
jlt $6 $2 $4 $pc			#jump to top of inner loop
add $lit $5 $5 1            #increment outer loop index
jlt $5 $2 $3 $pc			#jump to top of outer loop 
