class RouteMapping(object):

    __routes = dict()

    def __init__(self):
        self.__routes = dict()

    def get(self, route: str(), callback: object()):
        """
        Binds a GET route with the given callback 
        :rtype: object
        """
        self.__set_route('get', {route: callback})
        return RouteMapping

    def post(self, route: str(), callback: object()):
        """
        Binds a POST route with the given callback
        :rtype: object
        """
        self.__set_route('post', {route: callback})
        return RouteMapping

    def put(self, route: str(), callback: object()):
        """
        Binds a PUT route with the given callback
        :rtype: object
        """
        self.__set_route('put', {route: callback})
        return RouteMapping

    def patch(self, route: str(), callback: object()):
        """
        Binds a PATCH route with the given callback
        :rtype: object
        """
        self.__set_route('patch', {route: callback})
        return RouteMapping

    def delete(self, route: str(), callback: object()):
        """
        Binds a PUT route with the given callback
        :rtype: object
        """
        self.__set_route('delete', {route: callback})
        return RouteMapping

    def head(self, route: str(), callback: object()):
        """
        Binds a HEAD route with the given callback
        :rtype: object
        """
        self.__set_route('head', {route: callback})
        return RouteMapping

    def options(self, route: str(), callback: object()):
        """
        Binds a OPTIONS route with the given callback
        :rtype: object
        """
        self.__set_route('options', {route: callback})
        return RouteMapping

    def __set_route(self, type_route, route):
        """
        Sets the given type_route and route to the route mapping
        :rtype: object
        """
        if type_route in self.__routes:
            self.__routes[type_route].append(route)
        else:
            self.__routes[type_route] = [route]
        return RouteMapping

    def get__routes(self):
        """
        Gets the mapped routes
        :rtype: dict
        """
        return self.__routes
