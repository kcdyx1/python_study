available_toppings = ["蘑菇", "肥肠", "尖椒", "芝士", "炸鸡", "西红柿", "鸡蛋"]
requested_toppings = ["蘑菇", "火腿", "芝士"]
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("已添加" + requested_topping + "。")
	else:
		print("非常抱歉，我们的" + requested_topping + "已售罄！")
print("\n您的披萨已经制作完成，请享用！")
