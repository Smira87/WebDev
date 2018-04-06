import httplib2
import os
from urllib import splituser, splitpasswd
from xmlrpclib import ServerProxy, getparser, ProtocolError, MultiCall


class HTTPSDigestAuthTransport:
    def request(self, host, handler, request_body, verbose=0):
        auth, host = splituser(host)
        username, password = splitpasswd(auth)
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        if verbose:
            h.debuglevel = 1
        h.add_credentials(username, password)
        resp, content = h.request(
            "https://" + host + handler,
            "POST",
            body=request_body,
            headers={'content-type': 'text/xml'})

        if resp.status != 200:
            raise ProtocolError("https://" + host + handler, resp.status,
                                resp.reason, None)
        p, u = getparser(0)
        p.feed(content)
        return u.close()

class HTTPSTrustedAuthTransport:
    def request(self, host, handler, request_body, verbose=0):
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        if verbose:
            h.debuglevel = 1
        resp, content = h.request(
            "https://" + host + handler,
            "POST",
            body=request_body,
            headers={'content-type': 'text/xml'})

        if resp.status != 200:
            raise ProtocolError("https://" + host + handler, resp.status,
                                resp.reason, None)
        p, u = getparser(0)
        p.feed(content)
        return u.close()

def NewClient():
    username = os.environ['SIPPY_API_USER']
    password = os.environ['SIPPY_API_PASS']
    host = os.environ['SIPPY_API_HOST']

    url = "http://{0}:{1}@{2}/xmlapi/xmlapi".format(username, password, host)

    transport = HTTPSDigestAuthTransport()
    return ServerProxy(url, transport, verbose=True, allow_none=True)

def NewClientTrusted():
    host = os.environ['SIPPY_API_HOST']
    url = "http://{0}/xmlapi/xmlapi".format(host)
    transport = HTTPSTrustedAuthTransport()
    return ServerProxy(url, transport, verbose=True, allow_none=True)

def NewMultiCallClient():
    return MultiCall(NewClient())
