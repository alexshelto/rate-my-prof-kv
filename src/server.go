package main


import (
	"flag"
	"fmt"
	"net/http"
)



type App struct {
	volume string
}



func (a *App) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "lengthe url raw query %d \n", len(r.URL.RawQuery))
	fmt.Fprintf(w,"http method: %s \n", r.Method)



}



func main() {
	port := flag.Int("port", 3000, "Port for the server to listen on")
	flag.Parse()
	fmt.Println("Server started on localhost port", *port)


	// http.HandleFunc("/", handler)
	// http.HandleFunc("/GET", GetKey)
	



	a := App{volume: "hello"}
	http.ListenAndServe(fmt.Sprintf(":%d", *port),&a)
}

