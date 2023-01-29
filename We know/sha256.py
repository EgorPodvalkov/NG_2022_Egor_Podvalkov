from hashlib import sha256
from string import ascii_lowercase as letters
from threading import Thread
from rich.console import Console

log = Console().log
result = None

# from 2 to 5 (6 and more will take much time, the word crypto taked 7 minutes)
words_length = 4

def generateWords(length: int) -> list[str]:
    '''Returns list of generated words with following lenth'''
    result = []

    for sumIndex in range(len(letters) ** length):
        word = ""
        for step in range(length):
            index = sumIndex % len(letters)
            sumIndex = sumIndex // len(letters)
            word = letters[index] + word
        result.append(word)
    return result


def taskForThread(index: int, userHash: str, pieces_of_words: list[str]):
    '''Finds word that starts on index letter and encrypts in following hash'''
    global result

    for word in pieces_of_words:
        # if other thread find the result
        if result:
            return

        # checking result
        word = letters[index] + word 
        if word == "crypto":
            log("crypto")
        hash = sha256()
        hash.update(word.encode('utf-8'))

        # if this thread find the result
        if hash.hexdigest() == userHash:
            log("Thread №" + str(index) + " finds the word")
            log("Encrypted word is [bold yellow u]" + word)
            result = word
            return


def main():
    threads = []

    userHash = input("Enter your hash (if it wouldn`t have correct length i use my hash):\n")
    if len(userHash) != 64:
        userHash = "106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7"
        log("Ok, so we used my hash)")
    log("words generation")
    pieces_of_words = generateWords(words_length - 1)

    for index in range(len(letters)):
        threads.append(Thread(target=taskForThread, args=(index, userHash, pieces_of_words, )))

    log("Threads №0 - №" + str(len(threads) - 1) + " are getting to work!")
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    log("Threads №0 - №" + str(len(threads) - 1) + " are stopped!")
    if not result:
        log("We don`t find word by your hash ((")

main()
