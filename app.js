var express = require("express");
var app = express();

app.get("/",function(req,res) {
    res.send("Hello world")
})


var server = app.listen(8080,function() {
    console.log("Listening at " + server.address().address + ": " + server.address().port);
});