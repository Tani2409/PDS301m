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
    <div>
      <div className="section-header" style={{ marginBottom: '16px' }}>
        <span className="section-title">So sánh Đầu Tư Bạc vs Gửi Ngân Hàng</span>
      </div>
      <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '24px', letterSpacing: '0.04em' }}>
        Đánh giá hiệu quả đầu tư so với mức lãi suất tiết kiệm cố định cùng kỳ hạn.
      </p>

      <div style={{ display: 'flex', gap: '16px' }}>
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

      <div style={{ display: 'flex', gap: '16px' }}>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Lãi Ngân hàng (%/năm)</label>
          <input
            type="number"
            value={bankRateAnnual}
            onChange={(e) => setBankRateAnnual(e.target.value)}
            step="0.1"
          />
        </div>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Kỳ hạn (Tháng)</label>
          <input
            type="number"
            value={months}
            onChange={(e) => setMonths(e.target.value)}
          />
        </div>
      </div>

      <button onClick={handleCompare} style={{ marginTop: '16px' }}>Phân Tích So Sánh</button>

      {result && (
        <div className="result-box">
          <h3 style={{ marginBottom: '16px' }}>Kết quả hiển thị ({months} tháng):</h3>

          <div className="info-row" style={{ paddingTop: 0 }}>
            <span className="info-key">Lợi nhuận Bạc</span>
            <span className="info-val" style={{ color: 'var(--gold-light)' }}>
              {result.silverProfit.toLocaleString('vi-VN')}
            </span>
          </div>

          <div className="info-row">
            <span className="info-key">Lãi Ngân Hàng</span>
            <span className="info-val" style={{ color: 'var(--text)' }}>
              {Math.round(result.bankProfit).toLocaleString('vi-VN')}
            </span>
          </div>

          <div className="info-row" style={{
            borderBottom: 'none',
            paddingBottom: 0,
            color: result.silverProfit > result.bankProfit ? 'var(--gold)' : 'var(--text)',
            fontSize: '12px'
          }}>
            <span className="info-key" style={{ color: 'inherit' }}>Kết luận:</span>
            <span style={{ fontWeight: 500 }}>{result.conclusion.replace('KẾT LUẬN: ', '')}</span>
          </div>
        </div>
      )}
    </div>
  );
}
