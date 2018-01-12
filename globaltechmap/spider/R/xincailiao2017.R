# 处理新材料2017年数据
# 数据导入
xincailiao <- read_delim("News_20180101/xincailiao.csv",  "^", escape_double = FALSE, col_names = FALSE, col_types = cols(X3 = col_skip(), X4 = col_date(format = "%Y-%m-%d"), X8 = col_skip()), trim_ws = TRUE)
# 对列进行命名
colnames(xincailiao) <- c('title','bianhao','date','source','area','content')
# 转化为日期数据
xincailiao$date <- as.Date(xincailiao$date, "%y-%m-%d")
# 提取2017年数据
startdate <- as.Date("2017-01-01")
enddate <- as.Date("2017-12-31")
xincailiao2017 <- filter(xincailiao, date >= startdate & date <= enddate)
