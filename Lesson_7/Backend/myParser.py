'''
Image parser for getting list of images` urls from website\n
Main function is getImageListByUrl
'''
from rich.console import Console
from urllib.request import urlopen

log = Console().log


# main function
def getImageListByUrl(url: str) -> list[str]:
    '''Returns images` urls list for dowmloading by url'''
    extentions = [
        ".jpeg", ".jpg", ".png", ".ico",
        ".gif", ".tiff", ".tif", ".svg",
        ".eps", ".bmp", ".dib"
        ]
    html = str(urlopen(url).read())
    result = []
    # log(html)

    index = 0
    temp = html
    while True:
        temp_index = temp.find(".")
        # exit from while True
        if temp_index == -1:
            break
        index += temp_index

        for extention in extentions:
            # checking each extention
            if html[index : index + len(extention)] == extention:
                # adding unique result
                img_url = extractUrlFromHTML(html[: index + len(extention)], url)
                if img_url not in result:
                    result.append(img_url)
                break

        # deleting checked html
        temp = temp[temp_index + 1:]
        index += 1
    return result


# helpfull function 
def extractUrlFromHTML(html: str, url: str) -> str:
    '''Returns last url from text (adds start of url if url in html not full)'''
    start_symbols = ["'", '"', ";", "("]
    start = max(filter(lambda index: index != 1, [html[::-1].find(symbol) * (-1) for symbol in start_symbols]))
    result = html[start:]
    # if full url
    if "://" in result:
        return result
    # if not full url
    else:
        url += "/"
        # getting index of first "/" after "://"
        end = url.find("/", url.find("://") + 3)
        return url[:end] + result

# url = "https://ru.wallpaper.mob.org/"
# log(getImageListByUrl(url))