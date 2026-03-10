import PriceConverter from './components/PriceConverter';
import SpreadRisk from './components/SpreadRisk';
import ProfitBankCompare from './components/ProfitBankCompare';
import MarketDashboard from './components/MarketDashboard';
import LiveTicker from './components/LiveTicker';
import './index.css';

function App() {
  return (
    <div className="app-container">
      <header>
        <h1>SilverTrade Analytics</h1>
        <p>Hệ thống Phân tích & Quản lý Đầu tư Bạc Chuyên sâu</p>
      </header>

      <main className="grid-layout">
        <LiveTicker />
        <PriceConverter />
        <SpreadRisk />
        <ProfitBankCompare />
        <MarketDashboard />
      </main>

      <footer style={{ textAlign: 'center', marginTop: '2rem', paddingBottom: '2rem', color: 'var(--text-secondary)' }}>
        <p>&copy; 2026 Phase 1+2 Ported. Built with React + Vite + Vanilla CSS.</p>
      </footer>
    </div>
  );
}

export default App;
