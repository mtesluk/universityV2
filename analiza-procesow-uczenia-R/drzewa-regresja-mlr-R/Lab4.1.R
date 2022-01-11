install.packages("C50")
install.packages("MASS")
library (MASS)
library (C50)
data(shuttle)
head(shuttle)

vars <- c("sign", "wind", "magn", "vis", "error", "stability")
v = shuttle[, c(vars, "use")]

set.seed(length(v$sign))
in_train <- sample(1:nrow(v), size = 0.8 * length(v$sign))
train_data <- v[ in_train,]
test_data  <- v[-in_train,]

tree_mod  = C5.0(x = train_data[, vars], y = train_data$use, trials=10)
tree_mod 
summary(tree_mod )
plot(tree_mod )

p = predict(tree_mod , newdata = test_data, type = "prob")
