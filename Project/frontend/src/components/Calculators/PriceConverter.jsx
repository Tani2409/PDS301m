import { useState } from 'react';

export default function PriceConverter() {
  const [usdOz, setUsdOz] = useState(30.5);
  const [exchangeRate, setExchangeRate] = useState(25400);
  const [result, setResult] = useState(null);

  const handleConvert = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/calculate/conversion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          amount: 1, // 1 lượng
          unit: 'tael',
          purity: 1.0,
          live_price: Number(usdOz),
          usd_vnd: Number(exchangeRate)
        })
      });
      const res = await response.json();
      if (res.status === 'success') {
        setResult(res.result.vnd);
      }
    } catch (err) {
      console.error("Lỗi quy đổi giá từ BE:", err);
    }
  };

  return (
    <div>
      <div className="section-header" style={{ marginBottom: '16px' }}>
        <span className="section-title">Chuyển đổi USD/oz sang VND/lượng</span>
      </div>
      <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '24px', letterSpacing: '0.04em' }}>
        Công cụ quy đổi giá bạc thế giới sang giá nội địa theo tỷ giá tuỳ chỉnh.
      </p>
      
      <div className="input-group">
        <label>Giá Bạc TG (USD/oz)</label>
        <input 
          type="number" 
          value={usdOz} 
          onChange={(e) => setUsdOz(e.target.value)} 
          step="0.1"
        />
      </div>

      <div className="input-group">
        <label>Tỷ giá USD/VND</label>
        <input 
          type="number" 
          value={exchangeRate} 
          onChange={(e) => setExchangeRate(e.target.value)} 
        />
      </div>

      <button onClick={handleConvert}>Quy đổi giá</button>

      {result !== null && (
        <div className="info-row" style={{ marginTop: '24px', borderBottom: 'none' }}>
          <span className="info-key">Giá Bạc Quy Đổi</span>
          <span className="info-val" style={{ color: 'var(--accent-light)', fontSize: '16px' }}>
            {Math.round(result).toLocaleString('vi-VN')} VND/lượng
          </span>
        </div>
      )}
    </div>
  );
}
