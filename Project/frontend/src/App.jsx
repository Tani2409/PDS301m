import { useState, useEffect } from 'react';
import PriceConverter from './components/PriceConverter';
import SpreadRisk from './components/SpreadRisk';
import ProfitBankCompare from './components/ProfitBankCompare';
import MarketDashboard from './components/MarketDashboard';
import LiveTicker from './components/LiveTicker';
import './index.css';

function App() {
  const [time, setTime] = useState('');
  const [date, setDate] = useState('');
  
  useEffect(() => {
    const tick = () => {
      const now = new Date();
      setTime(now.toLocaleTimeString('vi-VN', { hour12: false }));
      setDate(now.toLocaleDateString('vi-VN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }));
    };
    tick();
    const interval = setInterval(tick, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      <header>
        <div className="logo">
          <div className="logo-icon">
            <svg viewBox="0 0 14 14" fill="none">
              <polygon points="7,1 13,5 13,9 7,13 1,9 1,5" fill="#0D0D0D" stroke="#0D0D0D" strokeWidth="0"/>
              <polygon points="7,1 13,5 13,9 7,13 1,9 1,5" fill="#C9A84C"/>
            </svg>
          </div>
          <span className="logo-text">SILVER<span>TRACK</span></span>
        </div>

        <div className="header-right">
          <span className="last-update">
            <span className="pulse-dot"></span>
            Cập nhật: <span id="update-time">{time}</span>
          </span>
          <button className="btn-refresh" onClick={() => window.location.reload()}>↻ Làm mới</button>
        </div>
      </header>

      <main>
        {/* TOP METRICS (LiveTicker sẽ thế vào đây hoặc phần header) */}
        <LiveTicker />

        {/* MARKET DASHBOARD TABLE */}
        <MarketDashboard />

        {/* BOTTOM GRID FOR FORMS */}
        <div className="bottom-grid">
          <div className="info-panel" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            <PriceConverter />
            <SpreadRisk />
          </div>
          <div className="info-panel">
            <ProfitBankCompare />
          </div>
        </div>
      </main>

      <footer>
        <p>SILVERTRACK — Bảng giá bạc thời gian thực · Dữ liệu mang tính tham khảo</p>
        <p id="footer-date">{date}</p>
      </footer>
    </>
  );
}

export default App;
