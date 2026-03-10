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

    // Cập nhật ngẫu nhiên mỗi 1.5 đến 3 giây để giống dữ liệu live thị trường
    const simulateTick = () => {
      setCurrentPrice(prev => {
        setPrevPrice(prev);
        // Biến động random rất nhỏ (-0.05 đến +0.05)
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

  return (
    <div className="glass-card" style={{ textAlign: 'center', gridColumn: '1 / -1', padding: '2rem' }}>
      <h2 style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem', borderBottom: 'none' }}>
        <span className="live-indicator"></span> 
        Live Thị Trường Vi Mô (Mô phỏng XAG/USD)
      </h2>
      
      <div 
        style={{ 
          fontSize: '4rem', 
          fontWeight: 700, 
          color: isUp ? 'var(--success-color)' : 'var(--danger-color)',
          textShadow: `0 0 30px ${isUp ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`,
          transition: 'color 0.3s ease',
          fontFamily: 'monospace',
          marginBottom: '0.5rem'
        }}
      >
        ${currentPrice.toFixed(2)}
        <span style={{ fontSize: '2rem', marginLeft: '1rem', opacity: 0.8 }}>
          {isUp ? '▲' : '▼'}
        </span>
      </div>
      
      <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
        Tick-by-tick trading data (Lấy giá gốc từ Backend & tạo biến động vi mô)
      </p>
    </div>
  );
}
