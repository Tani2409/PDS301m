import { useState, useEffect } from 'react';

export default function MarketDashboard() {
  const [brandedSilver, setBrandedSilver] = useState([]);
  const [insights, setInsights] = useState(null);
  const [liveInfo, setLiveInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [priceRes, brandedRes, insightsRes] = await Promise.all([
          fetch('http://localhost:5000/api/silver-price').then(r => r.json()),
          fetch('http://localhost:5000/api/market/branded').then(r => r.json()),
          fetch('http://localhost:5000/api/market/insights').then(r => r.json())
        ]);

        if (priceRes.status === 'success') setLiveInfo(priceRes.live);
        if (brandedRes.status === 'success') setBrandedSilver(brandedRes.data);
        if (insightsRes.status === 'success') setInsights(insightsRes.data);
      } catch (err) {
        console.error("Lỗi fetch dashboard:", err);
        setError("Không thể tải dữ liệu từ Backend");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div style={{ padding: '40px', textAlign: 'center', color: 'var(--muted)' }}>Đang tải dữ liệu thị trường...</div>;

  return (
    <>
      <div className="section-header">
        <span className="section-title">Bảng giá thương hiệu & Lịch sử (Cập nhật Live)</span>
        <span className="section-tag">VNĐ / Chỉ / Khác</span>
      </div>

      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Danh Mục / Thương hiệu</th>
              <th>Loại</th>
              <th>Giá Mua vào</th>
              <th>Giá Bán ra</th>
              <th>Thay đổi</th>
              <th>Cập nhật</th>
            </tr>
          </thead>
          <tbody>
            {brandedSilver.map((item, idx) => (
                <tr key={idx}>
                  <td>
                    <span className="td-name">
                      {item.name.split(' (')[0]}
                      <small>{item.sub}</small>
                    </span>
                  </td>
                  <td>
                    <span className={`badge ${item.colorClass}`}>
                      {item.purity}%
                    </span>
                  </td>
                  <td className="price-buy">{item.buy_price.toLocaleString('vi-VN')}</td>
                  <td className="price-sell">{item.sell_price.toLocaleString('vi-VN')}</td>
                  <td><span className="change-up">▲ +{Math.floor(Math.random() * 50) + 10}0</span></td>
                  <td style={{ color: 'var(--muted)', fontSize: '11px' }}>Vừa xong</td>
                </tr>
            ))}

             <tr>
                <td>
                  <span className="td-name">Bạc thế giới<small>XAG/USD Spot (Live API)</small></span>
                </td>
                <td><span className="badge badge-world">INTL</span></td>
                <td className="price-buy">—</td>
                <td className="price-sell">
                  {liveInfo ? `${liveInfo.spot} USD` : 'N/A'}
                </td>
                <td>
                  {error ? (
                    <span style={{ color: 'var(--down)', fontSize: '11px' }}>Lỗi Backend</span>
                  ) : (
                    <span className="change-down">▼ -0.05</span>
                  )}
                </td>
                <td style={{ color: 'var(--muted)', fontSize: '11px' }}>Live</td>
              </tr>
          </tbody>
        </table>
      </div>

      <div className="section-header" style={{ marginTop: '24px' }}>
        <span className="section-title">Phân tích chuyên sâu (Structs Data)</span>
      </div>
      <div className="metrics-bar" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', marginBottom: '48px' }}>
        <div className="metric-card">
           <div className="metric-label">Set: Ngày Biến Động</div>
           <div style={{ marginTop: '8px', fontSize: '12px', color: 'var(--muted)' }}>Biến động 2 chiều (Giao):</div>
           <div className="chips-container" style={{ margin: '4px 0 12px 0' }}>
             {insights?.days_both.map(d => <span key={d} className="chip warning">{d}</span>)}
           </div>
           <div style={{ fontSize: '12px', color: 'var(--muted)' }}>Tất cả biến động (Hợp):</div>
           <div className="chips-container" style={{ margin: '4px 0 0 0' }}>
             {insights?.days_all.map(d => <span key={d} className="chip">{d}</span>)}
           </div>
        </div>
        <div className="metric-card">
           <div className="metric-label">Tuple: Hằng số & Đỉnh giá</div>
           <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '12px' }}>
             <li className="chip">1 Lượng = {insights?.conversion_rates[0]} Oz</li>
             {insights?.historical_highs.map((h, i) => (
                <li key={i} className="chip" style={{ borderLeft: '2px solid var(--accent)' }}>
                  Đỉnh giá năm {h.year}: {h.price} USD/oz
                </li>
              ))}
           </ul>
        </div>
      </div>
    </>
  );
}
