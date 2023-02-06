#Yes I know that It's very primitive at the moment but I'll make it better over time

from nltk.chat.util import Chat, reflections
print("This is a chat robot you can ask whatever you want. if you want to quit just write 'Bye'.")
pairs = [
    ["(hi|Hi)", ["Hi!"]],
    ["(what is your name(.*)|what's your name(.*))", ["My name is Wall-E","I'm Wall-E"]],
    ["Is your name from a movie?", ["Yes! My name comes from Wall-E."]],
    ["Your name is cute",["Thank youu!"]],
    ["how old are you(.*)", ["I don't have age but i was produced in 2023"]],
    ["who produced you(.*)", ["A lovely company"] ],
    ["(what is your job|why were you produced)", ["I was made to chat with people so this is my job and i love it"]],
    ["Bye" , ["Bye! Have nice day"]]
]

chat = Chat(pairs, reflections)
chat.converse(quit="Bye")