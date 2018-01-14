# 处理新材料2017年数据
# 数据导入
xincailiao2017 <- read_csv("Results/xincailiao2017.csv", col_names = c("words", "num"), col_types = cols(words = col_character(), num = col_integer()))
xincailiao2016 <- read_csv("Results/xincailiao2016.csv", col_names = c("words", "num"), col_types = cols(words = col_character(), num = col_integer()))
xincailiao2015 <- read_csv("Results/xincailiao2015.csv", col_names = c("words", "num"), col_types = cols(words = col_character(), num = col_integer()))

# 对列进行命名
colnames(xincailiao) <- c('title','bianhao','date','source','area','content')
# 转化为日期数据
xincailiao$date <- as.Date(xincailiao$date, "%y-%m-%d")
# 提取2017年数据
startdate <- as.Date("2017-01-01")
enddate <- as.Date("2017-12-31")
xincailiao2017 <- filter(xincailiao, date >= startdate & date <= enddate)

library("tidyverse")
xincailiao2017g <- ggplot(xincailiao2017[2:10,], aes(x = words, y = num, fill = words))+geom_bar(stat = "identity") + theme(text = element_text(family = 'SimSun'))
xincailiao2017g
