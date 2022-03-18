import socket
import time


class ClientError(Exception):
    print('Fault')


class Client:
    def __init__(self, addr, port, timeout=None):
        self._addr = addr
        self._port = int(port)
        self._timeout = int(timeout)

    def send(self, cmd):
        with socket.create_connection((self._addr, self._port), self._timeout) as sock:
            sock.sendall(cmd.encode("utf8"))
            buf = sock.recv(1024)
            return buf.decode('utf-8')

    def get(self, key):
        resp = self.send('get ' + key + '\n')
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)
        ret = dict()
        lines = resp.split('\n')
        for line in lines[1:-2]:
            metric = line.split(' ')
            res_key = metric[0]
            res_val = float(metric[1])
            res_ts = int(metric[2])
            if res_key not in ret:
                ret[res_key] = list()
            ret[res_key].append((res_ts, res_val))
            ret[res_key].sort(key=lambda tup: tup[0])

        return ret

    def put(self, key, val, timestamp=None):
        resp = self.send('put ' + key + ' ' + str(val) + ' ' + str(timestamp if timestamp else int(time.time())) + '\n')
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)
