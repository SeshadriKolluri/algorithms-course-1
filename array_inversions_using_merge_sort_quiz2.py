# Recurvsive method for computing the number of inversions in an array
# This algorithm works very similar to merge sort, but also computes inversions along the way

# Compute number of inversions using merge sort 
def compute_inversions(number_list):
	#print number_list

	if len(number_list) < 2: 
		sorted_list = number_list
		inversions = 0

	else:

		array_length = len(number_list)
		#Left half of the array (approximately)
		left_array = number_list[:int(array_length/2)]
		(sorted_left_half, left_inversions) = compute_inversions(left_array)


		#Right half of the array (approximately)
		right_array = number_list[int(array_length/2):]
		(sorted_right_half,right_inversions) = compute_inversions(right_array)

		# initialize an empty list
		sorted_list = []
		#Number of inversion where the first element is in the left half of array and right half of the array
		mixed_inversions = 0 

		# initialize the index to zero for the merge sort
		left_index = 0
		right_index = 0

		#merging the two sub arrays and computing the number of mixed inversions
		while left_index < len(sorted_left_half) and right_index < len(sorted_right_half):
			if sorted_left_half[left_index] < sorted_right_half[right_index]:
				sorted_list.append(sorted_left_half[left_index])
				left_index = left_index + 1
			else:
				sorted_list.append(sorted_right_half[right_index])
				right_index = right_index + 1
				mixed_inversions = mixed_inversions + len(sorted_left_half) - left_index

		#print sorted_left_half, left_index, sorted_right_half, right_index
		#if we already went through the left half, just append the right half
		if left_index == len(left_array):
			sorted_list = sorted_list + sorted_right_half[right_index:]
		#if we already went through the right half, just append the left half
		if right_index == len(right_array):
			sorted_list = sorted_list + sorted_left_half[left_index:]
			
		# add the left, right and mixed inversions to get total number of inversions
		inversions = left_inversions + right_inversions + mixed_inversions
	return sorted_list,inversions

import random

#read the file into a list and strip all the white space charaters
f = open('IntegerArray.txt','r')
number_list = [int(number.strip()) for number in f.readlines()]

#test a small array of randomly shuffled numbers. 
test_set = range(1,11)
random.shuffle(test_set)

print test_set
sorted_list,inversions = compute_inversions(test_set)

print sorted_list
print inversions

sorted_list,inversions = compute_inversions(number_list)
print inversions

