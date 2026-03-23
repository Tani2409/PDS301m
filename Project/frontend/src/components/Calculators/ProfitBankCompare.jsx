import { useState } from 'react';

export default function ProfitBankCompare() {
  const [activeTab, setActiveTab] = useState('compare'); // 'compare' hoặc 'breakeven'
  
  // States cho So sánh trực tiếp
  const [capital, setCapital] = useState(11800000 * 5 + 12500000 * 2);
  const [silverProfit, setSilverProfit] = useState(1600000);
  
  // States cho Điểm hòa vốn
  const [purchasePrice, setPurchasePrice] = useState(1200000); // Giá mua/chi
  
  // Common states
  const [bankRateAnnual, setBankRateAnnual] = useState(5.0);
  const [months, setMonths] = useState(3);
  
  const [result, setResult] = useState(null);
  const [beResult, setBeResult] = useState(null);

  const handleCompare = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/calculate/investment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          capital: Number(capital),
          rate_annual: Number(bankRateAnnual),
          months: Number(months),
          silver_profit: Number(silverProfit)
        })
      });
      const res = await response.json();
      if (res.status === 'success') {
        setResult(res.result);
      }
    } catch (err) {
      console.error("Lỗi so sánh đầu tư từ BE:", err);
    }
  };

  const handleCalculateBE = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/calculate/breakeven', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          purchase_price: Number(purchasePrice),
          bank_rate: Number(bankRateAnnual),
          months: Number(months)
        })
      });
      const res = await response.json();
      if (res.status === 'success') {
        setBeResult(res.result);
      }
    } catch (err) {
      console.error("Lỗi tính điểm hòa vốn từ BE:", err);
    }
  };

  return (
    <div>
      <div className="section-header" style={{ marginBottom: '16px' }}>
        <span className="section-title">Phân tích Đầu tư vs Tiết kiệm</span>
      </div>

      {/* Tabs giả lập để chọn chế độ */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '20px' }}>
        <button 
          onClick={() => setActiveTab('compare')}
          className={activeTab === 'compare' ? '' : 'btn-outline'}
          style={{ padding: '6px 16px', fontSize: '11px', minWidth: 'auto' }}
        >
          So sánh Lợi nhuận
        </button>
        <button 
          onClick={() => setActiveTab('breakeven')}
          className={activeTab === 'breakeven' ? '' : 'btn-outline'}
          style={{ padding: '6px 16px', fontSize: '11px', minWidth: 'auto' }}
        >
          Điểm hòa vốn (Break-even)
        </button>
      </div>

      {activeTab === 'compare' ? (
        <>
          <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '16px' }}>
            Đánh giá hiệu quả dựa trên lợi nhuận bạn đã thu được.
          </p>
          <div style={{ display: 'flex', gap: '16px' }}>
            <div className="input-group" style={{ flex: 1 }}>
              <label>Vốn đầu tư (VND)</label>
              <input type="number" value={capital} onChange={(e) => setCapital(e.target.value)} />
            </div>
            <div className="input-group" style={{ flex: 1 }}>
              <label>Lợi nhuận Bạc (VND)</label>
              <input type="number" value={silverProfit} onChange={(e) => setSilverProfit(e.target.value)} />
            </div>
          </div>
        </>
      ) : (
        <>
          <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '16px' }}>
            Tính toán xem bạn cần bán giá bao nhiêu để lời hơn gửi ngân hàng.
          </p>
          <div className="input-group">
            <label>Giá lúc bạn mua (VND/chỉ)</label>
            <input 
              type="number" 
              value={purchasePrice} 
              onChange={(e) => setPurchasePrice(e.target.value)} 
              placeholder="Ví dụ: 1.200.000"
            />
          </div>
        </>
      )}

      <div style={{ display: 'flex', gap: '16px' }}>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Lãi Ngân hàng (%/năm)</label>
          <input type="number" value={bankRateAnnual} onChange={(e) => setBankRateAnnual(e.target.value)} step="0.1" />
        </div>
        <div className="input-group" style={{ flex: 1 }}>
          <label>Kỳ hạn dự kiến (Tháng)</label>
          <input type="number" value={months} onChange={(e) => setMonths(e.target.value)} />
        </div>
      </div>

      <button 
        onClick={activeTab === 'compare' ? handleCompare : handleCalculateBE} 
        style={{ marginTop: '16px' }}
      >
        {activeTab === 'compare' ? 'Phân Tích So Sánh' : 'Tính Giá Hòa Vốn'}
      </button>

      {/* Render kết quả So sánh */}
      {activeTab === 'compare' && result && (
        <div className="result-box">
          <h3 style={{ marginBottom: '16px' }}>Kết quả ({months} tháng):</h3>
          <div className="info-row" style={{ paddingTop: 0 }}>
            <span className="info-key">Lợi nhuận Bạc</span>
            <span className="info-val" style={{ color: 'var(--accent-light)' }}>{result.silverProfit.toLocaleString('vi-VN')} VND</span>
          </div>
          <div className="info-row">
            <span className="info-key">Lãi Ngân Hàng</span>
            <span className="info-val">{Math.round(result.bankProfit).toLocaleString('vi-VN')} VND</span>
          </div>
          <div className="info-row" style={{ borderBottom: 'none', color: result.silverProfit > result.bankProfit ? 'var(--accent)' : 'var(--text)' }}>
            <span className="info-key" style={{ color: 'inherit' }}>Kết luận:</span>
            <span style={{ fontWeight: 500 }}>{result.conclusion}</span>
          </div>
        </div>
      )}

      {/* Render kết quả Hòa vốn */}
      {activeTab === 'breakeven' && beResult && (
        <div className="result-box">
          <h3 style={{ marginBottom: '16px' }}>Mục tiêu giá bán ({months} tháng):</h3>
          <div className="info-row" style={{ paddingTop: 0 }}>
            <span className="info-key">Lãi suất Bank tương ứng</span>
            <span className="info-val" style={{ color: 'var(--up)' }}>+{beResult.targetReturnPercent}%</span>
          </div>
          <div className="info-row">
            <span className="info-key">Giá bán tối thiểu cần đạt</span>
            <span className="info-val" style={{ color: 'var(--accent-light)', fontSize: '18px' }}>
              {beResult.breakEvenPrice.toLocaleString('vi-VN')} đ/chỉ
            </span>
          </div>
          <p style={{ marginTop: '12px', fontSize: '11px', color: 'var(--muted)', fontStyle: 'italic' }}>
            *Để lời hơn gửi tiết kiệm, bạn cần bán được giá cao hơn mức này (đã tính bù đắp lãi suất ngân hàng).
          </p>
        </div>
      )}
    </div>
  );
}
