const http = require('http') // require the library http into our code.
const fs = require('fs')
const port = 3000 // tells our code what port it's gonna be listening to for our server

const server = http.createServer(function(req,res) {// create our server.
    // everytime someone request a page from our server, this function gets called
    res.writeHead(200, { 'Content-Type': 'text/html' })
    fs.readFile('index.html', function(error,data) {
        if (error) {
            res.writeHead(404)
            res.write('Error: File Not Found')
        } else {
            res.write(data) // this data para is just all the content in index.html
        }
        res.end()
    })
    // res.write('Hello Node')
    // res.end()
})

server.listen(port, function(error) {
    if (error) {
        console.log('something went wrong', error)
    } else {
        console.log('Server is listening on port' + port )
    }
})