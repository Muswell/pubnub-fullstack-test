import sys,getopt,logging

class ENV(object):
    cli_params = None
    operands = {} 
    _env = None
    @staticmethod
    def parse_cli(cli_params):
        if ENV.cli_params != None:
            return ENV.operands

        ENV.cli_params = cli_params
        opts, args = getopt.getopt(sys.argv[1:], '',ENV.cli_params)

        for opt,arg in opts: 
            if(len(arg) != 0):
                ENV.operands[opt] = arg
        return ENV.operands

    @staticmethod
    def get_env():
        if( ENV._env == None):
            cli = ENV.parse_cli(ENV.cli_params)
            env = cli.get('--env','local')
        else:
            env = ENV._env

        print "ENV %s" % (env,)
        return env

    @staticmethod
    def set_env(env):
        ENV._env = env
        return ENV
