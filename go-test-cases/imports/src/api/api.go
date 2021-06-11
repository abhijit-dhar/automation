package api

import (
    "encoding/json"
    "io/ioutil"
    "log"
    "otgclient"
    "context"
    "net/http"
    "crypto/tls"
    // "github.com/openconfig/gnmi/client"
    // "github.com/golang/protobuf/proto"
)


// Structure of the configuration file
// Currently we only support two arms
type Data struct {
    Username string
    Controller string
    Ports[2] string
    Speed string
    Line_rate  int
    Mtu int
    Promiscuous bool
    Timeout_seconds int
    Interval_seconds float32
    Log_level string
    Dynamic_stats_output bool
}


// Structure to manage client
type ClientContext struct {
    Ctx context.Context
    Controller string
    Client *otgclient.ClientWithResponses
    Response *otgclient.SetConfigResponse
    Error error
}


// Function to read test-bed settings. YThe setting is expected to be a a JSON
// file with the format as in the example below
//{
//    "username": "common",
//    "controller": "https://localhost:443",
//    "ports": [
//        "localhost:5555",
//        "localhost:5556"
//    ],
//    "speed": "speed_1_gbps",
//    "line_rate": 10,
//    "mtu": 1600,
//    "promiscuous": true,
//    "timeout_seconds": 300,
//    "interval_seconds": 0.5,
//    "log_level": "info",
//    "dynamic_stats_output": true
//}
func ReadSettings (path string) (data Data) {
    content, err := ioutil.ReadFile(path)
    if (err != nil) {
         log.Fatal("Error in opening the file %s", path)
    }

    var payload Data
    err = json.Unmarshal(content, &payload)
    if (err != nil) {
         log.Fatal("Error in opening the file %s", err)
    }

    return payload
}


// Function to connect to Athena server 
func Connect (ctx context.Context, controller string) (ClientContext) {
    var client ClientContext

    client.Ctx = ctx
    client.Controller = controller

    new_client, err := otgclient.NewClientWithResponses(
        controller,
        otgclient.WithHTTPClient(&http.Client{
            Transport: &http.Transport{
                TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
            },
        }))

    if (err != nil) {
	client.Error = err
        return client
    }

    client.Client = new_client
    response, err := new_client.SetConfigWithResponse(ctx, otgclient.SetConfigJSONRequestBody {})
    client.Response = response
    client.Error = nil

    return client
}


// Function to load JSON config file
func LoadConfig(client *ClientContext, filename string) {
    var config otgclient.SetConfigJSONRequestBody

    data, err := ioutil.ReadFile(filename)
    if (err != nil) {
        log.Fatal("failed reading data from %s: %s\n", filename, err)
        client.Error = err
	return
    }

    myClient := client.Client
    ctx := client.Ctx

    _ = json.Unmarshal([]byte(data), &config)
    response, err := myClient.SetConfigWithResponse(ctx, config)

    client.Response = response
    client.Error = err
    return
}


// Function to get configuration whatever is done
func GetConfig (client *ClientContext) {
    ctx := client.Ctx
    myClient := client.Client

    get_response, err := myClient.GetConfigWithResponse(ctx)

    client.Response.Body = get_response.Body
    client.Response.HTTPResponse = get_response.HTTPResponse
    client.Response.JSON400 = get_response.JSON400
    client.Response.JSON500 = get_response.JSON500
    client.Error = err
    return
}


// Function to start/stop traffic
func Traffic(client *ClientContext, flow_names *[]string, state string) {
    var traffic otgclient.SetTransmitStateJSONRequestBody
    ctx := client.Ctx
    myClient := client.Client

    traffic.State = state
    traffic.FlowNames = flow_names

    start_response, err := myClient.SetTransmitStateWithResponse(ctx, traffic)
    client.Response.Body = start_response.Body
    client.Response.HTTPResponse = start_response.HTTPResponse
    client.Response.JSON200 = start_response.JSON200
    client.Response.JSON400 = start_response.JSON400
    client.Response.JSON500 = start_response.JSON500
    client.Error = err
    return
}


func GetState(client *ClientContext) {
    ctx := client.Ctx
    myClient := client.Client
    var body otgclient.GetMetricsJSONRequestBody
    response, err := myClient.GetMetricsWithResponse(ctx, body)
    client.Response.Body = response.Body
    client.Response.HTTPResponse = response.HTTPResponse
    client.Response.JSON400 = response.JSON400
    client.Response.JSON500 = response.JSON500
    client.Error = err
    return
}
