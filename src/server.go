package main


import (
	"flag"
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "On page: %s", r.URL.Path[1:])
}

func main() {
	port := flag.Int("port", 3000, "Port for the server to listen on")


	http.HandleFunc("/balls", handler)
	http.ListenAndServe(fmt.Sprintf(":%d", *port),nil)
}

