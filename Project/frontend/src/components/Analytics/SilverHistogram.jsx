import { useState, useEffect } from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts';

export default function SilverHistogram() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:5000/api/market/histogram')
      .then(res => res.json())
      .then(result => {
        if (result.status === 'success') {
          setData(result.data);
        }
      })
      .catch(err => console.error("Lỗi fetch histogram:", err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return null;

  return (
    <div className="histogram-container" style={{ padding: '32px' }}>
      <div className="section-header" style={{ marginBottom: '16px' }}>
        <span className="section-title">📊 PHÂN TÍCH MẬT ĐỘ GIÁ (HISTOGRAM)</span>
      </div>
      <p style={{ color: 'var(--muted)', fontSize: '13px', lineHeight: '1.6', marginBottom: '40px' }}>
        Biểu đồ thống kê số lượng ngày mà giá bạc nằm trong từng khoảng giá cụ thể. <br/>
        <span style={{ color: 'var(--accent)' }}>● Mục tiêu:</span> Tìm ra <b>"Vùng giá phổ biến nhất"</b> (cột cao nhất) để xác định ngưỡng hỗ trợ thị trường.
      </p>
      
      <div style={{ height: '400px', width: '100%' }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 60 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
            <XAxis 
              dataKey="range" 
              stroke="var(--muted)" 
              fontSize={10} 
              angle={-45} 
              textAnchor="end"
              interval={0}
              label={{ value: "Khoảng giá (VNĐ/Lượng)", position: 'insideBottom', offset: -45, fill: 'var(--muted)', fontSize: 13, fontWeight: '500' }}
            />
            <YAxis 
              stroke="var(--muted)" 
              fontSize={11}
              label={{ value: "Tần suất (Số ngày)", angle: -90, position: 'insideLeft', offset: -15, fill: 'var(--muted)', fontSize: 13, fontWeight: '500' }}
            />
            <Tooltip 
              cursor={{ fill: 'var(--bg-tertiary)', opacity: 0.4 }}
              content={({ active, payload }) => {
                if (active && payload && payload.length) {
                  return (
                    <div style={{ backgroundColor: 'var(--bg-secondary)', padding: '12px', border: '1px solid var(--border)', borderRadius: '8px' }}>
                      <p style={{ margin: 0, color: 'var(--accent)', fontWeight: 'bold' }}>Khoảng: {payload[0].payload.range}</p>
                      <p style={{ margin: '4px 0 0 0', color: 'var(--text)', fontSize: '12px' }}>Tần suất: <b>{payload[0].value} ngày</b> xuất hiện</p>
                    </div>
                  );
                }
                return null;
              }}
            />
            <Bar dataKey="count" name="Số ngày xuất hiện">
              {data.map((entry, index) => (
                <Cell 
                  key={`cell-${index}`} 
                  fill={entry.count === Math.max(...data.map(d => d.count)) ? 'var(--accent)' : 'var(--muted)'} 
                  fillOpacity={0.6}
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
