from math import sqrt

def mean(input_array):
	for i in range(0,(len(input_array)-1)):
		input_array[i] = float(input_array[i])
	total_sum = 0.00
	for value in input_array:
		total_sum = total_sum + value
	return float(total_sum/len(input_array))

def standard_deviation(input_array):
	mu = mean(input_array)
	variance_numerator = 0.00
	for val in input_array:
		variance_numerator = variance_numerator + (val - mu)**2 #Sigma((x-mu)^2)
	variance = variance_numerator/len(input_array)
	return sqrt(variance)

def covariance(x_array, y_array):
	if len(x_array) != len(y_array):
		return "fail"
	x_mu = mean(x_array)
	y_mu = mean(y_array)
	covariance_numerator = 0.00
	for i in range(len(x_array)):
		covariance_numerator = covariance_numerator + (x_array[i] - x_mu)*(y_array[i] - y_mu)
	return covariance_numerator/len(x_array)

def correlation(x_array,y_array):
	if covariance(x_array,y_array) != "fail":
		return covariance(x_array,y_array)/((standard_deviation(x_array))*(standard_deviation(y_array)))
	else:
		return "fail"

xinp = [1,2,2,4]
yinp = [2,4,6,8]
print correlation(xinp,yinp)
