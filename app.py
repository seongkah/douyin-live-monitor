from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import asyncio
import aiohttp
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

# 数据库设置
engine = create_engine('sqlite:///douyin_live_data.db')

# 模拟抖音API
async def fetch_live_data(live_id):
    # 这里应该是实际的API调用
    return {
        'id': live_id,
        'viewer_count': 1000,
        'like_count': 5000,
        'comment_count': 200
    }

@app.route('/api/start_monitor', methods=['POST'])
def start_monitor():
    live_id = request.json['live_id']
    # 这里应该启动一个后台任务来监控直播
    # 为了简单起见，我们只是立即获取一次数据
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    live_data = loop.run_until_complete(fetch_live_data(live_id))
    
    processed_data = {
        'live_id': live_data['id'],
        'viewer_count': live_data['viewer_count'],
        'like_count': live_data['like_count'],
        'comment_count': live_data['comment_count'],
        'timestamp': datetime.now()
    }
    
    df = pd.DataFrame([processed_data])
    df.to_sql('live_stats', engine, if_exists='append', index=False)
    
    return jsonify({"message": "监控已启动", "data": processed_data})

@app.route('/api/get_stats', methods=['GET'])
def get_stats():
    df = pd.read_sql('SELECT * FROM live_stats ORDER BY timestamp DESC LIMIT 10', engine)
    return jsonify(df.to_dict('records'))

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
