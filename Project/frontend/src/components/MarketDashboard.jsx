import { useState, useEffect } from 'react';
import { 
  silverTypes, 
  getNgayBienDongHaiChieu, 
  getTatCaNgayBienDong, 
  CONVERSION_RATES, 
  HISTORICAL_HIGHS 
} from '../utils/marketData';

export default function MarketDashboard() {
  const [livePrices, setLivePrices] = useState([]);
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

  // Tính toán Max/Min từ mảng livePrices (chỉ trích xuất phần 'price')
  const pricesArray = livePrices.map(item => item.price);
  const maxPrice = pricesArray.length > 0 ? Math.max(...pricesArray) : 0;
  const minPrice = pricesArray.length > 0 ? Math.min(...pricesArray) : 0;

  // Convert Set to Array cho việc render
  const daysBoth = Array.from(getNgayBienDongHaiChieu());
  const daysAll = Array.from(getTatCaNgayBienDong());

  return (
    <>
      <div className="section-header">
        <span className="section-title">Bảng giá theo thương hiệu & Lịch sử</span>
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
            {/* Dictionary Data Rendering */}
            {Object.entries(silverTypes).map(([name, info], idx) => (
              <tr key={name}>
                <td>
                  <span className="td-name">
                    {name.split(' (')[0]}
                    <small>{name.includes('(') ? name.split('(')[1].replace(')', '') : 'Bản tiêu chuẩn'}</small>
                  </span>
                </td>
                <td>
                  <span className={`badge ${idx === 0 ? 'badge-sjc' : idx === 1 ? 'badge-doji' : 'badge-pnj'}`}>
                    {info.do_tinh_khiet}%
                  </span>
                </td>
                <td className="price-buy">{(info.gia_ban_chi - 20000).toLocaleString('vi-VN')}</td>
                <td className="price-sell">{info.gia_ban_chi.toLocaleString('vi-VN')}</td>
                <td><span className="change-up">▲ +{Math.floor(Math.random() * 50) + 10}0</span></td>
                <td style={{ color: 'var(--muted)', fontSize: '11px' }}>10:00</td>
              </tr>
            ))}

            {/* List Data Rendering - Latest price injected as World Silver */}
             <tr>
                <td>
                  <span className="td-name">Bạc thế giới<small>XAG/USD (hiện diện Live API)</small></span>
                </td>
                <td><span className="badge badge-world">INTL</span></td>
                <td className="price-buy">—</td>
                <td className="price-sell">
                  {loading ? 'Đang tải...' : (livePrices.length > 0 ? `${livePrices[livePrices.length - 1].price} USD` : 'N/A')}
                </td>
                <td>
                  {error ? (
                    <span style={{ color: 'var(--down)', fontSize: '11px' }}>Lỗi Backend</span>
                  ) : (
                    <span className="change-down">▼ -0.15</span>
                  )}
                </td>
                <td style={{ color: 'var(--muted)', fontSize: '11px' }}>Live</td>
              </tr>
          </tbody>
        </table>
      </div>

      {/* Thông tin phụ hiển thị bằng layout thẻ chips (Set/Tuple display) */}
      <div className="section-header" style={{ marginTop: '24px' }}>
        <span className="section-title">Phân tích chuyên sâu (Structs Data)</span>
      </div>
      <div className="metrics-bar" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', marginBottom: '48px' }}>
        <div className="metric-card">
           <div className="metric-label">Set: Ngày Biến Động</div>
           <div style={{ marginTop: '8px', fontSize: '12px', color: 'var(--muted)' }}>Biến động 2 chiều:</div>
           <div className="chips-container" style={{ margin: '4px 0 12px 0' }}>
             {daysBoth.map(d => <span key={d} className="chip warning">{d}</span>)}
           </div>
           <div style={{ fontSize: '12px', color: 'var(--muted)' }}>Tất cả biến động:</div>
           <div className="chips-container" style={{ margin: '4px 0 0 0' }}>
             {daysAll.map(d => <span key={d} className="chip">{d}</span>)}
           </div>
        </div>
        <div className="metric-card">
           <div className="metric-label">Tuple: Hằng số & Lịch sử</div>
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
