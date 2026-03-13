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
    <div>
      <div className="section-header" style={{ marginBottom: '16px' }}>
        <span className="section-title">Đánh giá Rủi Ro Chênh Lệch</span>
      </div>
      <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '24px', letterSpacing: '0.04em' }}>
        Đánh giá mức độ rủi ro dựa trên độ giãn của giá mua bán.
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
        <div style={{ marginTop: '24px' }}>
          {result.error ? (
            <div style={{ color: 'var(--down)', fontSize: '12px' }}>{result.error}</div>
          ) : (
             <div className="info-row" style={{ borderBottom: 'none', flexDirection: 'column', alignItems: 'flex-start', gap: '8px' }}>
               <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'center' }}>
                 <span className="info-key">Chênh lệch (Spread):</span>
                 <span className={`badge ${result.status === 'an toan' ? 'badge-pnj' : 'badge-doji'}`}>
                    {result.status}
                 </span>
               </div>
               <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'baseline' }}>
                 <span className="info-val" style={{ color: 'var(--gold-light)', fontSize: '18px' }}>
                   {result.spreadValue.toLocaleString('vi-VN')} VND
                 </span>
                 <span style={{ fontSize: '12px', color: 'var(--muted)' }}>
                   ({result.spreadPercent.toFixed(2)}%)
                 </span>
               </div>
             </div>
          )}
        </div>
      )}
    </div>
  );
}
