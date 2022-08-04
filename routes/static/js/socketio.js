document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket location.protocol
    //var socket = io.connect('http://' + document.domain + ':' + location.port);
    var protocol = window.location.protocol;
    var socket = io.connect(protocol + '//' + document.domain + ':' + location.port);
    // Set default room
    let room = "global"

    // Leave Room
    function leaveRoom() {
        socket.emit('leave', {
            'username': username,
            'room': room
        });
    }

    // Join Room
    function joinRoom() {
        socket.emit('join', {
            'username': username,
            'room': room
        });
        document.querySelector('#user_message').focus();
    }

//    function deleteMsg(id) {
//        socket.emit('delete-event', {
//            'id': id
//        });
//    }
    socket.on('connect', () => {
        joinRoom();
    });


    // Display all incoming messages 從 main.py def message出發!
    socket.on('message', data => {
        //判斷 自己 或者是其他user display 格式
        if(data.username == username){ // 本人
            const div_layer1 = document.createElement('div');
            const div_layer2 = document.createElement('div');
            const div_layer3_1 = document.createElement('div');
            const div_layer3_2 = document.createElement('div');
            const ul = document.createElement('ul');
            const li1= document.createElement('li');
            const li2= document.createElement('li');
            const li3= document.createElement('li');
            const a1 = document.createElement('a');
            const a2 = document.createElement('a');
            const a3 = document.createElement('a');
            div_layer1.className = "iconTag message_row you-message";
            div_layer2.className = "message-content dropstart";
            div_layer3_1.className = "message-text";
            div_layer3_2.className = "message-time";
            ul.className = "dropdown-menu";
            a1.className = "dropdown-item";
            a2.className = "dropdown-item";
            a3.className = "dropdown-item";
            ul.setAttribute("aria-labelledby", "dropdownMenuLink");
            a1.setAttribute("href", "#");
            a2.setAttribute("href", "#");
            a3.setAttribute("href", "#");

            div_layer3_1.innerHTML = data.msg;
            div_layer3_2.innerHTML = data.time_stamp;
            a1.innerHTML = "編輯";
            li1.innerHTML = a1.outerHTML;
            a2.innerHTML = "刪除";
            li2.innerHTML = a2.outerHTML;
            a3.innerHTML = "複製";
            li3.innerHTML = a3.outerHTML;
            ul.innerHTML = li1.outerHTML + li2.outerHTML + li3.outerHTML;
            div_layer2.innerHTML = ul.outerHTML + div_layer3_1.outerHTML + div_layer3_2.outerHTML;
            div_layer1.innerHTML = div_layer2.outerHTML;
            document.querySelector('#display-message-section').append(div_layer1)
        } else { // 其他users
            const div_layer1 = document.createElement('div');
            const div_layer2 = document.createElement('div');
            const div_layer3_1 = document.createElement('div');
            const div_layer3_2 = document.createElement('div');
            img_layer = document.createElement('img');
            div_layer1.className = "message_row other-message";
            div_layer2.className = "message-content";
            img_layer.className = "head";
            div_layer3_1.className = "message-text";
            div_layer3_2.className = "message-time";
            img_layer.src = "data:image/png;base64,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"
            div_layer3_1.innerHTML = data.username +":<br />"+ data.msg.replace(/\n/g, "<br />");;
            div_layer3_2.innerHTML = data.time_stamp;
            div_layer2.innerHTML = img_layer.outerHTML + div_layer3_1.outerHTML + div_layer3_2.outerHTML;
            div_layer1.innerHTML = div_layer2.outerHTML;
            document.querySelector('#display-message-section').append(div_layer1)
        }
    });

    //  擷取 網頁上的元素中的值 以及 從flask後端傳來存放在javascript的變數值
    // Send Message
    document.querySelector('#send_message').onclick = () => {  // 從其中一位user client發出
        msg_Check = document.querySelector('#user_message').value
        if (msg_Check !== "") {
            socket.send({'msg': msg_Check, 'username':username, 'room': room});
            document.querySelector('#user_message').value = '';  // 清空"輸入訊息欄位"
        }
    }



    // Print system message
    function printSysMsg(msg) {
        const p = document.createElement('p')
        p.innerHTML = msg;
        document.querySelector('#display-message-section').append(p);
    }

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

    // Logout from chat
    document.querySelector("#logout-btn").onclick = () => {
        leaveRoom();
    };

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