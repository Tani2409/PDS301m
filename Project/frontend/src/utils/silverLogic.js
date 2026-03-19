export const OZ_TO_TAEL = 1.20565;

export function convertSilverPrice(usdPerOz, exchangeRate) {
  const usdPerTael = usdPerOz * OZ_TO_TAEL;
  const vndPerTael = usdPerTael * exchangeRate;
  return vndPerTael;
}

export function calculateSpread(bidPrice, askPrice) {
  if (askPrice <= bidPrice) {
    return {
      error: "Giá bán ra phải lớn hơn giá mua vào",
    };
  }

  const spreadValue = askPrice - bidPrice;
  const spreadPercent = (spreadValue / askPrice) * 100;

  let status = "an toan";
  if (spreadPercent > 5) {
    status = "rui ro cao";
  }

  return {
    spreadValue,
    spreadPercent,
    status,
  };
}

export function calculateTotalProfit(transactions) {
  let totalProfit = 0;
  let totalCapital = 0;
  const results = [];

  transactions.forEach((trade, idx) => {
    const capital = trade.buy_price * trade.quantity;
    const revenue = trade.sell_price * trade.quantity;
    const profit = revenue - capital;

    totalCapital += capital;
    totalProfit += profit;
    
    results.push({
      index: idx + 1,
      profit,
    });
  });

  const roiPercent = totalCapital > 0 ? (totalProfit / totalCapital) * 100 : 0;
  
  return {
    totalProfit,
    roiPercent,
    results,
  };
}

export function compareInvestmentVsBank(capital, silverProfit, bankRateAnnual, months) {
  const bankProfit = capital * (bankRateAnnual / 100 / 12) * months;
  
  let conclusion = "";
  let diff = 0;
  
  if (silverProfit > bankProfit) {
    diff = silverProfit - bankProfit;
    conclusion = `Bạc lời hơn gửi Bank. Chênh: +${diff.toLocaleString('vi-VN')} VND`;
  } else if (silverProfit < bankProfit) {
    diff = bankProfit - silverProfit;
    conclusion = `Gửi Bank lời hơn Bạc. Chênh: +${diff.toLocaleString('vi-VN')} VND`;
  } else {
    conclusion = "Hiệu quả tương đương nhau.";
  }

  return {
    bankProfit,
    silverProfit,
    diff,
    conclusion
  };
}

export function calculateBreakEven(purchasePrice, bankRateAnnual, months) {
  // Lãi suất mục tiêu tương ứng với ngân hàng
  const targetReturnPercent = (bankRateAnnual / 100 / 12) * months;
  // Giá bán cần thiết = Giá mua * (1 + tỷ lệ lãi ngân hàng)
  // Lưu ý: Đây là giá bán ra bạn nhận được từ cửa hàng (Bid Price)
  const breakEvenPrice = purchasePrice * (1 + targetReturnPercent);
  const requiredGain = breakEvenPrice - purchasePrice;

  return {
    breakEvenPrice: Math.round(breakEvenPrice),
    requiredGain: Math.round(requiredGain),
    targetReturnPercent: (targetReturnPercent * 100).toFixed(2)
  };
}
