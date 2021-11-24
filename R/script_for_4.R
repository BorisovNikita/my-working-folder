func1 <- function(x, y, z) {
  if (z == 0) {
    print("Деление на 0!")
  } else if (is.integer(c(x,y,z)) | (is.double(c(x,y,z)))) {
    print(x^y/z)
  } else {
    print("Ошибка в типе данных")
  }
}

func2 <- function(N, isDebug = FALSE, lang = "RU", short = FALSE) {
  if (is.element(lang, c("Eng","eng","English","english","Англ","англ", "анг"))) {
    if (short) {
      week = c("Mo","Tu","We","Th","Fr","Sa","Su")
    } else {
      week = c("Monday", "Tuesday", "Wednesday",
               "Thursday","Friday",
               "Saturday","Sunday")
    }
  } else {
    if (short) {
      week = c("Пн","Вт","Ср","Чт","Пт","Сб","Вс")
    } else {
      week = c("Понедельник", "Вторник", "Среда",
               "Четверг","Пятница",
               "Суббота","Воскресенье")
    }
  }
  temp <- function(x) {
    if (x<1){
      returned <- ' '
    } else if (x>7) {
      returned <- NaN
    } else {
      returned <- week[x]
    }
    return(returned)
  }
  
  if (is.double(N) | is.integer(N)) {
    N <- as.integer(N)
    returned <- sapply(N,FUN = temp)
  } else {
    print("Ошибка передаваемого аргумента")
    returned <- NaN
  }

  
  if (isDebug) {
    return(print(paste0("Введено: ", N,", Возвращено: ", returned)))
  } else {
    return(returned)
  }
}




func1(2,3,4)
func1(2,3,0)
func1(2,"fd",4)
func1(2,c(3,4,5),4)

func2(c(3,4,5,6))
func2(2, isDebug = TRUE)
func2(2, isDebug = TRUE, lang = "Eng", short = TRUE)
func2(c(-1,2,10,11), isDebug = TRUE, lang = "RU", short = FALSE)
func2(c(-1,2,10,11,"fasd"))

