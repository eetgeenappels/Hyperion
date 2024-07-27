// generate chatlog


const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }
}

function generateChatLog(chatData) {


    const chatLog = document.createElement('div');
    chatLog.classList.add('chat_log');

    chatData.log.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');

        const containerDiv = document.createElement('div');
        containerDiv.classList.add('container');

        const itemSvgDiv = document.createElement('div');
        itemSvgDiv.classList.add('item');
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('width', '30');
        svg.setAttribute('height', '30');
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', '15');
        circle.setAttribute('cy', '15');
        circle.setAttribute('r', '15');
        if (message.role === 'user') {
            circle.setAttribute('fill', 'red');
        } else if (message.role === 'assistant') {
            circle.setAttribute('fill', 'blue');
        }
        svg.appendChild(circle);
        itemSvgDiv.appendChild(svg);

        const itemTextDiv = document.createElement('div');
        itemTextDiv.classList.add('item');
        const roleText = document.createElement('p');
        roleText.textContent = message.role === 'user' ? 'Human' : 'AI';
        itemTextDiv.appendChild(roleText);

        containerDiv.appendChild(itemSvgDiv);
        containerDiv.appendChild(itemTextDiv);

        const contentP = document.createElement('p');
        contentP.textContent = message.content;

        messageDiv.appendChild(containerDiv);
        messageDiv.appendChild(contentP);

        chatLog.appendChild(messageDiv);
        chatLog.appendChild(document.createElement('br'));
    });

    return chatLog;
}

function submitPrompt(event) {
    console.log( `Form Submitted! Timestamp: ${event.timeStamp}`);
    event.preventDefault();

    const inputValue = document.getElementById('id_prompt').value;

    inputValue.value = "";


    fetch(textgen_url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
        },
        csrfmiddlewaretoken: csrfToken,
        body: JSON.stringify({ prompt: inputValue })
    }).then(response => {
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        return reader.read().then(
		function processText({ done, value }) {
		    if (done) {
			console.log('Stream complete');
			return;
		    }
		    var recieved_chat_data = JSON.parse(decoder.decode(value));

                    const chat_log_placeholder = document.getElementById("chat_placeholder");


                    // clear data
                    clearElement(chat_log_placeholder);

                    console.log(recieved_chat_data)

                    chat_log_placeholder.appendChild(generateChatLog(recieved_chat_data));
                    
		    return reader.read().then(processText);
        });
    }).catch(error => console.error('Error:', error));

	
}



const form = document.getElementById("prompt");
form.addEventListener("submit", submitPrompt);

console.log("this is being executed");
const chat_log_placeholder = document.getElementById("chat_placeholder");

// clear data
clearElement(chat_log_placeholder);

chat_log_placeholder.appendChild(generateChatLog(JSON.parse(chat_data.replaceAll("&#x27;",'"'))));
