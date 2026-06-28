# SSRF to gitlab

## Build 

手動build法:
- docker-compose up
- 打tunnel出來，瀏覽器連 127.0.0.1:12345 -> 設root密碼 -> 新增flag repo
    - example: 
        - ssh -D 9999 yourmachine
        - visit 127.0.0.1:12345 with proxy 127.0.0.1:9999
