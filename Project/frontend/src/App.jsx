import { useState, useEffect } from 'react';
import PriceConverter from './components/Calculators/PriceConverter';
import SpreadRisk from './components/Calculators/SpreadRisk';
import ProfitBankCompare from './components/Calculators/ProfitBankCompare';
import MarketDashboard from './components/Market/MarketDashboard';
import LiveTicker from './components/Market/LiveTicker';
import SilverChart from './components/Analytics/SilverChart';
import SilverHistogram from './components/Analytics/SilverHistogram';
import SilverCalculator from './components/Calculators/SilverCalculator';
import './index.css';

function App() {
  const [activeTab, setActiveTab] = useState('live'); // 'live', 'charts', 'functions'
  const [time, setTime] = useState('');
  
  useEffect(() => {
    const tick = () => {
      setTime(new Date().toLocaleTimeString('vi-VN', { hour12: false }));
    };
    tick();
    const interval = setInterval(tick, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app-container">
      {/* SIDEBAR MENU */}
      <aside className="sidebar">
        <div className="sidebar-logo">
          <div className="logo-icon">
            <svg viewBox="0 0 14 14" fill="none" width="24" height="24">
              <polygon points="7,1 13,5 13,9 7,13 1,9 1,5" fill="#B0C4DE"/>
            </svg>
          </div>
          <span className="logo-text" style={{ fontSize: '18px' }}>SILVER<span>TRACK</span></span>
        </div>

        <nav className="nav-menu">
          <div 
            className={`nav-item ${activeTab === 'live' ? 'active' : ''}`}
            onClick={() => setActiveTab('live')}
          >
            <span>⚡</span> Live Tracking
          </div>
          <div 
            className={`nav-item ${activeTab === 'charts' ? 'active' : ''}`}
            onClick={() => setActiveTab('charts')}
          >
            <span>📈</span> Charts
          </div>
          <div 
            className={`nav-item ${activeTab === 'functions' ? 'active' : ''}`}
            onClick={() => setActiveTab('functions')}
          >
            <span>🛠️</span> Functions
          </div>
        </nav>

        <div style={{ marginTop: 'auto', padding: '24px', fontSize: '12px', color: 'var(--muted)' }}>
          Cập nhật: {time}
        </div>
      </aside>

      {/* MAIN CONTENT AREA */}
      <main className="main-content">
        <LiveTicker />

        {activeTab === 'live' && (
          <div className="fade-in">
            <MarketDashboard />
            <div style={{ marginTop: '24px' }}>
              <PriceConverter />
            </div>
          </div>
        )}

        {activeTab === 'charts' && (
          <div className="fade-in">
            <SilverChart />
            <SilverHistogram />
          </div>
        )}

        {activeTab === 'functions' && (
          <div className="fade-in">
            <SilverCalculator />
            <div className="bottom-grid" style={{ marginTop: '24px' }}>
              <div className="info-panel">
                <SpreadRisk />
              </div>
              <div className="info-panel">
                <ProfitBankCompare />
              </div>
            </div>
          </div>
        )}

        <footer style={{ marginTop: '40px', paddingTop: '20px', borderTop: '1px solid var(--border)' }}>
          <p style={{ color: 'var(--muted)', fontSize: '12px' }}>
            SILVERTRACK — Hệ thống phân tích giá bạc thời gian thực (Modular structure v2.0)
          </p>
        </footer>
      </main>
    </div>
  );
}

export default App;
