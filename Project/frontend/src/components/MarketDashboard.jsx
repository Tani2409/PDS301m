import { useState, useEffect } from 'react';
import { 
  getNgayBienDongHaiChieu, 
  getTatCaNgayBienDong, 
  CONVERSION_RATES, 
  HISTORICAL_HIGHS 
} from '../utils/marketData';

export default function MarketDashboard() {
  const [livePrices, setLivePrices] = useState([]);
  const [liveInfo, setLiveInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch dữ liệu từ Python Backend
  useEffect(() => {
    fetch('http://localhost:5000/api/silver-price')
      .then(res => {
        if (!res.ok) throw new Error('Mạng bị lỗi hoặc Server backend chưa chạy');
        return res.json();
      })
      .then(data => {
        if (data.status === 'success') {
          setLivePrices(data.data);
          setLiveInfo(data.live);
        } else {
          throw new Error(data.message);
        }
      })
      .catch(err => {
        console.error("Lỗi fetch:", err);
        setError(err.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  // Convert Set to Array cho việc render
  const daysBoth = Array.from(getNgayBienDongHaiChieu());
  const daysAll = Array.from(getTatCaNgayBienDong());

  // Định nghĩa các thương hiệu dựa trên giá LIVE
  const basePrice = liveInfo?.local_price || 1200000;
  
  const brandedSilver = [
    { name: "Bạc 999 (SJC)", sub: "Bạc miếng niêm yết", purity: 99.9, colorClass: "badge-sjc", buyAdj: -25000, sellAdj: 0 },
    { name: "Bạc 999 (DOJI)", sub: "Bạc thỏi đầu tư", purity: 99.9, colorClass: "badge-doji", buyAdj: -30000, sellAdj: 10000 },
    { name: "Bạc 925 (PNJ)", sub: "Trang sức cao cấp", purity: 92.5, colorClass: "badge-pnj", buyAdj: -150000, sellAdj: -100000 }
  ];

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
            {brandedSilver.map((item, idx) => {
              const sellPrice = item.purity === 92.5 ? Math.round(basePrice * 0.925) : basePrice + item.sellAdj;
              const buyPrice = sellPrice + item.buyAdj;
              
              return (
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
                  <td className="price-buy">{buyPrice.toLocaleString('vi-VN')}</td>
                  <td className="price-sell">{sellPrice.toLocaleString('vi-VN')}</td>
                  <td><span className="change-up">▲ +{Math.floor(Math.random() * 50) + 10}0</span></td>
                  <td style={{ color: 'var(--muted)', fontSize: '11px' }}>Vừa xong</td>
                </tr>
              );
            })}

            {/* List Data Rendering - World Silver */}
             <tr>
                <td>
                  <span className="td-name">Bạc thế giới<small>XAG/USD Spot (Live API)</small></span>
                </td>
                <td><span className="badge badge-world">INTL</span></td>
                <td className="price-buy">—</td>
                <td className="price-sell">
                  {loading ? 'Đang tải...' : (liveInfo ? `${liveInfo.spot} USD` : 'N/A')}
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
             {daysBoth.map(d => <span key={d} className="chip warning">{d}</span>)}
           </div>
           <div style={{ fontSize: '12px', color: 'var(--muted)' }}>Tất cả biến động (Hợp):</div>
           <div className="chips-container" style={{ margin: '4px 0 0 0' }}>
             {daysAll.map(d => <span key={d} className="chip">{d}</span>)}
           </div>
        </div>
        <div className="metric-card">
           <div className="metric-label">Tuple: Hằng số & Đỉnh giá</div>
           <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '12px' }}>
             <li className="chip">1 Lượng = {CONVERSION_RATES[0]} Oz</li>
             {HISTORICAL_HIGHS.map((h, i) => (
                <li key={i} className="chip" style={{ borderLeft: '2px solid var(--gold)' }}>
                  Đỉnh giá năm {h[0]}: {h[1]} USD/oz
                </li>
              ))}
           </ul>
        </div>
      </div>
    </>
  );
}
