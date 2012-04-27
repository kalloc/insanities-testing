#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from webob.exc import HTTPException
from insanities import web
from debug_dj import technical_500_response

import logging
logger = logging.getLogger(__name__)

class Debug(object):
    def handle(self, env, data, nxt):
        try:
            return nxt(env, data)
        except HTTPException, e:
            raise e
        except Exception, e:
            exc_info = sys.exc_info()
            html = technical_500_response(env, *exc_info)
            response = web.Response(status=500, body=html)
            logger.exception(e)
            return response



