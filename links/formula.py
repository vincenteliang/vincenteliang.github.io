if(empty(prop("任务类型")), "❓任务类型", 
if(empty(prop("周计划量")), "❓周计划量", 
if(prop("周完成量") / prop("周计划量") <= 0, 
if(prop("Status") == "Miss", "🤣 0%", "⏳ 快开始啊"), 
if(prop("周完成量") / prop("周计划量") > 1, 
"■■■■■■■■■■" + " " + format(round(prop("周完成量") / prop("周计划量") * 100)) + "%", 
slice("■■■■■■■■■■", 10 - round(prop("周完成量") / prop("周计划量") * 10)) + " " + format(round(prop("周完成量") / prop("周计划量") * 100)) + "%"))))
