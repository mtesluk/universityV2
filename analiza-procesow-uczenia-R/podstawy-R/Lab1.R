# a
a <-  5 / exp(10)
b <- 2 * a
max(a, b)

# b
help(cos)

# c
a <- seq(70, 135)
mean(a)

# d
??round

# e
setwd("C:/Users/mtesluk/Desktop/studia/Apu/Lab1")
a <- "smartfon Sony"
getwd()
ls()
save(a, file = "workspace.RData")
remove(a)
ls()
load("workspace.RData")
ls()

# f
install.packages("gridExtra")
library(gridExtra)
help(package="gridExtra")
setwd("C:/Users/mtesluk/Desktop/studia/Apu/Lab1")
a = read.csv("test.csv", na.strings = "")
b = a[seq(1, 10),]
grid.table(b)

# g
a = seq(200, 40, -8)

# h
a = seq(50, 30)
b = seq(20, 50)
d = c(a, b);

# i j k l m n o
nazwa = c("Xperia 10", "Xperia 1", "Xperia 5", "Xperia L4", "Xperia 10 Plus", "Xperia 1 Plus", "Xperia 5 Plus", "Xperia L4 beta", "Xperia L4 Plus", "Xperia L4 Minus")
wyswietlacz = c("6''", "6''", "6''", "6''", "6,2''", "6''", "6''", "6''", "6''", "6''")
pamiec_RAM = c("6 GB", "6 GB", "6 GB", "6 GB", "6,5 GB", "6 GB", "6 GB", "6 GB", "6 GB", "6 GB")
pamiec_wbudowana = c("128 GB", "128 GB", "128 GB", "128 GB", "160 GB", "128 GB", "128 GB", "128 GB", "128 GB", "128 GB")
aparat_foto = c("12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix", "12 Mpix")
cena = c(1880, 1480, 1280, 1180, 1999, 2000, 2100, 1700, 1600, 1500)
liczba_opinii = c("45", "66", "120", "13", "107", "66", "99", "33", "12", "67")
ramka = data.frame(nazwa, wyswietlacz, pamiec_RAM, pamiec_wbudowana, aparat_foto, cena, liczba_opinii)
m = mean(ramka[, "cena"])

nowy_smarfon = data.frame(nazwa="Xperia Small", wyswietlacz="5''", pamiec_RAM="3 GB", pamiec_wbudowana="64 GB",aparat_foto="12 Mpix",cena=1000,liczba_opinii="22")
ramka = rbind(ramka, nowy_smarfon)
m2 = mean(ramka[, "cena"])

ocena = c("4", "4.5", "4.5", "4", "4", "3.5", "3", "4.5", "5", "5", "4.5")
ramka = cbind(ramka, ocena)
ocena_5 = mean(ramka[ramka$ocena == "5", "cena"])
ocena_4_5 = mean(ramka[ramka$ocena == "4.5", "cena"])
ocena_4 = mean(ramka[ramka$ocena == "4", "cena"])
ocena_3 = mean(ramka[ramka$ocena == "3", "cena"])
ocena_3_5 = mean(ramka[ramka$ocena == "3.5", "cena"])

nowy_smarfon2 = data.frame(nazwa="Xperia Big", wyswietlacz="5''", pamiec_RAM="6 GB", pamiec_wbudowana="64 GB",aparat_foto="12 Mpix",cena=200,liczba_opinii="22", ocena="5")
nowy_smarfon3 = data.frame(nazwa="Xperia You", wyswietlacz="6''", pamiec_RAM="4 GB", pamiec_wbudowana="128 GB",aparat_foto="12 Mpix",cena=1200,liczba_opinii="45", ocena="4.5")
nowy_smarfon4 = data.frame(nazwa="Xperia X5S", wyswietlacz="5''", pamiec_RAM="3 GB", pamiec_wbudowana="64 GB",aparat_foto="12 Mpix",cena=1400,liczba_opinii="77", ocena="4")
nowy_smarfon5 = data.frame(nazwa="Xperia EN", wyswietlacz="4''", pamiec_RAM="5 GB", pamiec_wbudowana="64 GB",aparat_foto="12 Mpix",cena=1600,liczba_opinii="0", ocena="4")
ramka = rbind(ramka, nowy_smarfon2)
ramka = rbind(ramka, nowy_smarfon3)
ramka = rbind(ramka, nowy_smarfon4)
ramka = rbind(ramka, nowy_smarfon5)
install.packages("plotrix")
library(plotrix)
count <- table(ramka$ocena)
barplot(count, main = "Liczebność", ylim = c(0, 10), xlab = "Ocena", ylab = "Ilość")

percentages <- table(ramka$ocena) / length(ramka$ocena)
pie(percentages)

status_opini = c("mniej niż 50 opinii", "50-100 opinii", "więcej niż 100 opinii", "mniej niż 50 opinii", "więcej niż 100 opinii", "50-100 opinii", "50-100 opinii", "mniej niż 50 opinii", "50-100 opinii", "50-100 opinii", "50-100 opinii", "więcej niż 100 opinii", "50-100 opinii", "mniej niż 50 opinii", "nie ma")
ramka = cbind(ramka, status_opini)
percentages <- table(ramka$status_opini) / length(ramka$status_opini)
pie(percentages)

write.csv(ramka,'ramka.csv')
ramka1 = read.csv("ramka.csv")