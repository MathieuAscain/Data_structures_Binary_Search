# Data Structure - Binary Search #
Binary search program made in *Python*

## First step ##
First all elements are integrated into a list while the user press Yes (Y or y).
Control if the value is a number

## Second step ##
Then an element to be searched is requested to the user named *target*
Control if *target* is a number

## Third step ##
Use of a recursive function to look for the *target*
### Recursive binary search function parameters ###
*left* parameter is set to the first element of the list
*right* parameter is set to the last element of the list
*target* is the local variable within the binary search function which stores the value to be searched

### Case if the target is in the list ###
The recursive function will check if the *middle* is higher or lower the *target* and will 
call the recursive function by reducing the range in case *target* has not been found in the *middle*

### Case if the target is not in the list ###
In this case *right* and *left* parameters will not fulfill right >= left,
then the *recursive binary search* function will return -1

## Fourth step ###
Depending on the result returned it will show to the terminal if the *target* has been found or not.
