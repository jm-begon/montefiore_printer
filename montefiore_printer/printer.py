import subprocess


class Orientation(object):
    PORTRAIT = "Portrait"
    LANDSCAPE = "Landscape"


class Printer(object):

    def __init__(self, n_copies=1, color=False, one_sided=False,
                 orientation=Orientation.PORTRAIT, paper="A4"):

        self.color = color
        self.n_copies = n_copies
        self.one_sided = one_sided
        self.orientation = orientation
        self.paper = paper

    def __repr__(self):
        return "{cls}(n_copies={n_copies}, color={color}, " \
               "one_sided={one_sided}, orientation={orientation}," \
               "paper={paper})".format(cls=self.__class__.__name__,
                                       n_copies=self.n_copies,
                                       color=self.color,
                                       one_sided=self.one_sided,
                                       orientation=self.orientation,
                                       paper=self.paper)

    def get_lrp_options(self):
        options = ["-o media={}".format(self.paper),
                   "-#{}".format(self.n_copies)]
        if self.color:
            options.append("-P lpcolor")

        if self.orientation == Orientation.LANDSCAPE:
            options.append("-o landscape")

        if self.one_sided:
            if self.orientation == Orientation.LANDSCAPE:
                options.append("-o sides=two-sided-short-edge")
            else:
                options.append("-o sides=two-sided-long-edge")

        return ["lrp"] + options

    def __str__(self):
        return " ".join(self.get_lrp_options())

    def print_document(self, fpath):
        response = subprocess.check_call(self.get_lrp_options() + [fpath])
        return "OK" if response == 0 else "*** RETURN CODE:{} ***".format(
            str(response))


class GatewayPrinter(Printer):

    def __init__(self, gateway, n_copies=1, color=False,
                 one_sided=False, orientation=Orientation.PORTRAIT, paper="A4"):
        super(GatewayPrinter, self).__init__(n_copies=n_copies,
                                             color=color,
                                             one_sided=one_sided,
                                             orientation=orientation,
                                             paper=paper)
        self.gateway = gateway

    def __repr__(self):
        return "{cls}(gateway={gateway}, n_copies={n_copies}, color={color}, " \
               "one_sided={one_sided}, orientation={orientation}," \
               "paper={paper})".format(cls=self.__class__.__name__,
                                       gateway=self.gateway,
                                       n_copies=self.n_copies,
                                       color=self.color,
                                       one_sided=self.one_sided,
                                       orientation=self.orientation,
                                       paper=self.paper)

    def __str__(self):
        return " ".join(self.get_lrp_options()) + " {document} | ssh"

    def print_document(self, fpath):
        with open(fpath) as hdl:
            response = subprocess.check_call(("ssh", self.gateway, "lpr {options}".format(options=" ".join(self.get_lrp_options()))),
                                         stdin=hdl.read())
            return "OK" if response == 0 else "*** RETURN CODE:{} ***".format(
                str(response))
