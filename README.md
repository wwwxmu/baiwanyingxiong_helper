# 百万英雄答题助手
---
### 功能
为百万英雄、冲顶大会等在线答题平台提供答题“助攻”。利用ocr图片文字识别技术，对手机进行截图，识别题目，自动打开浏览器搜索，简单答案统计等，以期提高答题准确率。
> 注：只提供答案参考，并不能百分百给出准确答案。

### 平台
macOS + iPhone
python 2.7

### 使用说明
类似于之前的微信跳一跳ios自动版，也是需要借助力WDA这个神器。参考：[https://testerhome.com/topics/7220](https://testerhome.com/topics/7220)
1. 克隆 WebDriverAgent 项目 git clone https://github.com/facebook/WebDriverAgent
2. 安装 Carthage brew install carthage
3. 执行 ./Scripts/bootstrap.sh
4. 打开 WebDriverAgent 项目并按照教程修改, 运行 Product -> Test
5. 安装端口转发 brew install libimobiledevice
6. 转发端口 iproxy 8100 8100 , 窗口不要关闭或者终止运行
7. 访问 http://localhost:8100/status 有内容显示

8. 克隆 baiwanyingxiong_helper 项目 git clone https://github.com/wwwxmu/baiwanyingxiong_helper
9. 安装项目依赖
10. 进入baiwanyingxiong_helper目录下，python main.py
11. 题目出现后按“回车”键自动搜索

### 参考
【Skyexu】https://github.com/Skyexu/TopSup

https://www.jianshu.com/p/dc828c4b901d
