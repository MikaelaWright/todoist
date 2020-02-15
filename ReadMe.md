
## POST ##
`curl -d '{"desc":"car fix"}' -X POST http://127.0.0.1:5000/todos
`
## DELETE ##
`curl -d '{"idx":0}' -X DELETE http://127.0.0.1:5000/todos`

## PUT ##
`curl -d '{"desc":"get groceries","idx":0}' -X PUT http://127.0.0.1:5000/todos`

## GET ##
`curl http://127.0.0.1:5000/todos`