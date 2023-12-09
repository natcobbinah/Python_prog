from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer

print("Using MinMaxScaler")
data1 = ([
    [58., 1., 43.],
    [10., 200., 65.],
    [20., 75., 7.]
])

# it can be observed that the attributes in one feature has values in higher range
# compared to other attribute's values, and thus, it is often required to scale or
# normalize the attribute values in common range.

# so we can use the min-max scaler from sklearn to normalize the mean and sde to box
# all the data into a range lying between certain min and max values. Generally the
# range is set between 0 and 1.

scaled_values = MinMaxScaler(feature_range=(0,1))
results = scaled_values.fit(data1).transform(data1)
print(results)

print()

print("Using StandardScaler")
data2 = ([
    [58., 1., 43.],
    [10., 200., 65.],
    [20., 75., 7.]
])
# to use the standard-scaler, to make all the data have a similar mean, that is, a zero mean, and a
# unit variance across the data, we apply the standard-scaler algorithm
stand_scalar = StandardScaler().fit(data2)
results = stand_scalar.transform(data2)
print(results)

print()

print("Using Binarizer")
data3 = ([
    [58., 1., 43.],
    [10., 200., 65.],
    [20., 75., 7.]
])
# To binarize a given feature set, we can make use of a threshold. If any value within a given dataset is 
# greater than the threshold, the value is replaced by 1, and if less, it is replaced by 0
results = Binarizer(threshold=50.0).fit(data3).transform(data3)
print(results)