项目需求：
	本质是要原材料剩余货量的修改和excel表格的生成

1.项目的需求分析
2.model的设计
	1.原材料的model
		-name
		-材料的数量
		-外键货架
		-外键位置
		-外键原料类别
		-数据修改的时间
		
	2.快速筛选+组合筛选+原材料名字模糊搜索
	
	3.table的设计
		通过ajax异步提交，取到原料类别下对应的原材料，js实现子标签的填写，
		
	4.table2excel插件生成excel表格供打印使用