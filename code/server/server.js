
// 通信・MySQLに必要なライブラリを読み込み
var http = require('http');


// HTTPサーバの実行
var server = http.createServer();

// サーバにHTTPリクエストが届いたときのコールバック関数
server.on('request', function(req,res){
	// スマートフォンからのアクセスがPOSTであった場合
	if(req.method == 'POST'){
		// スマートフォンへ返信するデータのヘッダを作成
		res.writeHead(200, {'Content-Type' : req.headers['content-type']});
    	
    	// スマートフォンからデータを受信したときの処理 (コールバック関数)
    	req.on('data', function(data){
    		// スマートフォンから受信したデータ(文字列)を、文字列に変換
            console.log(data);
    	});

		// スマートフォンから全てのデータを受信したときの処理（コールバック関数）
		req.on('end', function(){
			// スマートフォンへのデータの返信を終了
			res.end();
		});
	}
	// スマートフォンからのアクセスがPOST以外の場合
	else {
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.write('Hello World\n');
		res.end();
	}
});

// スマートフォンからの接続を待ち受けるポート番号の設定(3000番)
server.listen(3000);
