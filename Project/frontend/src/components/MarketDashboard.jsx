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
    <div className="glass-card" style={{ gridColumn: '1 / -1' }}>
      <h2>📈 Bảng Theo Dõi Thị Trường Cấu Trúc Dữ Liệu (Live Data)</h2>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginTop: '1.5rem' }}>
        
        {/* Lịch sử Giá (List) - Thay thế bằng Live API */}
        <div>
          <h3 style={{ color: 'var(--text-secondary)', fontSize: '1rem', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            List: Lịch sử giá thế giới (USD/oz)
            {loading && <span style={{ fontSize: '0.8rem', color: 'var(--accent-color)' }}>(Đang tải live...)</span>}
          </h3>
          
          {error ? (
            <div style={{ color: 'var(--danger-color)', fontSize: '0.9rem', marginBottom: '1rem', padding: '0.5rem', background: 'rgba(239, 68, 68, 0.1)', borderRadius: '4px' }}>
              ⚠️ Lỗi: {error}. Vui lòng chạy `python backend/api.py`.
            </div>
          ) : (
            <>
              <div className="chips-container" style={{ marginBottom: '1rem', maxHeight: '120px', overflowY: 'auto' }}>
                {livePrices.map((p, i) => (
                  <span key={i} className="chip">
                    <span style={{color: 'var(--text-secondary)', marginRight: '4px'}}>{p.date}:</span>
                    {p.price}
                  </span>
                ))}
              </div>
              <div style={{ display: 'flex', gap: '1rem' }}>
                <div>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Cao nhất</span>
                  <div style={{ color: 'var(--success-color)', fontWeight: 600 }}>{maxPrice > 0 ? maxPrice : '--'} USD</div>
                </div>
                <div>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Thấp nhất</span>
                  <div style={{ color: 'var(--danger-color)', fontWeight: 600 }}>{minPrice > 0 ? minPrice : '--'} USD</div>
                </div>
              </div>
            </>
          )}
        </div>

        {/* Cột mốc (Tuple) */}
        <div>
          <h3 style={{ color: 'var(--text-secondary)', fontSize: '1rem', marginBottom: '0.5rem' }}>
            Tuple: Hằng số & Đỉnh lịch sử
          </h3>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            <li className="chip">Quy đổi chuẩn: 1 Lượng = {CONVERSION_RATES[0]} Oz</li>
            {HISTORICAL_HIGHS.map((h, i) => (
              <li key={i} className="chip" style={{ borderLeft: '4px solid var(--warning-color)' }}>
                Đỉnh năm {h[0]}: {h[1]} USD/oz
              </li>
            ))}
          </ul>
        </div>

        {/* Biến động (Set) */}
        <div>
          <h3 style={{ color: 'var(--text-secondary)', fontSize: '1rem', marginBottom: '0.5rem' }}>
            Set: Phân tích các ngày biến động
          </h3>
          
          <div style={{ marginBottom: '0.5rem' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Ngày giật 2 chiều (Giao thoa):
            </span>
            <div className="chips-container">
              {daysBoth.map(d => <span key={d} className="chip warning">{d}</span>)}
            </div>
          </div>
          
          <div>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Tất cả ngày chú ý (Hợp):
            </span>
            <div className="chips-container">
              {daysAll.map(d => <span key={d} className="chip">{d}</span>)}
            </div>
          </div>
        </div>

      </div>

      {/* Danh mục Bạc (Dictionary) */}
      <h3 style={{ marginTop: '2rem', marginBottom: '0.5rem', color: 'var(--text-secondary)', fontSize: '1rem' }}>
        Dictionary: Danh mục các loại Bạc hiện nay
      </h3>
      <div style={{ overflowX: 'auto' }}>
        <table className="data-table">
          <thead>
            <tr>
              <th>Loại Bạc</th>
              <th>Độ Tinh Khiết (%)</th>
              <th>Giá Bán Ra (VND/chỉ)</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(silverTypes).map(([name, info]) => (
              <tr key={name}>
                <td style={{ fontWeight: 500 }}>{name}</td>
                <td>{info.do_tinh_khiet}%</td>
                <td style={{ color: 'var(--accent-color)' }}>{info.gia_ban_chi.toLocaleString('vi-VN')}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}
