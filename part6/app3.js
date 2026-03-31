const bills = [
  { number: 100 },
  { number: 90 },
  { number: 80 },
  { number: 60 },
  { number: 82 },
  { number: 66 },
  { number: 27 },
  { number: 1 },
  { number: 9 },
  { number: 8 },
];

const tips = bills
  .filter((calculateTip) => calculateTip.number >= 30)
  .map((calculateTip) => (calculateTip.number * 15) / 100);

const tiips = bills
  .filter((calculateTipp) => calculateTipp.number < 30)
  .map((calculateTipp) => (calculateTipp.number * 20) / 100);

console.log(tips);
console.log(tiips);
