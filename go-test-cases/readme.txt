export GOPATH=$HOME/automation/go-test-cases/imports/
# get the go otg client
# https://github.com/open-traffic-generator/models/releases/download/v0.4.0/goclient.tar.gz
# unzip tar -zxvf goclient.tar.gz ---> client.go
# copy the client.go to $GOPATH/otgclient  
go build otgclient
go build api

