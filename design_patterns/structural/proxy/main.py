# Proxy is a structural design pattern that provides an object that acts as a substitute for a
# real service object used by a client. A proxy receives client requests, does some work
# (access control, caching, etc.) and then passes the request to a service object.

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self):
        print("RealSubject: Handling request")


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self._check_access():
            self._real_subject.request()
            self._log_access()

    def _check_access(self):
        print("Proxy: Checking access")
        return True

    def _log_access(self):
        print("Proxy: Logging access")


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    proxy.request()
