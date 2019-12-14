#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Constant time complexity - O(1) - This while loop in this function will always run only twice. By the second iteration, it will have terminated due to a > n^3. 

b) Quadratic time complexity - O(n^2) - The nested loops indicates that the function will run n^2 times.

c) Linear time complexity - O(n) - The function will call itself recursively n times.

## Exercise II

Since we are trying to find a value (f) that should be included within the range of 0 through n(building height), we can perform a binary search to find the value (f). We can do a search because we can know the range from 0 to n is sorted. A binary search will run at O(log n) time complexity since it n input is being cut in half every new iteration.

find(building, floor)
   bottom = 0
   top = length of building - 1
   ## These variables will change depending on the new size of the range, which should reduce by half every time

   while (bottom <= top) 
   ## This starts by looking at the entire range
   ## middle = bottom + top / 2, it will terminate once they cross
      
      if middle < floor 
   ## If not in left half
         bottom = middle + 1 
   # Sets new range to only the right half

      if middle > floor 
   # If not in right half
         top = middle - 1 
   # Sets new range to only the left

      if middle = floor
         return middle  
   ## This is floor we are looking for

   



