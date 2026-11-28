"""Make the NYTimes RSS compatible with Today's News. Read XML on stdin."""

import sys
from xml.dom import Node, minidom


ATOM = "http://www.w3.org/2005/Atom"
MEDIA = "http://search.yahoo.com/mrss/"


def children(node, name):
    return [child for child in node.childNodes
            if child.nodeType == Node.ELEMENT_NODE and child.tagName == name]


def has_text(node, name):
    return any(part.data.strip() for element in children(node, name)
               for part in element.childNodes
               if part.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE))


def clean_feed(data):
    document = minidom.parseString(data)
    root = document.documentElement
    channels = children(root, "channel")
    if root.tagName != "rss" or len(channels) != 1:
        raise ValueError("Expected an RSS channel")

    channel = channels[0]
    items = children(channel, "item")
    if not any(has_text(item, "title") and has_text(item, "link") for item in items):
        raise ValueError("Feed contains no articles with a title and link")

    # Point an importing reader at this copy if it follows the feed's self link.
    for link in channel.getElementsByTagNameNS(ATOM, "link"):
        if link.parentNode == channel and link.getAttribute("rel") == "self":
            link.setAttribute("href", "https://caadfutures2025.hku.hk/ARCH7476/data/feeds/nyt.xml")

    for item in items:
        # Today's News matches these fields by local name. Preserve the RSS
        # article URL and summary when the publisher also includes media tags.
        for element in list(item.childNodes):
            if element.nodeType != Node.ELEMENT_NODE:
                continue
            if (element.namespaceURI, element.localName) in (
                (ATOM, "link"), (MEDIA, "description")
            ) and has_text(item, element.localName):
                item.removeChild(element)
    return document.toxml(encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.buffer.write(clean_feed(sys.stdin.buffer.read()))
