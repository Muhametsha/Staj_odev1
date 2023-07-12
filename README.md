# Homewrork1
#Target Finding

This program aims to find the target number in a given sequence of numbers. If the target number is found in the array, the program prints its index.
If the target number is not found in the array, the program inserts the target number in the order of the list and reorders the array.
## How to use

1. Run the program.
2. Enter a string of numbers. Enter numbers separated by commas. For example: "1, 2, 4, 8"
3. Enter the target number.
4. The program prints the index of the target number or its index in the inserted and sorted array.
### Example :

Entry:
search_find([1, 2, 4, 8], 4)
search_find([2, 4, 5, 8], 3)
Output:
2
1
-----------------------------------------------------------------------------------------------------
 # Homework2
 This code changes the rows of the type 'Iris-setosa' in the dataset to 'apple' and prints the results to the screen. 
 
 Then it saves the updated DataFrame to an Excel file.
----------------------------------------------------------------------------------------------------------
 # Homework3 
The given code performs data normalization on the Iris dataset using a for loop. Here is an explanation of the code in English:

   Import the necessary libraries: pandas and numpy.
   Define the file path of the Iris dataset.
   Read the CSV file into a pandas DataFrame using the read_csv() function, storing it in the variable df.
   Remove the last column of the DataFrame since we only want to normalize the numerical columns. The columns to be normalized are stored in the columns_to_normalize variable.
   Create an array (asv) containing the values of the columns to be normalized.
   Initialize an empty list normalized_data to store the normalized columns.
   Iterate over each column in the asv array.
   For each column, extract the column data and store it in the column_data variable.
   Compute the normalized column values using the formula: (value - min) / (max - min), where min is the minimum value in the column and max is the maximum value.
   Append the normalized column to the normalized_data list.
   After iterating over all columns, transpose the normalized_data list to match the shape of the original data.
   Create a new DataFrame (normalized_df) using the transposed normalized data and the original column names.
   Print the normalized Iris dataset.

The code normalizes the numerical columns of the Iris dataset, ensuring that each column's values are scaled to a range between 0 and 1.
