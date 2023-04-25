import subprocess
from abc import ABC, abstractmethod


class Ping(ABC):
    """
    The Ping interface declares common operations for both RealPing and
    the ProxyPing.
    """

    @abstractmethod
    def execute(self, address: str) -> None:
        pass

        
class RealPing(Ping):
    """
    The RealPing contains the core logic of pinging an IP address.
    """

    def execute(self, address: str) -> None:
        if address.startswith("192."):
            for i in range(10):
                subprocess.call(["ping", "-n", "1", address])
        else:
            print("RealPing: The IP address must start with '192.'.")


class ProxyPing(Ping):
    """
    The ProxyPing has an interface identical to the RealPing.
    """

    def __init__(self, real_ping: RealPing) -> None:
        self._real_ping = real_ping

    def execute(self, address: str) -> None:
        """
        The ProxyPing can perform some operations before and after the RealPing
        executes the ping command.
        """

        if address == "192.168.0.254":
            print("ProxyPing: Pinging www.google.com with executefree.")
            self._real_ping.execute("www.google.com")
        else:
            self._real_ping.execute(address)


def client_code(ping: Ping, address: str) -> None:
    """
    The client code is supposed to work with all objects (both RealPing and
    ProxyPing) via the Ping interface.
    """

    # ...

    ping.execute(address)

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a RealPing instance:")
    real_ping = RealPing()
    client_code(real_ping, "192.168.0.1")

    print("")

    print("Client: Executing the same client code with a ProxyPing instance:")
    proxy_ping = ProxyPing(real_ping)
    client_code(proxy_ping, "192.168.0.1")

    print("")

    print("Client: Executing the same client code with a ProxyPing instance that pings google.com:")
    client_code(proxy_ping, "192.168.0.254")
