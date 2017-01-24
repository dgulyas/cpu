pt $lit $ramAdd 0
pt $pc $1
lk $0
minus $0 $lit $ram 48 #convert ascii value into number and store in ram
add $ramAdd $lit $ramAdd 1 #increment the ram address
je $0 $lit $1 $clk #if input number was 0, jump to top of loop
