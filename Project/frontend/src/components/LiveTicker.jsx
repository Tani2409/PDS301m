import { useState, useEffect } from 'react';

export default function LiveTicker() {
  const [prices, setPrices] = useState({ world: 31.50, local: 1200000 });
  const [prevPrices, setPrevPrices] = useState({ world: 31.50, local: 1200000 });
  const [isFetched, setIsFetched] = useState(false);

  // Lấy giá thực tế từ Backend (Gồm Spot World & Local Estimate)
  useEffect(() => {
    fetch('http://localhost:5000/api/silver-price')
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success' && data.live) {
          const liveWorld = data.live.spot;
          const liveLocal = data.live.local_price;
          setPrices({ world: liveWorld, local: liveLocal });
          setPrevPrices({ world: liveWorld, local: liveLocal });
          setIsFetched(true);
        }
      })
      .catch(console.error);
  }, []);

  // Giả lập giá nhảy liên tục cho cả Thế giới & Việt Nam
  useEffect(() => {
    if (!isFetched) return;

    const simulateTick = () => {
      setPrices(prev => {
        setPrevPrices(prev);
        // Biến động nhẹ cho thế giới (+/- 0.05 USD)
        const worldChange = (Math.random() * 0.1 - 0.05);
        // Biến động nhẹ cho VN (+/- 300 VND)
        const localChange = Math.floor(Math.random() * 600 - 300);
        
        return {
          world: parseFloat((prev.world + worldChange).toFixed(2)),
          local: prev.local + localChange
        };
      });
      
      const nextTick = Math.random() * 1500 + 1000;
      timeOutId = setTimeout(simulateTick, nextTick);
    };

    let timeOutId = setTimeout(simulateTick, 2000);
    return () => clearTimeout(timeOutId);
  }, [isFetched]);

  const worldIsUp = prices.world >= prevPrices.world;
  const worldDiff = (prices.world - prevPrices.world).toFixed(2);
  
  const localIsUp = prices.local >= prevPrices.local;
  const localDiff = prices.local - prevPrices.local;

  return (
    <div className="metrics-bar">
      <div className="metric-card">
        <div className="metric-label">Bạc thế giới (Live Spot)</div>
        <div className="metric-value gold">${prices.world.toFixed(2)}</div>
        <div className={`metric-change ${worldIsUp ? 'up' : 'down'}`}>
          {worldIsUp ? '▲ +' : '▼ '}{worldDiff} (USD/oz)
        </div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Bạc 999 (Live VNĐ)</div>
        <div className="metric-value gold">{prices.local.toLocaleString('vi-VN')}</div>
        <div className={`metric-change ${localIsUp ? 'up' : 'down'}`}>
          {localIsUp ? '▲ +' : '▼ '}{localDiff.toLocaleString('vi-VN')} (đ/chỉ)
        </div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Bạc 925 (Ước tính)</div>
        <div className="metric-value">{(Math.round(prices.local * 0.925)).toLocaleString('vi-VN')}</div>
        <div className="metric-change" style={{ color: 'var(--muted)' }}>Dựa trên giá 999 x 0.925</div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Trạng thái thị trường</div>
        <div className="metric-value" style={{ color: 'var(--up)', fontSize: '18px', marginTop: '4px' }}>Đang Mở Cửa</div>
        <div className={`metric-change ${worldIsUp ? 'up' : 'down'}`}>Biến động theo sàn NY</div>
      </div>
    </div>
  );
}
