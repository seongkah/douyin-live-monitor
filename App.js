// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [liveId, setLiveId] = useState('');
  const [stats, setStats] = useState([]);

  const startMonitor = async () => {
    try {
      const response = await axios.post('/api/start_monitor', { live_id: liveId });
      alert(response.data.message);
      getStats();
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const getStats = async () => {
    try {
      const response = await axios.get('/api/get_stats');
      setStats(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {
    getStats();
  }, []);

  return (
    <div className="container">
      <h1>抖音直播监控</h1>
      <input 
        value={liveId} 
        onChange={(e) => setLiveId(e.target.value)} 
        placeholder="输入直播ID"
      />
      <button onClick={startMonitor}>开始监控</button>
      <button onClick={getStats}>刷新数据</button>
      <h2>最新统计数据</h2>
      <table>
        <thead>
          <tr>
            <th>直播ID</th>
            <th>观看人数</th>
            <th>点赞数</th>
            <th>评论数</th>
            <th>时间戳</th>
          </tr>
        </thead>
        <tbody>
          {stats.map((stat) => (
            <tr key={stat.timestamp}>
              <td>{stat.live_id}</td>
              <td>{stat.viewer_count}</td>
              <td>{stat.like_count}</td>
              <td>{stat.comment_count}</td>
              <td>{stat.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;