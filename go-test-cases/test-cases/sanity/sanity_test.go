package ourtest

// global imports
import (
    "testing"
    "fmt"
    "context"
    "time"
)

// test harness imports
import (
    "api"
)

func TestConnections(t *testing.T) {
    ctx := context.Background()
    config := api.ReadSettings("../../client_settings/settings.json")
    controller := config.Controller

    client := api.Connect(ctx, controller)

    if (client.Error != nil)  {
	t.Errorf("Error %s", client.Error)
    } else {
        fmt.Printf("Status code = %d, response = %s\n",
	           client.Response.StatusCode(),
		   string(client.Response.Body))

        fmt.Printf("GREAT SUCCESS\n")
    }

    api.LoadConfig(&client, "bidirectional_ethernet.json")
    if (client.Error != nil)  {
        t.Errorf("Error %s", client.Error)
    } else {
        fmt.Printf("Status code = %d, response = %s\n",
                   client.Response.StatusCode(),
                   string(client.Response.Body))

        fmt.Printf("GREAT SUCCESS\n")
    }

    api.GetConfig(&client)
    if (client.Error != nil)  {
        t.Errorf("Error %s", client.Error)
    } else {
        fmt.Printf("Status code = %d, response = %s\n",
                   client.Response.StatusCode(),
                   string(client.Response.Body))
        fmt.Printf("GREAT SUCCESS\n")
    }

    flows := []string{"p1-p2", "p2-p1"}
    api.Traffic(&client, &flows, "start")
    if (client.Error != nil)  {
        t.Errorf("Error %s", client.Error)
    } else {
        fmt.Printf("Status code = %d, response = %s\n",
                   client.Response.StatusCode(),
                   string(client.Response.Body))
        fmt.Printf("GREAT SUCCESS (Traffic Started)\n")
    }

    fmt.Printf("Running traffic for 5 seconds\n")
    time.Sleep(5 * time.Second)

    api.GetState(&client)
    if (client.Error != nil)  {
        t.Errorf("Error %s", client.Error)
    } else {
        fmt.Printf("Status code = %d, response = %s\n",
                   client.Response.StatusCode(),
                   string(client.Response.Body))
        fmt.Printf("GREAT SUCCESS (Traffic Started)\n")
    }

}
