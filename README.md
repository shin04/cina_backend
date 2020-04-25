# USAGE
## login
POST  
```
/api/v1/rest-auth/login
```
パラメータ  
```
username: ログインに使うメールアドレス
password: ログインに使うパスワード
```

レスポンス
```
ステータス: 200  
key: 認証用のトークン
```

## logout
POST
```
/api/v1/rest-auth/logout
```
レスポンス
```
ステータス: 200  
detail: "Successfully logged out."
```

## register
POST
```
/api/v1/rest-auth/registration
```
パラメータ
```
username: ユーザ名  
email: メールアドレス  
password1: パスワード  
password2: 確認用のパスワード 
```

レスポンス
```
ステータス: 201  
key: 認証用のトークン
```

## user list
GET
```
/api/v1/users
```

レスポンス
```
ステータス: 200
ユーザのリスト
例）
[
    {
        "uuid": "84b28bb4-a161-4c8b-bc57-a33483d20ce3",
        "username": "",
        "email": "admin@admin.com"
    },
    {
        "uuid": "f1d68c5f-a523-41c4-97f5-bb8a3e5e4f53",
        "username": "daishin",
        "email": "daishin@daishin.com"
    },
    {
        "uuid": "20d2cd55-a616-4b2d-a13c-dce6dd0e0f2f",
        "username": "hoge",
        "email": "hoge@hoge.com"
    }
]
```

GET
```
/api/v1/user/{uuid}
```

レスポンス
```
ステータス: 200

```