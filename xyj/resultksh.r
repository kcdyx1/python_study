library(tidyverse)
library(readr)
library(ggthemes)

xyj_result <- read_csv("python_study/xyj/result.csv")
View(xyj_result)

Top10 <- xyj_result[1:10,]
p = ggplot(Top10, aes(x = Word, y = Number, fill = Word))+geom_bar(stat = "identity") + theme(text = element_text(family = 'SimSun'))
p