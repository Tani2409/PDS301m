<<<<<<< Updated upstream:Project/frontend/src/components/SpreadRisk.jsx
import { useState } from 'react';
import { calculateSpread } from '../utils/silverLogic';
=======
import { useState, useEffect } from 'react';
>>>>>>> Stashed changes:Project/frontend/src/components/Calculators/SpreadRisk.jsx

export default function SpreadRisk() {
  const [bidPrice, setBidPrice] = useState(1180000); // Giá mua vào
  const [askPrice, setAskPrice] = useState(1220000); // Giá bán ra
  const [result, setResult] = useState(null);

<<<<<<< Updated upstream:Project/frontend/src/components/SpreadRisk.jsx
  const handleCalculate = () => {
    const res = calculateSpread(Number(bidPrice), Number(askPrice));
    setResult(res);
  };

=======
  // States cho Danh sách Giao dịch (Bài 3)
  const [transactions, setTransactions] = useState([
    { buy_price: 11800000, sell_price: 12200000, quantity: 5 },
    { buy_price: 12500000, sell_price: 12300000, quantity: 2 }
  ]);

  const [computedStats, setComputedStats] = useState({ totalProfit: 0, roiPercent: 0, total_capital: 0 });

  const handleCalculateSpread = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/calculate/risk', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bid: Number(bidPrice), ask: Number(askPrice) })
      });
      const res = await response.json();
      if (res.status === 'success') {
        setResult(res.result);
      }
    } catch (err) {
      console.error("Lỗi tính toán spread từ BE:", err);
    }
  };

  // Tự động tính toán Portfolio khi danh sách giao dịch thay đổi
  useEffect(() => {
    const calculatePortfolio = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/calculate/portfolio', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ transactions })
        });
        const res = await response.json();
        if (res.status === 'success') {
          setComputedStats(res.result);
        }
      } catch (err) {
        console.error("Lỗi tính toán portfolio từ BE:", err);
      }
    };

    calculatePortfolio();
  }, [transactions]);

  // Các hàm xử lý danh sách giao dịch
  const handleAddTransaction = () => {
    setTransactions([...transactions, { buy_price: 0, sell_price: 0, quantity: 1 }]);
  };

  const handleUpdateTransaction = (index, field, value) => {
    const newTransactions = [...transactions];
    newTransactions[index][field] = Number(value);
    setTransactions(newTransactions);
  };

  const handleRemoveTransaction = (index) => {
    setTransactions(transactions.filter((_, i) => i !== index));
  };

>>>>>>> Stashed changes:Project/frontend/src/components/Calculators/SpreadRisk.jsx
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
                 <span className="info-val" style={{ color: 'var(--accent-light)', fontSize: '18px' }}>
                   {result.spreadValue.toLocaleString('vi-VN')} VND
                 </span>
                 <span style={{ fontSize: '12px', color: 'var(--muted)' }}>
                   ({result.spreadPercent.toFixed(2)}%)
                 </span>
               </div>
             </div>
          )}
<<<<<<< Updated upstream:Project/frontend/src/components/SpreadRisk.jsx
        </div>
=======
        </>
      ) : (
        <>
          <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '16px', letterSpacing: '0.04em' }}>
            Tổng hợp lợi nhuận từ các lần mua bán bạc của bạn (Bài toán 3).
          </p>
          <div style={{ backgroundColor: 'var(--bg-secondary)', padding: '16px', borderRadius: '8px', marginBottom: '16px', border: '1px solid var(--border)' }}>
            <h4 style={{ margin: '0 0 12px 0', fontSize: '12px', color: 'var(--accent)' }}>Danh sách Giao dịch Bạc</h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0,1fr) minmax(0,1fr) 60px 30px', gap: '8px', marginBottom: '8px', fontSize: '10px', color: 'var(--muted)' }}>
              <span>Giá Bạn Mua</span>
              <span>Giá Bạn Bán</span>
              <span style={{ textAlign: 'center' }}>SL</span>
              <span></span>
            </div>
            {transactions.map((tx, index) => (
              <div key={index} style={{ display: 'grid', gridTemplateColumns: 'minmax(0,1fr) minmax(0,1fr) 60px 30px', gap: '8px', marginBottom: '8px', alignItems: 'center' }}>
                <input type="number" placeholder="Giá mua..." value={tx.buy_price} onChange={(e) => handleUpdateTransaction(index, 'buy_price', e.target.value)} style={{ padding: '6px' }} />
                <input type="number" placeholder="Giá bán..." value={tx.sell_price} onChange={(e) => handleUpdateTransaction(index, 'sell_price', e.target.value)} style={{ padding: '6px' }} />
                <input type="number" placeholder="SL" value={tx.quantity} onChange={(e) => handleUpdateTransaction(index, 'quantity', e.target.value)} style={{ padding: '6px', textAlign: 'center' }} />
                <button onClick={() => handleRemoveTransaction(index)} className="btn-outline" style={{ padding: '6px', minWidth: 'auto', border: 'none', color: 'var(--down)' }}>✕</button>
              </div>
            ))}
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '12px', alignItems: 'center' }}>
              <button onClick={handleAddTransaction} className="btn-outline" style={{ padding: '4px 12px', fontSize: '11px', minWidth: 'auto' }}>+ Thêm Giao Dịch</button>
              <div style={{ textAlign: 'right', fontSize: '12px' }}>
                <table style={{ borderCollapse: 'collapse', color: 'var(--text)' }}>
                  <tbody>
                    <tr>
                      <td style={{ paddingRight: '12px', color: 'var(--muted)', textAlign: 'right' }}>Tổng Vốn:</td>
                      <td style={{ fontWeight: '500' }}>{computedStats.total_capital.toLocaleString('vi-VN')} VND</td>
                    </tr>
                    <tr>
                      <td style={{ paddingRight: '12px', color: 'var(--muted)', textAlign: 'right' }}>Tổng Lãi/Lỗ:</td>
                      <td style={{ fontWeight: '500', color: computedStats.totalProfit >= 0 ? 'var(--up)' : 'var(--down)' }}>{computedStats.totalProfit.toLocaleString('vi-VN')} VND</td>
                    </tr>
                    <tr>
                      <td style={{ paddingRight: '12px', color: 'var(--muted)', textAlign: 'right' }}>Tỷ suất lợi nhuận (ROI):</td>
                      <td style={{ fontWeight: '500', color: computedStats.roiPercent >= 0 ? 'var(--up)' : 'var(--down)' }}>{computedStats.roiPercent.toFixed(2)}%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </>
>>>>>>> Stashed changes:Project/frontend/src/components/Calculators/SpreadRisk.jsx
      )}
    </div>
  );
}
