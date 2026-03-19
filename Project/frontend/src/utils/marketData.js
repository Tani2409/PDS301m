// Lịch sử giá bạc thế giới (USD/oz) trong 8 ngày qua
export const priceHistory = [30.5, 31.2, 29.8, 30.1, 31.5, 32.0, 31.8, 31.9];

// Dictionary lưu thông tin nhiều loại bạc
export const silverTypes = {
  "Bạc 999 (Bạc ta)": { do_tinh_khiet: 99.9, gia_ban_chi: 1200000 },
  "Bạc 925 (Trang sức)": { do_tinh_khiet: 92.5, gia_ban_chi: 1050000 },
  "Bạc đồng xu quốc tế": { do_tinh_khiet: 99.9, gia_ban_chi: 1250000 }
};

// Set các ngày biến động
export const ngayTangManh = new Set(["12/02", "15/02", "18/02"]); 
export const ngayGiamManh = new Set(["14/02", "18/02", "20/02"]);

// Giao thoa và hợp của Set
export const getNgayBienDongHaiChieu = () => {
  return new Set([...ngayTangManh].filter(x => ngayGiamManh.has(x)));
};

export const getTatCaNgayBienDong = () => {
  return new Set([...ngayTangManh, ...ngayGiamManh]);
};

// Tuple lưu hằng số trong Python được biểu diễn bằng Object.freeze() trong JS để thành Immutable
export const CONVERSION_RATES = Object.freeze([1.20565, 31.1034768]);

export const HISTORICAL_HIGHS = Object.freeze([
  [1980, 49.45],
  [2011, 49.51]
]);
