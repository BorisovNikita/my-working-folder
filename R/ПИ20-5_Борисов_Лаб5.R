generate.supply <- function(n, min, max){
  return(sample(min:max, n, replace = TRUE))
}
#1 написание и вызов функции
res <- generate.supply(15, 2, 10)
# график вариант 1
plot(
  res,
  cex = 2,
  fg = "magenta",
  pch = 21,
  bg = "yellow",
  type = "b",
  lty = 2,
  lwd = 2,
  main = "Поставки товаров 1",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
abline(v = seq(0, 15, 1), col = "blue", lty = 2, lwd=0.5)
abline(h = seq(2, 10, 1), col = "red", lty = 2, lwd=0.5)

# график вариант 2
plot(
  res,
  cex = 5,
  pch = 24,
  bg = "red",
  col.axis = "green",
  type = "b",
  lty = 6,
  lwd = 3,
  main = "Поставки товаров 2",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
abline(v = seq(0, 15, 5), col = "blue", lty = 2, lwd=0.5)
abline(h = seq(2, 10, 5), col = "red", lty = 2, lwd=0.5)

# график вариант 3
plot(
  res,
  cex = 0.5,
  pch = 2,
  bg = "red",
  col.axis = "green",
  type = "b",
  lty = 5,
  lwd = 1.5,
  main = "Поставки товаров 3",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
abline(v = seq(0, 15, 3), lty = 4, lwd=0.5)
abline(h = seq(2, 10, 2), lty = 3, lwd=0.5)

#задание 3
res1 <- generate.supply(10,0,10)
res2 <- generate.supply(10,0,10)
#вариант графиков 1
plot(
  0:10,
  0:10,
  type = "n",
  main = "Поставки товаров 2 в 1",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
lines(
  res1,
  cex = 2,
  pch = 19,
  col = "red",
  col.axis = "blue",
  type = "b",
  lty = 2,
  lwd = 2,

)
lines(
  res2,
  col = "green",
  cex = 2,
  pch = 19,
  type = "b",
  lty = 2,
  lwd = 2,
)
legend(x = "topright",
       legend = c("Поставка 1", "Поставка 2"),
       lty = c(2, 2),
       col = c("red","green"),
       lwd = 2)

#вариант графиков 2
plot(
  0:10,
  0:10,
  type = "n",
  main = "Поставки товаров 2 в 1",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
lines(
  res1,
  cex = 1,
  pch = 3,
  col = "red",
  col.axis = "blue",
  type = "b",
  lty = 6,
  lwd = 1,
  
)
lines(
  res2,
  col = "green",
  cex = 4,
  pch = 12,
  type = "b",
  lty = 4,
  lwd = 0.5,
)
legend(x = "topright",
       legend = c("Поставка 1", "Поставка 2"),
       lty = c(1, 1),
       col = c("red","green"),
       lwd = 4)

#задание 4
rm(ress)
ress <- list(generate.supply(10, 0, 10), generate.supply(10, 0, 10),
             generate.supply(10, 0, 10), generate.supply(10, 0, 10),
             generate.supply(10, 0, 10))
plot(
  0:14,
  0:14,
  type = "n",
  main = "Поставки товаров 5 в 1",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
clrs = c("green", "blue", "yellow", "red", "magenta")
for (i in 1:5){
  lines(
    ress[[i]],
    col = clrs[i],
    cex = i,
    pch = 12+i,
    type = "b",
    lty = 4,
    lwd = 0.5*i,
  )
}
legend(x = "topright",
       legend = c("Поставка 1", "Поставка 2", "Поставка 3", "Поставка 4", "Поставка 5"),
       lty = c(1,2,1,3,4),
       col = clrs,
       lwd = 1)


#задание 5
summ <- c(0,0,0,0,0)
for (i in 1:5)
  summ <- summ + ress[[i]]
plot(
  summ,
  col = "red",
  cex = 5,
  type = "b",
  main = "Поставки товаров в сумме по 5",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)

#задание 6
generate.sale <- function(in_) {
  sale <- c()
  for (i in in_){
    sale <- c(sale, sample(0:i, 1))
  }
  return(sale)
}

#задание 7
supply <- generate.supply(10, 0, 10)
sale <- generate.sale(supply)
plot(
  supply,
  col = "red",
  cex = 2,
  pch = 19,
  type = "b",
  main = "Поставки товаров в сумме по 5",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
lines(
  sale,
  col = "blue",
  cex = 2,
  pch = 19,
  type = "b",
  lty = 4,
  lwd = 1,
)
legend(x = "topright",
       legend = c("Поставка","Продажа"),
       lty = c(1,4),
       col = c("red","blue"),
       lwd = 1)

#задание 8
mag1Supply <- generate.supply(10, 0, 10)
mag1Sale <- generate.sale(mag1Supply)
mag2Supply <- generate.supply(10, 0, 10)
mag2Sale <- generate.sale(mag2Supply)
mag3Supply <- generate.supply(10, 0, 10)
mag3Sale <- generate.sale(mag3Supply)
lst <- list(mag1Supply,mag1Sale, mag2Supply, mag2Sale, mag3Supply, mag3Sale)
plot(
  0:14,
  0:14,
  type = "n",
  main = "Поставки и продажи товаров по 3м магазинам",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
clrs = c("green", "blue", "yellowgreen", "red", "magenta", "orange")
for (i in 1:5){
  lines(
    ress[[i]],
    col = clrs[i],
    cex = 1,
    pch = 19,
    type = "b",
    lty = i,
    lwd = 1,
  )
}
legend(x = "topright",
       legend = c("Поставка 1", "Продажа 1", "Поставка 2", "Продажа 2", "Поставка 3", "Продажа 3"),
       lty = c(1:6),
       col = clrs,
       lwd = 1)

#задание 9
ost <- list(lst[[1]]-lst[[2]], lst[[3]]-lst[[4]], lst[[5]]-lst[[6]])
plot(
  0:14,
  0:14,
  type = "n",
  main = "остатки товаров по 3м магазинам",
  xlab = "день",
  ylab = "количество товара",
  sub = "несколько дней месяца на графике"
)
clrs = c("green", "blue", "red")
for (i in 1:5){
  lines(
    ress[[i]],
    col = clrs[i],
    cex = 1,
    pch = 19,
    type = "b",
    lty = i,
    lwd = 1,
  )
}
legend(x = "topright",
       legend = c("Остатки 1", "Остатки 2", "Остатки 3"),
       lty = c(1:3),
       col = clrs,
       lwd = 1)