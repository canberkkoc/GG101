### Build


```zsh
## Assuming you have Go in your computer
~/Desktop/Go101 ❯ go mod init
~/Desktop/Go101 ❯ go mod tidy
~/Desktop/Go101 ❯ go get -u
~/Desktop/Go101 ❯ go build -v wildfires.go
```

### Run

```zsh

## You must have postgres on your computer and tables on DB
~/Desktop/Go101 ❯ ./wildfires
2021/09/22 12:26:58 host=localhost port=5432 user=postgres dbname=firewatcher password=postgres sslmode=disable

   ____    __
  / __/___/ /  ___
 / _// __/ _ \/ _ \
/___/\__/_//_/\___/ v4.6.0
High performance, minimalist Go web framework
https://echo.labstack.com
____________________________________O/_______
                                    O\
⇨ http server started on [::]:8000
```
