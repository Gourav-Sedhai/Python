from itertools import accumulate 

Input = [1, 2, 3, 4, 5, 6, 7, 8, 9]


split = [2, 2, 2, 2, 2] 

Output = [Input[x - y: x] for x, y in zip( 
          accumulate(split), split)] 
  
print("Input", Input, '2') 
print("Output", Output) 
