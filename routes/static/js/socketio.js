document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket location.protocol
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Set default room
    let room = "Default"

    socket.on('connect', () => {
        socket.send({'msg':"I\'m connected", 'username': username, 'room': room});
    });

    // Display all incoming messages 從 main.py def message出發!
    socket.on('message', data => {
        const p = document.createElement('p');
        const span_username = document.createElement('span')
        const span_timestamp = document.createElement('span')
        const br = document.createElement('br');
        span_username.innerHTML = data.username
        span_timestamp.innerHTML = data.time_stamp
        p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
        document.querySelector('#display-message-section').append(p)
    });

    //  擷取 網頁上的元素中的值 以及 從flask後端傳來存放在javascript的變數值
    // Send Message
    document.querySelector('#send_message').onclick = () => {  // 從其中一位user client發出
        msg_Check = document.querySelector('#user_message').value
        if (msg_Check !== "" && room != "Default") {
            socket.send({'msg': msg_Check, 'username':username, 'room': room});
            document.querySelector('#user_message').value = '';  // 清空"輸入訊息欄位"
        }
    }

    // Room selection
    document.querySelectorAll('.select-room').forEach( p => {
        p.onclick = () => {
            let newRoom = p.innerHTML;
            console.info(room);
            if (newRoom == room) { //若user已經在該room->顯示系統訊息
                msg = `You are already in ${room} room.`
                printSysMsg(msg);
            } else { //若user不在該room->切換
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        }
    });

    // Leave Room
    function leaveRoom(room) {
        socket.emit('leave', {
            'username': username,
            'room': room
        });
    }

    // Join Room
    function joinRoom(newRoom) {
        socket.emit('join', {
            'username': username,
            'room': newRoom
        });
        document.querySelector('#display-message-section').innerHTML = ''
        document.querySelector('#user_message').focus();
    }

    // Print system message
    function printSysMsg(msg) {
        const p = document.createElement('p')
        p.innerHTML = msg;
        document.querySelector('#display-message-section').append(p);
    }

//    // Retrieve username
//    const username = document.querySelector('#get-username').innerHTML;
//
//    // Set default room
//    let room = "Lounge"
//    joinRoom("Lounge");
//
//    // Send messages
//    document.querySelector('#send_message').onclick = () => {
//        socket.emit('incoming-msg', {'msg': document.querySelector('#user_message').value,
//            'username': username, 'room': room});
//
//        document.querySelector('#user_message').value = '';
//    };


    // Select a room
//    document.querySelectorAll('.select-room').forEach(p => {
//        p.onclick = () => {
//            let newRoom = p.innerHTML
//            // Check if user already in the room
//            if (newRoom === room) {
//                msg = `You are already in ${room} room.`;
//                printSysMsg(msg);
//            } else {
//                leaveRoom(room);
//                joinRoom(newRoom);
//                room = newRoom;
//            }
//        };
//    });

//    // Logout from chat
//    document.querySelector("#logout-btn").onclick = () => {
//        leaveRoom(room);
//    };

//    // Trigger 'leave' event if user was previously on a room
//    function leaveRoom(room) {
//        socket.emit('leave', {'username': username, 'room': room});
//
//        document.querySelectorAll('.select-room').forEach(p => {
//            p.style.color = "black";
//        });
//    }

//    // Trigger 'join' event
//    function joinRoom(room) {
//
//        // Join room
//        socket.emit('join', {'username': username, 'room': room});
//
//        // Highlight selected room
//        document.querySelector('#' + CSS.escape(room)).style.color = "#ffc107";
//        document.querySelector('#' + CSS.escape(room)).style.backgroundColor = "white";
//
//        // Clear message area
//        document.querySelector('#display-message-section').innerHTML = '';
//
//        // Autofocus on text box
//        document.querySelector("#user_message").focus();
//    }
//
//    // Scroll chat window down
//    function scrollDownChatWindow() {
//        const chatWindow = document.querySelector("#display-message-section");
//        chatWindow.scrollTop = chatWindow.scrollHeight;
//    }
//
//    // Print system messages
//    function printSysMsg(msg) {
//        const p = document.createElement('p');
//        p.setAttribute("class", "system-msg");
//        p.innerHTML = msg;
//        document.querySelector('#display-message-section').append(p);
//        scrollDownChatWindow()
//
//        // Autofocus on text box
//        document.querySelector("#user_message").focus();
//    }
});