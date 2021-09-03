import re

map = {}


def get_meta(page):
    start = page.index('<head>')
    while True:
        meta_start = page.index('<meta', start)
        meta_end = page.index('>', meta_start)
        if page.find('content="', meta_start, meta_end) >= 0:
            s = page.find('content="', meta_start, meta_end) + len('content="')
            e = page.find('"', s)
            return page[s:e]
        start = meta_end + 1


def get_content_link(html: str):
    pattern = re.compile('<meta property="og:url" content="https://\S+"')
    match = pattern.search(html)
    s = match.start()
    e = match.end()

    return html[s:e].split("=")[-1][1:-1]


def count(html: str, word):
    lst = html.split('\n')
    body_s = lst.index('<body>')
    body_e = lst.index('</body>')
    body = lst[body_s:body_e + 1]
    cnt = 0
    link_count = 0
    for str in body:
        if '<a href=' in str:
            link_count += 1

        res = ''
        for x in str.lower():
            if x.isalpha():
                res += x
            else:
                if res == word.lower():
                    cnt += 1
                res = ''
        if res == word.lower():
            cnt += 1

    return cnt, link_count


def get_linked_links(html: str):
    global map
    lst = html.split('\n')
    body_s = lst.index('<body>')
    body_e = lst.index('</body>')
    body = lst[body_s:body_e + 1]
    out_links = []

    for str in body:
        if '<a href="' in str:
            link = str.split('"')[1]
            out_links.append(link)

    return out_links


def solution(word, pages):
    global map
    links = []
    for i in range(len(pages)):
        # link = get_content_link(pages[i])
        link = get_meta(pages[i])
        links.append(link)
        cnt, link_cnt = count(pages[i], word)
        map[link] = {}
        map[link]["index"] = i
        map[link]["count"] = cnt
        map[link]["link_count"] = link_cnt
        map[link]["linked_score"] = 0
        map[link]["links"] = get_linked_links(pages[i])
    for link in map:
        for linked in map[link]["links"]:
            if linked in map:
                map[linked]["linked_score"] += map[link]["count"] / len(map[link]["links"])

    best = float('-inf')
    idx = 0

    for link in map:
        if best < map[link]["count"] + map[link]["linked_score"]:
            best = map[link]["count"] + map[link]["linked_score"]
            idx = map[link]["index"]

    return idx


pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"
]

pages2 = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml \">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos/Muzi/Muzi/Muzi\"></a>\n\n\t^\n</body>\n</html>"
]

word = 'blind'
word2 = "Muzi"
print(solution(word2, pages2))
