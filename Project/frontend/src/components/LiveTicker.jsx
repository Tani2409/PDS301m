import { useState, useEffect } from 'react';

export default function LiveTicker() {
  const [currentPrice, setCurrentPrice] = useState(31.50);
  const [prevPrice, setPrevPrice] = useState(31.50);
  const [isFetched, setIsFetched] = useState(false);

  // Lấy giá base lần đầu
  useEffect(() => {
    fetch('http://localhost:5000/api/silver-price')
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success' && data.data.length > 0) {
          const lastPrice = data.data[data.data.length - 1].price;
          setCurrentPrice(lastPrice);
          setPrevPrice(lastPrice);
          setIsFetched(true);
        }
      })
      .catch(console.error);
  }, []);

  // Giả lập giá nhảy liên tục
  useEffect(() => {
    if (!isFetched) return;

    const simulateTick = () => {
      setCurrentPrice(prev => {
        setPrevPrice(prev);
        const change = (Math.random() * 0.1 - 0.05);
        return parseFloat((prev + change).toFixed(2));
      });
      
      const nextTick = Math.random() * 1500 + 1000;
      timeOutId = setTimeout(simulateTick, nextTick);
    };

    let timeOutId = setTimeout(simulateTick, 2000);
    return () => clearTimeout(timeOutId);
  }, [isFetched]);

  const isUp = currentPrice >= prevPrice;
  const changeValue = (currentPrice - prevPrice).toFixed(2);
  const changePercent = ((changeValue / prevPrice) * 100).toFixed(2);

  return (
    <div className="metrics-bar">
      <div className="metric-card">
        <div className="metric-label">Bạc thế giới (Live)</div>
        <div className="metric-value gold">${currentPrice.toFixed(2)}</div>
        <div className={`metric-change ${isUp ? 'up' : 'down'}`}>
          {isUp ? '▲ +' : '▼ '}{changeValue} ({changePercent}%)
        </div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Bạc 999 (Bạc ta)</div>
        <div className="metric-value gold">1.200.000</div>
        <div className="metric-change up">▲ +10.000 (+0.84%)</div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Bạc 925 (Trang sức)</div>
        <div className="metric-value">1.050.000</div>
        <div className="metric-change down">▼ -5.000 (-0.47%)</div>
      </div>
      <div className="metric-card">
        <div className="metric-label">Trạng thái thị trường</div>
        <div className="metric-value" style={{ color: 'var(--up)', fontSize: '18px', marginTop: '4px' }}>Đang Mở Cửa</div>
        <div className="metric-change" style={{ color: 'var(--muted)' }}>Phiên giao dịch New York</div>
      </div>
    </div>
  );
}
