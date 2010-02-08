#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqDescription:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
    
    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Description) is mandatory
        if "Description" not in req.req:
            print("+++ ERROR: requirement '%s' does not contain the "
                  + "tag 'Description'" % req.id)
            req.mark_syntax_error()
            return
        t = req.req['Description']
        # It must not be too long.
        if len(t)>1024:
            print("+++ ERROR: Description is much too long: %d characters" % len(t))
            print("+++        Please consider split up this requirement")
            req.mark_syntax_error()
            return
        if len(t)>255:
            print("+++ WARNING: Description is too long: %d characters" % len(t))
            print("+++          Please consider split up this requirement")
        req.t_Description = t
        del req.req['Description']
            