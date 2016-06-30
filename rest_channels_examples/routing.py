# coding=utf-8
from __future__ import unicode_literals

from channels import include

from chat.routing import routing as chat_routing
from collaborate_editor.routing import routing as collaborate_editor_routing

routing = [
    include(chat_routing, path=r'chat'),
    include(collaborate_editor_routing, path=r'^collaborate_editor'),
]
