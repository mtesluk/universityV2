install.packages("neuralnet")
library(neuralnet)

traininginput <-  as.data.frame(runif(500, min=1, max=3))
trainingoutput <- sin(traininginput^2)

trainingdata <- cbind(traininginput,trainingoutput)
colnames(trainingdata) <- c("Input","Output")

net.sqrt <- neuralnet(Output~Input,trainingdata, hidden=7, threshold=0.01, stepmax=1e7)

print(net.sqrt)
plot(net.sqrt, rep = "best")

testdata <- as.data.frame(runif(100, min=1, max=3))
net.results <- compute(net.sqrt, testdata)
print(net.results$net.result)

cleanoutput <- cbind(testdata,sin(testdata^2),
                     as.data.frame(net.results$net.result))
colnames(cleanoutput) <- c("Input","Expected Output","Neural Net Output")
print(cleanoutput)
