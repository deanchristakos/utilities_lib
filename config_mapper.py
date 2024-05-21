import configparser


class ConfigSectionMap:

    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config.read(configfile)
        self.sections = dict()

    def section_map(self, section):

        try:
            result = self.sections[section]
        except KeyError:
            result = dict()
            options = self.config.options(section)
            for option in options:
                try:
                    result[option] = self.config.get(section, option)
                    if result[option] == -1:
                        print("skip: %s" % option)
                except:
                    print("exception on %s!" % option)
                    result[option] = None
            self.sections[section] = result
        return result
