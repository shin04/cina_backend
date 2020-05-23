FORMAT: 1A
# cina API

# 認証関連
## ユーザ登録 [/api/v1/rest-auth/registration/]
### POST
+ Request (application/json)
    + Body 
        ```
        {
            username: ユーザー名(ログインでは使用しない)
            email: メールアドレス(ログインで使用)
            password1: パスワード 
            password2: 確認用パスワード
        }
        ```
+ Response 201 (application/json)
    + Body
        ```
        {
            key: 認証用のトークン
        }
        ```
## ログイン [/api/v1/rest-auth/login/]
### POST
+ Request (application/json)
    + Body
        ```
        {
            username: メールアドレス(ユーザー名ではないので注意)
            password: パスワード
        }
        ```
+ Response 200 (application/json)
    + Body
        ```
        {
            key: 認証用のトークン
        }
        ```
## ログアウト [/api/v1/rest-auth/logout/]
### POST
+ Response 200 (application/json)
    + Body
        ```
        {
            "detail": "Successfully logged out."
        }
        ```

# ユーザー関連
## ユーザーリスト [/api/v1/user_info/users/]
### GET
+ Response 200 (application/json)
    + Body
        ```
        [
            {
                "uuid": ユーザーID,
                "username": ユーザー名,
                "email": メールアドレス
            },
        ]
        ```
## 個別ユーザー情報 [/api/v1/user_info/users/[uuid]/]
### GET
+ Response 200 (application/json)
    + Body
        ```
        {
            "uuid": ユーザーID,
            "username": ユーザー名,
            "email": メールアドレス
        }
        ```

# ワークスペース関連
## ワークスペースリスト
### GET
+ Response 200 (application/json)
    + Body
        ```
        [
            {
                "id": ワークスペースID,
                "workspace_name": ワークスペース名,
                "admin": 管理者のユーザID
            },
        ]
        ```
### POST

- Request(application/json)

  - Body

    ```json
    {
      "workspace_name": ワークスペース名,
      "admin": 管理者のユーザID
    }
    ```

- Response(application/json)

  - Bdy

    ```
    {
        "id": ID,
        "workspace_name": ワークスペース名,
        "admin": 管理者のユーザID
    }
    ```

    

## 個別ワークスペース情報 [/api/v1/user_info/users/[uuid]/]
### GET
+ Response 200 (application/json)
    + Body
        ```
        {
            "id": ワークスペースID,
            "workspace_name": ワークスペース名,
            "admin": 管理者のユーザID
        }
        ```
## ワークスペースにユーザーを追加 [/api/v1/user_info/workspaces/1/add_user/]
### POST
+ Request (application/json)
    + Body
        ```
        {
            "add_user": ユーザーのメールアドレス
        }
        ```
+ Response 200 (application)
    + Body
        ```
        {
            "status": "success"
        }
        ```
## ワークスペースの存在確認 [/api/v1/user_info/workspaces/exist_workspace/?workspace_name=[ワークスペース名]]
### GET
+ Response 200 (application/json)
    + Body
        ```
        {
            "exist": true
        }
        ```

# ユーザーとワークスペースの対応
## 対応表取得 [/api/v1/user_info/workspacetable/]
### GET
+ Response
    + Body
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
## ワークスペース内のユーザー一覧取得 [/api/v1/user_info/workspacetable/users_by_workspace?workspace=[ワークスペース名]]
### GET
+ Resuponse
    + Body
        ```
        [
            {
                "authority": ワークスペース内でのユーザの権限,
                "email": ユーザのメールアドレス,
                "uuid": ユーザのID
            },
        ]
        ```

