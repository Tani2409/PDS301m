import { useState } from 'react';
import { compareInvestmentVsBank, calculateTotalProfit } from '../utils/silverLogic';

export default function ProfitBankCompare() {
  const [capital, setCapital] = useState(11800000 * 5 + 12500000 * 2); // Vốn mặc định từ Test 4
  const [silverProfit, setSilverProfit] = useState(1600000); // Lời mặc định từ Test 3
  const [bankRateAnnual, setBankRateAnnual] = useState(5.0);
  const [months, setMonths] = useState(3);
  const [result, setResult] = useState(null);

  const handleCompare = () => {
    const res = compareInvestmentVsBank(
      Number(capital),
      Number(silverProfit),
      Number(bankRateAnnual),
      Number(months)
    );
    setResult(res);
  };

  return (
    <div className="glass-card">
      <h2>🏦 Bạc vs Ngân Hàng</h2>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem', fontSize: '0.9rem' }}>
        So sánh lợi nhuận giữa đầu tư bạc và gửi tiết kiệm cùng kỳ hạn.
      </p>

      <div style={{ display: 'flex', gap: '1rem' }}>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Vốn đầu tư (VND)</label>
          <input 
            type="number" 
            value={capital} 
            onChange={(e) => setCapital(e.target.value)} 
          />
        </div>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Lợi nhuận Bạc (VND)</label>
          <input 
            type="number" 
            value={silverProfit} 
            onChange={(e) => setSilverProfit(e.target.value)} 
          />
        </div>
      </div>

      <div style={{ display: 'flex', gap: '1rem' }}>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Lãi suất Ngân hàng (%/năm)</label>
          <input 
            type="number" 
            value={bankRateAnnual} 
            onChange={(e) => setBankRateAnnual(e.target.value)} 
            step="0.1"
          />
        </div>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Số tháng gửi</label>
          <input 
            type="number" 
            value={months} 
            onChange={(e) => setMonths(e.target.value)} 
          />
        </div>
      </div>

      <button onClick={handleCompare}>So Sánh</button>

      {result && (
        <div className="result-box">
          <h3 style={{ marginBottom: '1rem' }}>{`Sau ${months} tháng:`}</h3>
          
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', flexWrap: 'wrap', gap: '0.5rem' }}>
            <span style={{ minWidth: '120px' }}>Lợi nhuận Bạc:</span>
            <strong style={{ color: 'var(--success-color)', wordBreak: 'break-word', textAlign: 'right', flex: 1 }}>{result.silverProfit.toLocaleString('vi-VN')} VND</strong>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', flexWrap: 'wrap', gap: '0.5rem' }}>
            <span style={{ minWidth: '120px' }}>Lãi Ngân Hàng:</span>
            <strong style={{ color: '#60a5fa', wordBreak: 'break-word', textAlign: 'right', flex: 1 }}>{Math.round(result.bankProfit).toLocaleString('vi-VN')} VND</strong>
          </div>
          
          <div style={{ 
            paddingTop: '1rem', 
            borderTop: '1px solid var(--glass-border)',
            color: result.silverProfit > result.bankProfit ? 'var(--success-color)' : '#60a5fa',
            fontWeight: 600
          }}>
            {'=> '} {result.conclusion}
          </div>
        </div>
      )}
    </div>
  );
}
