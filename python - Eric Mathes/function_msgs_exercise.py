def show_messages(messageList, sent_messagesList):
    while messageList:
        message = messageList.pop()
        print(message)
        sent_messages.append(message)

message_list = ['hello','how are you', 'are you hearing me', 'me feeling you']
sent_messages = []

show_messages(message_list[:], sent_messages)
print(message_list)
sent_messages.reverse()
print(sent_messages)