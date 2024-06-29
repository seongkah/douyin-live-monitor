# 抖音直播监控应用

这是一个使用Flask后端和React前端的Web应用程序,用于监控抖音直播并显示基本统计数据。

## 安装

1. 确保您已安装Python 3.7+和Node.js
2. 克隆此仓库或解压下载的zip文件
3. 在项目根目录中,运行 `pip install -r requirements.txt` 安装Python依赖
4. 进入frontend目录 `cd frontend`
5. 运行 `npm install` 安装React依赖
6. 运行 `npm run build` 构建React应用

## 运行应用

1. 在项目根目录中运行 `python app.py`
2. 在浏览器中访问 `http://localhost:5000`

## 开发模式

如果您想在开发模式下运行前端(实时重新加载更改):

1. 在一个终端中,在项目根目录运行 `python app.py`
2. 在另一个终端中,进入frontend目录并运行 `npm start`
3. 在浏览器中访问 `http://localhost:3000`

## 使用说明

1. 在输入框中输入抖音直播ID
2. 点击"开始监控"按钮开始收集数据
3. 使用"刷新数据"按钮更新显示的统计信息

注意: 这是一个演示应用,不包含实际的抖音API集成。在实际使用中,您需要替换 `fetch_live_data` 函数以使用真实的抖音API。
