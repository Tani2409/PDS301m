import { useState } from 'react';
import { calculateSpread } from '../utils/silverLogic';

export default function SpreadRisk() {
  const [bidPrice, setBidPrice] = useState(1180000); // Giá mua vào
  const [askPrice, setAskPrice] = useState(1220000); // Giá bán ra
  const [result, setResult] = useState(null);

  const handleCalculate = () => {
    const res = calculateSpread(Number(bidPrice), Number(askPrice));
    setResult(res);
  };

  return (
    <div className="glass-card">
      <h2>⚖️ Tính Chênh Lệch Mua Bán</h2>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem', fontSize: '0.9rem' }}>
        Đánh giá mức độ rủi ro dựa trên độ giãn của giá.
      </p>

      <div className="input-group">
        <label>Giá mua vào (VND/chỉ)</label>
        <input 
          type="number" 
          value={bidPrice} 
          onChange={(e) => setBidPrice(e.target.value)} 
        />
      </div>

      <div className="input-group">
        <label>Giá bán ra (VND/chỉ)</label>
        <input 
          type="number" 
          value={askPrice} 
          onChange={(e) => setAskPrice(e.target.value)} 
        />
      </div>

      <button onClick={handleCalculate}>Đánh Giá Rủi Ro</button>

      {result && (
        <div className="result-box">
          {result.error ? (
            <div style={{ color: 'var(--danger-color)' }}>{result.error}</div>
          ) : (
            <>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                <h3>Chênh lệch:</h3>
                <span className={`badge ${result.status === 'an toan' ? 'safe' : 'risk'}`}>
                  {result.status}
                </span>
              </div>
              <div className="value" style={{ fontSize: '1.25rem' }}>
                {result.spreadValue.toLocaleString('vi-VN')} VND
                <span style={{ fontSize: '1rem', color: 'var(--text-secondary)', marginLeft: '0.5rem' }}>
                  ({result.spreadPercent.toFixed(2)}%)
                </span>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}
