def IsSorted(a) :
	if len(a) == 1 :
		return True
	for i in range(1,len(a)) :
		if a[i-1] > a[i] :
			return False
	return True

# a: array, l: left, r:right, howto_pivot: first, last
def Partition(a, l, r, howto_pivot) :
	if howto_pivot == 'last' :
		swap = a[r]
		a[r] = a[l]
		a[l] = swap
	if howto_pivot == "median-of-three" :
		mid = (l+r) / 2
		# if the pivot is the last
		if (a[r] < a[l] and a[r] > a[mid]) or (a[r] > a[l] and a[r] < a[mid]) :
			swap = a[r]
			a[r] = a[l]
			a[l] = swap
		# if the pivot is the mid
		if (a[mid] < a[l] and a[mid] > a[r]) or (a[mid] > a[l] and a[mid] < a[r]) :
			swap = a[mid]
			a[mid] = a[l]
			a[l] = swap
	pivot_element = a[l]
	i = l + 1
	for j in range(l+1,r+1) :
		if a[j] < pivot_element :
			swap = a[i]
			a[i] = a[j]
			a[j] = swap
			i += 1
	swap = a[i-1]
	a[i-1] = a[l]
	a[l] = swap
	return i-1

# return: number of comparisons
def QuickSort(a, l, r, howto_pivot) :
	if l >= r :
		return 0
	pos = Partition(a, l, r, howto_pivot)
	return QuickSort(a, l, pos-1, howto_pivot) + QuickSort(a, pos+1, r, howto_pivot) +  (r-l)

print '============================'			

a = []
for line in open('QuickSort.txt') :
	a.append(int(line))

print QuickSort(a,0,len(a)-1,'first')
print IsSorted(a)
# first: 162085
# last: 164123
# median-of-three: 138382
