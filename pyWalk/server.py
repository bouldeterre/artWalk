from __future__ import print_function
import sys
import zerorpc


class WalkApi(object):
    def echo(self, text):
        """echo any text"""
        print("Received echo:" + text)
        return "Echoing:" + text


def main():
    addr = "tcp://127.0.0.1:4242"
    s = zerorpc.Server(WalkApi())
    s.bind(addr)
    print("start running on {}".format(addr))
    s.run()


if __name__ == "__main__":
    main()
