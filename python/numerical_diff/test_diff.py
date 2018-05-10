import numerical_differentiation as nd

p1 = [1.8, 10.889365] 
p2 = [1.9, 12.703199]
p3 = [2.0, 14.778112]
p4 = [2.1, 17.148957]
p5 = [2.2, 19.855030]

print "3-point-start", nd.diff_3points([p1, p2, p3], 'start')
print "5-point-start", nd.diff_5points([p1, p2, p3, p4, p5], 'start')
print
print "3-point-middle", nd.diff_3points([p2, p3, p4], 'middle')
print "5-point-middle", nd.diff_5points([p1, p2, p3, p4, p5], 'middle')
print
print "3-point-end", nd.diff_3points([p3, p4, p5], 'end')
print "5-point-end", nd.diff_5points([p1, p2, p3, p4, p5], 'end')
