var x1, >= 0, <= 20;
var x2 >= 0, <= 20;
var x3 >= 0, <= 20;
var x4 >= 0, <= 20;
var x5 >= 0, <= 20;


s.t. ogr1: 3*x1 + 5*x2 + 2*x3 + 5*x4 + 4*x5 <= 36;
s.t. ogr2: 7*x1 + 12*x2 + 11*x3 + 10*x4 <= 21;
s.t. ogr3: 3*x2*-1 + 12*x3 + 7*x4 + 2*x5 <= 17;

maximize maxz : 141*x1 + 393*x2 + 273*x3 + 804*x4 + 175*x5;

solve;
display maxz, x1, x2, x3, x4, x5;
end;