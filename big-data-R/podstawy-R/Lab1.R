
# Cw 1
# R version 3.6.3
install.packages("rattle")
install.packages("https://cran.r-project.org/bin/windows/contrib/3.6/RGtk2_2.20.36.zip", repos=NULL)

library(rattle)
rattle()

# Cw 28.1
v <- sample(1:4, 100, rep=TRUE)
print(v)
f <- factor(v, levels=1:4)
print(f)
levels(f) <- c("czerwony", "zielony", "niebieski", "zolty")
summary(f)

# Cw 28.2
table(cut(iris$Sepal.Length, c(4.3, 5.02, 5.74, 6.46, 7.18, 7.9)))

# Cw 28.3
table(iris$Sepal.Length < 5, factor(iris$Species))

# Cw 28.4
x <- c(1,3,4,7,11,18,29)
x2 <- list("x*2"=(x)*2, "x/2"=(x)/2, "sqrt(x)"=(sqrt(x)))
print(x2)
vec <- unlist(x2)
vec[vec >= 2 & vec <= 3.4]
unique(vec[vec >= 2 & vec <= 3.4])

# Cw 28.5
imiona = c("Kasia", "Ania", "Tomek", "Piotr", "Maria", "Karol", "Sylwia")
lata=c(25,31,23,52,76,49,26)
wysokosci=c(177,163,190,179,163,183,164)
wagi=c(57,69,83,75,70,83,53)
plci=c("K","K","M","M","K","M","K")
d = data.frame("imie"=imiona, "wiek"=lata, "wzrost"=wysokosci, "waga"=wagi, "plec"=as.factor(plci))
d$plec <- as.character(d$plec)
d$plec[d$plec == "K"] <- "MM"
d$plec[d$plec == "M"] <- "K"
d$plec[d$plec == "MM"] <- "M"
d$plec <- as.factor(d$plec)

# Cw 28.6
data.frame(swiss)[c(1,2,3,10,11,12,13),c("Examination", "Education", "Infant.Mortality")]
