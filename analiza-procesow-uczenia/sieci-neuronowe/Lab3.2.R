install.packages("neuralnet")
library(neuralnet)

# Z Lab1
#nazwa = c("Xperia 10 III", "Xperia 10 II", "Xperia 1 II", "Xperia 10 Plus", "Xperia 1 III", "Xperia 5 III", "Xperia 5 II", "Xperia 5 IV", "Xperia 5 V", "Xperia 5 VI", "Xperia 5 VII", "Xperia 5 VIII")
#pamiec_RAM = c(6, 4, 8, 4, 12, 8, 8, 6, 12, 8, 8, 6)
#pamiec_wbudowana = c(128, 128, 256, 64, 256, 128, 128, 128, 256, 128, 128, 128)
traininginput = as.data.frame(matrix(c(6, 128, 4, 128, 8, 256, 4, 64, 12, 256, 8, 64, 8, 128), nrow=7, ncol=2))
trainingoutput = c(1849, 999, 2799, 800, 4000, 1849, 2000)

compare.trainingdata = cbind(traininginput, trainingoutput)
maxs = apply(traininginput, 2, max)
mins = apply(traininginput, 2, min)

scaled.traininginput = as.data.frame(scale(traininginput))
trainingdata = cbind(scaled.traininginput, trainingoutput)

colnames(trainingdata) = c("RAM", "HDD", "Price")

net.price <- neuralnet(Price~RAM+HDD,trainingdata, hidden=c(7, 2), threshold=100, lifesign = "full")
plot(net.price)
net.price$result.matrix

RAM_test = c(6, 4)
HDD_test = c(128, 256)
testdata = data.frame(RAM_test, HDD_test)
scaled.testdata = as.data.frame(scale(testdata, center = mins, scale = maxs - mins))

net.results = compute(net.price, scaled.testdata)
cleanoutput <- cbind(testdata, as.data.frame(net.results$net.result))
colnames(cleanoutput) <- c("RAM","HDD","Price")
print(cleanoutput)
