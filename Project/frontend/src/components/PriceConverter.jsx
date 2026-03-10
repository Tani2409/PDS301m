import { useState } from 'react';
import { convertSilverPrice } from '../utils/silverLogic';

export default function PriceConverter() {
  const [usdOz, setUsdOz] = useState(30.5);
  const [exchangeRate, setExchangeRate] = useState(25400);
  const [result, setResult] = useState(null);

  const handleConvert = () => {
    const res = convertSilverPrice(Number(usdOz), Number(exchangeRate));
    setResult(res);
  };

  return (
    <div className="glass-card">
      <h2>💱 Chuyển đổi Giá Bạc</h2>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem', fontSize: '0.9rem' }}>
        Tính giá VND/lượng từ giá thế giới (USD/oz).
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

      <button onClick={handleConvert}>Tính Toán</button>

      {result !== null && (
        <div className="result-box">
          <h3>Giá Quy Đổi:</h3>
          <div className="value">{Math.round(result).toLocaleString('vi-VN')} VND/lượng</div>
        </div>
      )}
    </div>
  );
}
