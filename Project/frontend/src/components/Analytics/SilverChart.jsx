import { useState, useEffect } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend
} from 'recharts';

export default function SilverChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/silver-history')
      .then(res => {
        if (!res.ok) throw new Error('Không lấy được dữ liệu lịch sử');
        return res.json();
      })
      .then(result => {
        if (result.status === 'success') {
          setData(result.data);
        } else {
          throw new Error(result.message);
        }
      })
      .catch(err => {
        console.error("Lỗi fetch lịch sử:", err);
        setError(err.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{ color: 'var(--muted)', textAlign: 'center', padding: '40px' }}>Đang tải biểu đồ lịch sử...</div>;
  if (error) return <div style={{ color: 'var(--down)', textAlign: 'center', padding: '40px' }}>Lỗi: {error}</div>;
  if (data.length === 0) return null;

  // Custom Tooltip để format tiền tệ đẹp hơn
  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div style={{ backgroundColor: 'var(--bg-secondary)', padding: '12px', border: '1px solid var(--border)', borderRadius: '8px' }}>
          <p style={{ margin: '0 0 8px 0', color: 'var(--text)', fontWeight: '500' }}>{label}</p>
          <p style={{ margin: '4px 0', color: payload[0].color, fontSize: '12px' }}>
            VN: {payload[0].value.toLocaleString('vi-VN')} VND/Lượng
          </p>
          <p style={{ margin: '4px 0', color: payload[1].color, fontSize: '12px' }}>
            Thế Giới: {payload[1].value.toLocaleString('vi-VN')} USD/oz
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <>
      <div className="section-header" style={{ marginTop: '32px' }}>
        <span className="section-title">Biểu Đồ Biến Động Giá (2023 - 2025)</span>
      </div>
      <p style={{ color: 'var(--muted)', fontSize: '11px', marginBottom: '16px' }}>
        Tái hiện lịch sử giá gốc Thế giới so với giá Bán ra thực tế tại Việt Nam.
      </p>

      <div className="table-wrap" style={{ padding: '16px', height: '350px' }}>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
            <XAxis 
              dataKey="date" 
              stroke="var(--muted)" 
              fontSize={10} 
              tickMargin={10}
              minTickGap={30}
            />
            {/* Trục Y trái cho Giá VN */}
            <YAxis 
              yAxisId="left"
              stroke="var(--accent)" 
              fontSize={10} 
              tickFormatter={(value) => `${(value / 1000000).toFixed(1)}M`}
              domain={['auto', 'auto']}
            />
            {/* Trục Y phải cho Giá TG */}
            <YAxis 
              yAxisId="right" 
              orientation="right" 
              stroke="var(--muted)" 
              fontSize={10}
              domain={['auto', 'auto']}
            />
            <Tooltip content={<CustomTooltip />} />
            <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
            
            <Line 
              yAxisId="left"
              type="monotone" 
              dataKey="vn_price" 
              name="Giá Bạc VN" 
              stroke="var(--accent)" 
              strokeWidth={2} 
              dot={false}
              activeDot={{ r: 4, fill: 'var(--accent)', stroke: 'var(--bg-primary)' }}
            />
            <Line 
              yAxisId="right"
              type="monotone" 
              dataKey="global_price" 
              name="Giá TG (USD)" 
              stroke="var(--muted)" 
              strokeWidth={1.5} 
              dot={false} 
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </>
  );
}
