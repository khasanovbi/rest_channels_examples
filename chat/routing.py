# coding=utf-8
from __future__ import unicode_literals

from channels import include, route

from chat.views import ChatWebSocketView, DRFChatWebSocketView

routing = [
    route('websocket.connect', ChatWebSocketView.as_view(), path=r'^default/'),
    # include(DRFChatWebSocketView.as_view(), path=r'^drf/'),
]
