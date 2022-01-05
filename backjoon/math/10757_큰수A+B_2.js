const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const and = (param1, param2) => param1 && param2;
const or = (param1, param2) => param1 || param2;
const xor = (param1, param2) => !param1 === param2;
const sum = (bitA, bitB) => xor(bitA, bitB);
const carry = (bitA, bitB) => and(bitA, bitB);

const halfadder = (bitA, bitB) => [carry(bitA, bitB), sum(bitA, bitB)];
const fulladder = (bitA, bitB, carryN) => {
  const [carryA, sumA] = halfadder(bitA, bitB);
  const [carryB, sumB] = halfadder(carryN, sumA);
  return [or(carryA, carryB), sumB];
};

const getMaxByteLength = (byteA, byteB) => {
  return Math.max(byteA.length, byteB.length);
};

const fillByte = (byte, maxLength) => {
  const zeros = new Array(maxLength - byte.length).fill(false);
  return [...byte, ...zeros];
};

const getEqualByte = (byteA, byteB) => {
  const byteLength = getMaxByteLength(byteA, byteB);
  return [
    byteA.length < byteLength ? fillByte(byteA, byteLength) : byteA,
    byteB.length < byteLength ? fillByte(byteB, byteLength) : byteB,
  ];
};

const byteadder = (byteA, byteB) => {
  if (byteA.length !== byteB.length) {
    const [newByteA, newByteB] = getEqualByte(byteA, byteB);
    return byteadder(newByteA, newByteB);
  }
  const answer = [];
  const lastCarryN = byteA.reduce((prevCarryN, bitA, bitIndex) => {
    const bitB = byteB[bitIndex];
    const [nextCarryN, sum] = fulladder(bitA, bitB, prevCarryN);
    answer.push(sum);
    return nextCarryN;
  }, false);
  return [...answer, lastCarryN];
};

const divideBigInt = (quotient) => {
  const binary = [];
  while (quotient >= 2n) {
    const remainder = quotient % 2n;
    binary.push(remainder);
    quotient = quotient / 2n;
  }
  binary.push(quotient);
  return binary.map((v) => Number(v));
};

const divideInt = (quotient) => {
  const binary = [];
  while (quotient >= 2) {
    const remainder = quotient % 2;
    binary.push(remainder);
    quotient = parseInt(quotient / 2);
  }
  binary.push(quotient);
  return binary;
};

const dec2bin = (decimal) => {
  let quotient = decimal;
  const binary =
    typeof quotient === "bigint" ? divideBigInt(quotient) : divideInt(quotient);
  return binary;
};

const bin2dec = (binary) => {
  if (binary.length > 62) {
    return binary.reduce((result, nextValue, index) => {
      return result + BigInt(nextValue) * 2n ** BigInt(index);
    }, 0n);
  }
  return binary.reduce((result, nextValue, index) => {
    return result + nextValue * 2 ** index;
  }, 0);
};

const numToBool = (array) => array.map((v) => (v === 1 ? true : false));
const boolToNum = (array) => array.map((v) => (v === true ? 1 : 0));

const solution = (input) => {
  const [a, b] = input.split(" ").map((v) => BigInt(v));
  const sum = byteadder(numToBool(dec2bin(a)), numToBool(dec2bin(b)));
  return bin2dec(boolToNum(sum)) + "";
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
