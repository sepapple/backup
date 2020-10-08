var str = "0x2a73fab400000000000000000000000000000000000000000000000000000000000000640000000000000000000000000000000000000000000000000000017367064ede0000000000000000000000000000000000000000000000000000000014b901e10000000000000000000000000000000000000000000000000000000050c06c0100000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000024000000000000000000000000000000000000000000000000000000000000003a0000000000000000000000000000000000000000000000000000000000000000affffffffffffffffffffffffffffffffffffffffffffffffffffffffef5c5d00ffffffffffffffffffffffffffffffffffffffffffffffffffffffffef0725c0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeca60e0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffef0725c0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffef43ea80ffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeca60e0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffef687880ffffffffffffffffffffffffffffffffffffffffffffffffffffffffed819f20fffffffffffffffffffffffffffffffffffffffffffffffffffffffff04fabe0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffee2c0dc0000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000008b3421000000000000000000000000000000000000000000000000000000000092d07400000000000000000000000000000000000000000000000000000000009e391500000000000000000000000000000000000000000000000000000000009e355b000000000000000000000000000000000000000000000000000000000088298b00000000000000000000000000000000000000000000000000000000009cb1ed00000000000000000000000000000000000000000000000000000000008bf5d80000000000000000000000000000000000000000000000000000000000a758d7000000000000000000000000000000000000000000000000000000000071548f8000000000000000000000000000000000000000000000000000000000a143ab0000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff000000000000000000000000000000000000000000000000000000007fffffff";


// ユーザからのキーボード入力を取得する Promise を生成する
function readUserInput(question) {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve, reject) => {
    readline.question(question, (answer) => {
      resolve(answer);
      readline.close();
    });
  });
}

// メイン処理
const digit = async function main() {
  while(true){
  const name = await readUserInput('入力してください。');
  console.log("桁数は: "+ str.search(name));
  }
};

digit();
