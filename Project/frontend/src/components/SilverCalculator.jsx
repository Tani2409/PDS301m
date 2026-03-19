import { useState, useEffect } from 'react';

export default function SilverCalculator() {
  const [livePrice, setLivePrice] = useState(120000); // Mặc định 120k/chi nếu chưa fetch xong
  const [totalAmount, setTotalAmount] = useState(1);
  const [unit, setUnit] = useState('chi');
  const [purity, setPurity] = useState(1.0);
  const [resultVND, setResultVND] = useState(0);
  const [resultUSD, setResultUSD] = useState(0);

  // Style cho Option để tránh lỗi tàng hình
  const optionStyle = { backgroundColor: '#1A1A1A', color: '#F2F2F2' };

  // Lấy giá hiện tại từ Backend (CẬP NHẬT LIÊN TỤC 10 GIÂY/LẦN)
  useEffect(() => {
    const fetchLive = () => {
      fetch('http://localhost:5000/api/silver-price')
        .then(res => res.json())
        .then(res => {
          if (res.status === 'success') {
            // Lấy giá 1 chi (999) ước tính tại VN
            setLivePrice(res.live.local_price);
          }
        })
        .catch(err => console.error("Lỗi cập nhật giá live cho máy tính:", err));
    };

    fetchLive();
    const interval = setInterval(fetchLive, 10000); // Cập nhật mỗi 10 giây
    return () => clearInterval(interval);
  }, []);

  // Tính toán kết quả
  useEffect(() => {
    let baseChi = totalAmount;
    if (unit === 'tael') baseChi = totalAmount * 10;
    if (unit === 'oz') baseChi = totalAmount * 0.8294; // 1 oz ~ 0.8294 lượng ~ 8.294 chi

    const finalVND = baseChi * livePrice * purity;
    setResultVND(finalVND);
    setResultUSD(finalVND / 25450); // Ước tính tỷ giá
  }, [totalAmount, unit, purity, livePrice]);

  return (
    <div className="info-panel" style={{ marginTop: '24px', background: 'var(--bg-tertiary)' }}>
      <div className="section-header">
        <span className="section-title">💎 MÁY TÍNH QUY ĐỔI GIÁ TRỊ BẠC</span>
      </div>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '16px' }}>
        <div>
          <label style={{ display: 'block', fontSize: '11px', color: 'var(--muted)', marginBottom: '8px' }}>SỐ LƯỢNG BẠC:</label>
          <div style={{ display: 'flex', gap: '8px' }}>
            <input 
              type="number" 
              value={totalAmount} 
              onChange={(e) => setTotalAmount(parseFloat(e.target.value) || 0)}
              style={{ flex: 1, backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border)', padding: '10px', borderRadius: '8px', color: 'var(--text)' }}
            />
            <select 
              value={unit} 
              onChange={(e) => setUnit(e.target.value)}
              style={{ backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border)', padding: '10px', borderRadius: '8px', color: 'var(--text)' }}
            >
              <option value="chi" style={optionStyle}>Chỉ</option>
              <option value="tael" style={optionStyle}>Lượng (Cây)</option>
              <option value="oz" style={optionStyle}>Ounce (Oz)</option>
            </select>
          </div>
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '11px', color: 'var(--muted)', marginBottom: '8px' }}>LOẠI BẠC (ĐỘ TINH KHIẾT):</label>
          <select 
            value={purity} 
            onChange={(e) => setPurity(parseFloat(e.target.value))}
            style={{ width: '100%', backgroundColor: 'var(--bg-primary)', border: '1px solid var(--border)', padding: '10px', borderRadius: '8px', color: 'var(--text)' }}
          >
            <option value={1.0} style={optionStyle}>Bạc Ta 999 (Nguyên chất)</option>
            <option value={0.925} style={optionStyle}>Bạc 925 (Sterling Silver)</option>
            <option value={0.900} style={optionStyle}>Bạc 900 (Coin Silver)</option>
          </select>
        </div>
      </div>

      <div style={{ marginTop: '30px', padding: '20px', backgroundColor: 'var(--bg-primary)', borderRadius: '12px', textAlign: 'center' }}>
        <p style={{ margin: 0, fontSize: '12px', color: 'var(--muted)' }}>GIÁ TRỊ QUY ĐỔI TƯƠNG ĐƯƠNG:</p>
        <h2 style={{ margin: '8px 0', color: 'var(--accent)', fontSize: '28px' }}>
          {resultVND.toLocaleString('vi-VN')} <span style={{ fontSize: '14px' }}>VNĐ</span>
        </h2>
        <div style={{ padding: '8px 24px', backgroundColor: 'var(--accent-alpha)', display: 'inline-block', borderRadius: '20px', color: 'var(--accent)', fontSize: '13px' }}>
          ≈ {resultUSD.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} USD
        </div>
      </div>
    </div>
  );
}
