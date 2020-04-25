FORMAT: 1A
# cina API
cinaのoAPIの使用書

<br>

# 認証関連
## ユーザ登録 [/api/v1/rest-auth/registration/]
### POST
+ Request (application/json)

    + username: ユーザー名(ログインでは使用しない)
    + email: メールアドレス(ログインで使用)
    + password1: パスワード 
    + password2: 確認用パスワード

+ Response 201 (application/json)
    ```
    {
        key: 認証用のトークン
    }
    ```
<br>

## ログイン [/api/v1/rest-auth/login/]
### POST
+ Request (application/json)

    + username: メールアドレス(ユーザー名ではないので注意)
    + password: パスワード

+ Response 200 (application/json)
    ```
    {
        key: 認証用のトークン
    }
    ```
<br>


## ログアウト [/api/v1/rest-auth/logout/]
### POST
+ Response 200 (application/json)
    ```
    {
        "detail": "Successfully logged out."
    }
    ```
<br>

# ユーザー関連
## ユーザーリスト [/api/v1/user_info/users/]
### GET
+ Response 200 (application/json)
    ```
    [
        {
            "uuid": ユーザーID,
            "username": ユーザー名,
            "email": メールアドレス
        },
    ]
    ```
<br>

## 個別ユーザー情報 [/api/v1/user_info/users/[uuid]/]
### GET
+ Response 200 (application/json)
    ```
    {
        "uuid": ユーザーID,
        "username": ユーザー名,
        "email": メールアドレス
    }
    ```
<br>

# ワークスペース関連
## ワークスペースリスト
### GET
+ Response 200 (application/json)
    ```
    [
        {
            "id": ワークスペースID,
            "workspace_name": ワークスペース名,
            "admin": 管理者のユーザID
        },
    ]
    ```
<br>

## 個別ワークスペース情報 [/api/v1/user_info/users/[uuid]/]
### GET
+ Response 200 (application/json)
    ```
    {
        "id": ワークスペースID,
        "workspace_name": ワークスペース名,
        "admin": 管理者のユーザID
    }
    ```
<br>

## ワークスペースにユーザーを追加 [/api/v1/user_info/workspaces/1/add_user/]
### POST
+ Request (application/json)
    ```
    {
        "add_user": ユーザーのメールアドレス
    }
    ```

+ Response 200 (application)
    ```
    {
        "status": "success"
    }
    ```
<br>

## ワークスペースの存在確認 [/api/v1/user_info/workspaces/exist_workspace/?workspace_name=[ワークスペース名]]
### GET
+ Response 200 (application/json)
    ```
    {
        "exist": true
    }
    ```
<br>

# ユーザーとワークスペースの対応 [/api/v1/user_info/workspacetable/]
## 対応表取得
### GET
+ Response
    ```
    [
        {
            "id": テーブルID,
            "workspace": ワークスペースID,
            "user": ユーザーID,
            "user_authority": ユーザーの権限
        },
    ]
    ```
