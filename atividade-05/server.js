const express = require('express')
const path = require('path')
const http = require('http')
const socketIO = require('socket.io')

const app = express()
const server = http.createServer(app)
const io = socketIO(server)

server.listen(3000)

app.use(express.static(path.join(__dirname, 'public')))

let rooms = []

io.on('connection', (socket) => {
    console.log("Conexão estabelecida...")

    socket.on('join-request', (username, room) => {
        socket.username = username;
        socket.join(room)
        socket.room = room

        if (!rooms[room]) {
            rooms[room] = []
        }
        rooms[room].push(username)

        socket.emit('user-ok', rooms[room])
        socket.to(room).emit('list-update', {
            joined: username,
            list: rooms[room]
        })
    })

    socket.on('disconnect', () => {
        if (socket.room) {
            rooms[socket.room] = rooms[socket.room].filter(u => u !== socket.username)
            socket.to(socket.room).emit('list-update', {
                left: socket.username,
                list: rooms[socket.room]
            })
            socket.leave(socket.room)
        }
    })

    socket.on('send-msg', (txt) => {
        let obj = {
            username: socket.username,
            message: txt
        }

        socket.to(socket.room).emit('show-msg', obj)
    })
})